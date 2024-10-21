# Lab 17

*Lab 17 GitHub Classroom link:* https://classroom.github.com/a/Eku_G42u

In this lab, we'll learn how assemble genomes using different software and techniques

1. De novo genome assembly with short read data
2. Genome assembly with short read data against reference genome

This lab is written to be performed through WUSTL RIS, our university's cluster. Review Lab 11 for a refresher on how to use WUSTL RIS.


---

## Configuring your RIS profile

Add this line to the end of `~/.bash_profile`

```console
export STORAGE="/storage1/fs1/workshops/Active/BIO4220"
alias bsub-is="LSF_DOCKER_VOLUMES='${STORAGE}:${STORAGE}' bsub -Is -G compute-workshop -q workshop-interactive -a 'docker(ubuntu)' /bin/bash"
alias bsub-is-4220="LSF_DOCKER_VOLUMES='/storage1/fs1/workshops/Active/BIO4220:/storage1/fs1/workshops/Active/BIO4220' bsub -Is -G compute-workshop -q workshop-interactive -a 'docker(mlandis/biol4220:latest)' /bin/bash"
```

Now you can open an interactive job with RIS by typing `bsub-is-4220`. Note, it takes some time to load pull the Docker image and make a container for the job.

```console
$ bsub-is-4220
Job <783384> is submitted to queue <workshop-interactive>.
<<Waiting for dispatch ...>>
<<Starting on compute1-exec-76.ris.wustl.edu>>
2024-v1: Pulling from mlandis/biol4220
7478e0ac0f23: Pulling fs layer
7616101b52c0: Pulling fs layer

[ ... more text ... ]

michael.landis@compute1-exec-76:~$ # this image has many programs preinstalled
michael.landis@compute1-exec-76:~$ spades --version
SPAdes v3.13.1
michael.landis@compute1-exec-76:~$ bowtie2 --version
/usr/bin/bowtie2-align-s version 2.4.4
64-bit

```

You can also submit a job to LSF using `bsub` as follows:

```console
# make a script
LSF_DOCKER_VOLUMES='/storage1/fs1/workshops/Active/BIO4220:/storage1/fs1/workshops/Active/BIO4220' bsub -Is -G compute-workshop -q workshop-interactive -a 'docker(mlandis/biol4220:latest)' /bin/bash
```

Lastly, you will make a directory to store your work in the Storage directory for the class.

```console
$ cd /storage1/fs1/workshops/Active/BIO4220
$ mkdir -p users/michael.landis
$ cd users/michael.landis
$ git clone git@github.com:WUSTL-Biol4220/lab-17-mlandis.git
```

Cluster jobs will be able to write to the Storage directory. When the job is complete, you will transfer files from Storage into your home directory (`${HOME}`). 

---

## Dataset

We'll be looking at several genomic datasets for *E. coli*, a bacterial species relevant to human health, agriculture, and science. The *E. coli* genome is relatively small at approx. 4.6 Mbp in length, making it easy to work with. This lab will focus on several datasets already located in the shared Storage directory:

```console
$ cd /storage1/fs1/workshops/Active/BIO4220/dataset/ecoli
$ cat README.md
# E. coli sequences
accession       type          tech       notes         link
U00096          reference                               https://www.ncbi.nlm.nih.gov/nuccore/U00096.3
SRR11874161_1   short_reads   Illumina   paired_end_1   https://www.ncbi.nlm.nih.gov/sra/SRR11874161
SRR11874161_2   short_reads   Illumina   paired_end_2   https://www.ncbi.nlm.nih.gov/sra/SRR11874161
SRR8494908      long_reads    PacBio                    https://www.ncbi.nlm.nih.gov/sra/SRR8494908
```

There are four main files. 
These are the paired reads. The files ending with `_1.fastq` and `_2.fastq` represent a set of paired reads. The files encode information in groups of four lines. The first line is the sequence name, the second line contains the sequence data (base calls: A, C, G, T, and N), the third line contains a separator (+), and the fourth line reports quality scores.

```console
$ head -n4 SRR11874161_1.fastq
@SRR11874161.1 K00150:233:HL5YTBBXX:8:1227:17472:12603 length=150
AACGCTGCGCTGATTTGCCGTGGCGAGAAAATGTCGATCGCCATTATGGCCGGCGTGTTAGAAGCGCGTGGTCACAACGTTACCGTTATCGATCCGGTCGAAAAACTACTGGCAGTGGGGCATTACCTCGAATCTACCGTCGATATTGCT
+SRR11874161.1 K00150:233:HL5YTBBXX:8:1227:17472:12603 length=150
-AAAAF7FFJJ7JJJ<AF<F<JFJ7FJJFJJJFJJJJFAJJJ77JJFJJJA<A<A7AJFJJAJFJ<JJFAJJ<JFFJJJFFFJJJJF-F7<-7<JJJJJJF-AJJJJF7FJJJJJAFJJJJ)FAAJAJJJJAF77AFJJAJ<)-<7AJJA
```

How large is are the fastq files? List the file using a human-readable output (`-h`)

```console
$ ls -lh SRR11874161_1.fastq
-rw-------. 1 michael.landis storage-workshops-bio4220-rw 613M Oct 16 21:42 SRR11874161_1.fastq
```
which shows the files is 613 gigabytes in size (about as large as 1-2 full length movies encoded in high definition).

How many sequences do the two paired-end fastq files contain?

```console
$ cat SRR11874161_1.fastq SRR11874161_2.fastq | grep @SRR11874161 | wc -l
2899202
```

Nearly 2.9 million short reads.

---

## De novo genome assembly with short read data




Let's create some temporary variable to help locate filesystem objects:
```console
$ ECOLI_DIR="/storage1/fs1/workshops/Active/BIO4220/dataset/ecoli"
$ PROJ_DIR="/storage1/fs1/workshops/Active/BIO4220/users/michael.landis/lab-17-mlandis"
$ echo $ECOLI_DIR
$ echo $PROJ_DIR
```

We'll do the work from within our lab directory:
```console
$ cd $PROJ_DIR
```



### Quality control

We'll use the program `fastqc` to characterize the quality of the sequencing reads. For example, we can decide how aggressively to trim depending on the average quality scores at the beginning and ends of reads.

```console
$ mkdir fastqc_raw
```

To see the options for `fastqc`, run:

```console
$ fastqc --help
```

```console
$ fastqc -t 2 ${ECOLI_DIR}/SRR11874161_1.fastq ${ECOLI_DIR}/SRR11874161_2.fastq -o fastqc_raw
Started analysis of SRR11874161_1.fastq
Started analysis of SRR11874161_2.fastq
Approx 5% complete for SRR11874161_1.fastq
Approx 5% complete for SRR11874161_2.fastq
Approx 10% complete for SRR11874161_1.fastq
Approx 10% complete for SRR11874161_2.fastq

[ ... more text ... ]

Approx 90% complete for SRR11874161_1.fastq
Approx 90% complete for SRR11874161_2.fastq
Approx 95% complete for SRR11874161_1.fastq
Approx 95% complete for SRR11874161_2.fastq
Analysis complete for SRR11874161_1.fastq
Analysis complete for SRR11874161_2.fastq
```

Now unzip the results and inspect the data table:

```console
$ unzip fastqc_raw/SRR11874161_1_fastqc.zip
$ cd SRR11874161_1_fastqc
$ less SRR11874161_1_fastqc/fastqc_data.txt
```

Now look for bad things. For example, quality score by position relative to read length, 1 to 150bp.

Trim if quality drops at ends

What is a tile?


### Trimming

We'll use the program `fastp` to trim our reads. This will remove low quality bases and adapters from each read. Different sequencing technologies use distinctive adapter patterns that are easily identified. Some programs require that you specify what sequencing technology was used to determine what to trim. `fastp` has the option to detect it automatically.

```console
$ cd $PROJ_DIR
$ mkdir fastp
$ cd fastp
```

```console
$ fastp --in1 ${ECOLI_DIR}/SRR11874161_1.fastq --in2 ${ECOLI_DIR}/SRR11874161_2.fastq --out1 SRR11874161_trim_1.fastq --out2 SRR11874161_trim_2.fastq > fastp.log
$ cat fastp.log
```

<!--
```
fastp --in1 data/reads.1.fastq.gz --in2 data/reads.2.fastq.gz \
      --out1 trimmed/reads.trimmed.pe.1.fastq.gz \
      --out2 trimmed/reads.trimmed.pe.2.fastq.gz \
      --detect_adapter_for_pe \
      --length_required 100 \
      --qualified_quality_phred 30 \
      --average_qual 20 \
      --cut_right \
      --cut_mean_quality 25 \
      --thread 2 \
      --html trimmed/trimming.report.html \
      --json trimmed/trimming.report.json
```
-->

You can check the quality of your new datasets after trimming, using the same technique as above, under *Quality Control*. This published dataset was already trimmed and filtered for quality, so we don't expect to see a large difference before and after trimming. 

```console
$ cd $PROJ_DIR
$ mkdir fastqc_trim
$ fastqc -t 2 fastp/SRR11874161_trim_1.fastq fastp/SRR11874161_trim_2.fastq -o fastqc_trim
```

### De novo contig assembly

In some cases, no suitable reference genome is available -- for example, if you want to generate the first genome for a rare plant species with no closely known relatives. 

We'll build groups of overlapping short reads, called *contigs*. However, we don't know exactly where contigs belong in the genome. The contigs can be assembled into *scaffolds* using paired reads to link contigs together in a particular order. Scaffolds can potentially identify which contigs are on the same versus different chromosomes.

We'll use two programs, *minia* and *spades*, to assemble contigs for the trimmed *E. coli* short read data.

*minia* is relatively simple and fast. It is ultra low-memory software that assembles short reads into contigs.  It does not create scaffolds. It also only uses sequence data, while disregarding sequence quality, information during assembly. 

You can learn more about *minia* from the manual ([link](https://github.com/GATB/minia/raw/master/doc/manual.pdf)) or by typing the following command:
```console
$ minia --help
```

To assemble contigs with *minia* using standard settings, type:

```console
$ mkdir minia
$ minia -in fastp/SRR11874161_trim_1.fastq -in fastp/SRR11874161_trim_2.fastq -kmer-size 41 -abundance-min 2 -out minia/minia.41 -nb-cores 2
```

*spades* has a richer set of features, allows for higher quality assemblies, but is generally slower than *minia*.

Learn more about *spades* by visiting the manual webpage ([link](https://ablab.github.io/spades/)) or by typing the following command:

```console
$ spades --help
```

To assemble contigs with *spades* under standard settings, type:

```console
$ mkdir spades
$ spades -o spades -1 fastp/SRR11874161_trim_1.fastq -2 fastp/SRR11874161_trim_2.fastq -t 2 -m 8 --only-assembler
```


### Assembly evaluation


   Program: QUAST or Busco
   Description: Assess the quality of your assembly by checking N50, L50, genome coverage, and completeness of genes. This step helps you determine how well the assembly has performed.


```console
$ quast.py -o quast_minia minia/minia.41.contigs.fa
```

```console
$ quast.py -o quast_spades spades/scaffolds.fasta
```


---

## Running tasks through a non-interactive job


```console
#!/bin/bash

ECOLI_DIR="/storage1/fs1/workshops/Active/BIO4220/dataset/ecoli"
PROJ_DIR="/storage1/fs1/workshops/Active/BIO4220/users/michael.landis/lab-17-mlandis"

PWD=$(pwd)
cd $PROJ_DIR

echo "fastqc: pre-trim quality control"
mkdir fastqc_raw
fastqc -t 2 ${ECOLI_DIR}/SRR11874161_1.fastq ${ECOLI_DIR}/SRR11874161_2.fastq -o fastqc_raw

echo "fastp: trim reads"
mkdir fastp
cd fastp
fastp --in1 ${ECOLI_DIR}/SRR11874161_1.fastq --in2 ${ECOLI_DIR}/SRR11874161_2.fastq --out1 SRR11874161_trim_1.fastq --out2 SRR11874161_trim_2.fastq > fastp.log
cd ..

echo "fastqc: post-trim quality control"
mkdir fastqc_trim
fastqc -t 2 fastp/SRR11874161_trim_1.fastq fastp/SRR11874161_trim_2.fastq -o fastqc_trim

echo "minia: contig assembly"
mkdir minia
minia -in fastp/SRR11874161_trim_1.fastq -in fastp/SRR11874161_trim_2.fastq -kmer-size 41 -abundance-min 2 -out minia/minia.41 -nb-cores 2

echo "spades: contig assembly"
mkdir spades
spades -o spades -1 fastp/SRR11874161_trim_1.fastq -2 fastp/SRR11874161_trim_2.fastq -t 2 -m 8 --only-assembler

echo "quast: minia contig assembly quality"
quast.py -o quast_minia minia/minia.41.contigs.fa

echo "quast: spades contig assembly quality"
quast.py -o quast_spades spades/scaffolds.fasta

echo "...done!"
cd $PWD
```

Next make a script to submit the job to a non-interactive queue:

```console
#!/bin/bash
bsub -G compute-workshop \
-cwd /storage1/fs1/workshops/Active/BIO4220/users/michael.landis/lab-17-mlandis/ \
-o my_job.stdout.txt \
-J lab17 \
-q workshop \
-n 4 -M 4GB -R "rusage [mem=4GB] span[hosts=1]" \
-a 'docker(mlandis/biol4220:2024-v1)' /bin/bash /storage1/fs1/workshops/Active/BIO4220/users/michael.landis/lab-17-mlandis/my_job.sh
```

Update execute permissions and run the submission script:
```
$ chmod +x bsub_job.sh
$ ./bsub_job.sh
```

Confirm the job is running:
```
$ bjobs
JOBID   USER    STAT  QUEUE      FROM_HOST   EXEC_HOST   JOB_NAME   SUBMIT_TIME
790125  michael RUN   workshop   compute1-ex 4*compute1- lab17      Oct 21 01:15
```

You can monitor progress by looking at the end of the stdout log:
```console
$ tail my_job.stdout.txt
  0:00:41.937    40M / 1G    INFO   UnbranchingPathExtractor (debruijn_graph_constructor: 355)   Extracting unbranching paths
  0:00:48.899   108M / 1G    INFO   UnbranchingPathExtractor (debruijn_graph_constructor: 374)   Extracting unbranching paths finished. 1019759 sequences extracted
  0:00:52.523   108M / 1G    INFO   UnbranchingPathExtractor (debruijn_graph_constructor: 310)   Collecting perfect loops
  0:00:53.845   108M / 1G    INFO   UnbranchingPathExtractor (debruijn_graph_constructor: 343)   Collecting perfect loops finished. 0 loops collected
  0:00:54.745   364M / 1G    INFO    General                 (stage.cpp                 : 101)   PROCEDURE == Filling coverage indices (PHM)
  0:00:54.745   364M / 1G    INFO   K-mer Index Building     (kmer_index_builder.hpp    : 301)   Building kmer index
  0:00:54.745   364M / 1G    INFO   K-mer Index Building     (kmer_index_builder.hpp    : 314)   Building perfect hash indices
  0:00:56.506   372M / 1G    INFO   K-mer Index Building     (kmer_index_builder.hpp    : 336)   Index built. Total 10256448 bytes occupied (3.70997 bits per kmer).
  0:00:56.524   460M / 1G    INFO    General                 (construction.cpp          : 388)   Collecting k-mer coverage information from reads, this takes a while.
  0:01:18.325   460M / 1G    INFO    General                 (construction.cpp          : 508)   Filling coverage and flanking coverage from PHM
```

Either the job completes or it encounter an error. In either case, reviewing the stdout log will help guide your next steps.

---

## Exercises

Go through all the steps through an interactive session. Write a bash script called `job.sh` that will submit to process all tasks using a non-interactive session. Make sure the job produces a file named `job.log` for you to use for debugging.

Design the script so user arguments can modify these important analysis parameters:
```
```

What do you notice about quality when you run X?

What do you notice about quality when you run Y?

---

Clone the Lab 17 repo to the cluster. Commit and push the `job.sh` and `job.log`, and `history > history.txt` to the cloned repo to complete the assignment.




