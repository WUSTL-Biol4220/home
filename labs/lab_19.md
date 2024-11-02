# Lab 19

*Lab 19 GitHub Classroom link:* TBD

In this lab, we'll learn how assemble a genome using an Illumina short read dataset. The main steps will be:

1. Configure RIS profile
2. Data preparation (quality control, trimming)
3. De novo short read assembly
4. Assembly statistics

This lab is written to be performed through WUSTL Research Infrastructure Services (RIS) cluster: [link](https://ris.wustl.edu/). Review Lab 11 for a refresher on how to use WUSTL RIS.

---

## Configuring your RIS profile

First, we will configure your RIS user account with some helper variables and aliases. These additions will alleviate the need to memorize or look up complex commands and/or file paths.

To begin, ssh into an RIS login node, for example:

```console
$ ssh michael.landis@compute1-client-1.ris.wustl.edu
```

Once logged in, add these line to the end of `~/.bash_profile`

```console
export STORAGE="/storage1/fs1/workshops/Active/BIO4220"
alias bsub-is="LSF_DOCKER_VOLUMES='${STORAGE}:${STORAGE}' bsub -Is -G compute-workshop -q workshop-interactive -a 'docker(ubuntu)' /bin/bash"
alias bsub-is-4220="LSF_DOCKER_VOLUMES='/storage1/fs1/workshops/Active/BIO4220:/storage1/fs1/workshops/Active/BIO4220' bsub -Is -G compute-workshop -q workshop-interactive -a 'docker(mlandis/biol4220:latest)' /bin/bash"
```

The line with `export STORAGE` creates a variable to shared storage directory for our class. The lines that begin with `alias` create names that behave like commands for starting different kinds of interactive cluster jobs.

To make use of the new additions to your profile, you can either log off and log back in, or you can use the following command:

```console
$ source ~/.bash_profile
```

Now you can use the new `STORAGE` variable:

```console
$ cd $STORAGE
$ pwd
/storage1/fs1/workshops/Active/BIO4220
```

You may now also run an interactive job with RIS by typing `bsub-is-4220`. Note, it takes some time to load pull the Docker image and make a container for the job.

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

Let's create temporary variables to help locate filesystem objects for this lab (you could add these to your `.bash_profile` using `export` if you want):
```console
$ ECOLI_DIR="$STORAGE/dataset/ecoli"
$ PROJ_DIR="$STORAGE/users/michael.landis/lab-19-mlandis"
$ echo $ECOLI_DIR
$ echo $PROJ_DIR
```

Lastly, you will make a directory to store your work in the Storage directory for the class.

```console
$ mkdir -p users/michael.landis
$ cd users/michael.landis
$ git clone git@github.com:WUSTL-Biol4220/lab-19-mlandis.git
```

Cluster jobs will be able to write to the Storage directory. 

---

## Dataset

We'll be looking at several genomic datasets for *E. coli*, a bacterial species relevant to human health, agriculture, and science. The *E. coli* genome is relatively small at approx. 4.6 Mbp in length, making it easy to work with.

Genome sizes vary radically among species. Humans, for instance, have 3.2 Gb. Many viral genomes are only thousands of nucleotides in length, bacteria often have genomes that are millions of nucleotides long, while eukaryotes have genomes in the hundreds of billions of bases.

This lab will focus on several datasets already located in the shared Storage directory:

```console
$ cd $STORAGE/dataset/ecoli
$ cat README.md
# E. coli sequences
accession       type          tech       notes         link
U00096          reference                               https://www.ncbi.nlm.nih.gov/nuccore/U00096.3
SRR11874161_1   short_reads   Illumina   paired_end_1   https://www.ncbi.nlm.nih.gov/sra/SRR11874161
SRR11874161_2   short_reads   Illumina   paired_end_2   https://www.ncbi.nlm.nih.gov/sra/SRR11874161
SRR8494908      long_reads    PacBio                    https://www.ncbi.nlm.nih.gov/sra/SRR8494908
```

The Illumina sequences end with `_1.fastq` and `_2.fastq`, one for each in the paired reads. The files encode information in groups of four lines. The first line is the sequence name, the second line contains the sequence data (base calls: A, C, G, T, and N), the third line contains a separator (+), and the fourth line reports quality scores. You can learn more about the fastq format here: [link](https://en.wikipedia.org/wiki/FASTQ_format).

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

where `613M` means the file is 613 megabytes in size (about as large as 1-2 full length movies encoded in high definition).

How many sequences do the two paired-end fastq files contain?

```console
$ cat SRR11874161_1.fastq SRR11874161_2.fastq | grep @SRR11874161 | wc -l
2899202
```

... or, nearly 2.9 million short reads. That is about 1.5 reads per base pair in the genome. Assuming each read is 150bp in length and nothing is trimmed, we might expect a read depth of ~225x for each position in the *E. coli* genome. Normally a read depth as low as 20x is enough to have confidence in general features of the assembly, whereas 100x coverage is sought for analyses that depend on accurate base pair assignments for individual sites.


---

## De novo genome assembly with short read data

Let's get started the the assembly! We'll perform the work from within our lab directory:
```console
$ cd $PROJ_DIR
```

### Quality control

We'll use the program `fastqc` to characterize the quality of the sequencing reads. For example, we can decide how aggressively to trim depending on the average quality scores at the beginning and ends of reads.

To see the options for `fastqc`, run:

```console
$ fastqc --help
```

Let's store our quality control data in a subdirectory called `fastqc_raw`:


```console
$ mkdir -p fastqc_raw
$ fastqc -t 2 ${ECOLI_DIR}/SRR11874161_1.fastq \
              ${ECOLI_DIR}/SRR11874161_2.fastq \ 
              -o fastqc_raw
Started analysis of SRR11874161_1.fastq
Started analysis of SRR11874161_2.fastq
Approx 5% complete for SRR11874161_1.fastq
Approx 5% complete for SRR11874161_2.fastq

[ ... more text ... ]

Analysis complete for SRR11874161_1.fastq
Analysis complete for SRR11874161_2.fastq
```

Now unzip the results and inspect the data table:

```console
$ unzip fastqc_raw/SRR11874161_1_fastqc.zip
$ cd SRR11874161_1_fastqc
$ less SRR11874161_1_fastqc/fastqc_data.txt
```

For example, quality score by position relative to read length, 1 to 150bp. If the quality score indicated that the first and last 10bp of each read was of low quality, we could use that information to trim our reads more aggressively (next step). 



### Trimming

We'll use the program `fastp` to trim our reads. This will remove low quality bases and adapters from each read. Different sequencing technologies use distinctive adapter patterns that are easily identified. Some programs require that you specify what sequencing technology was used to determine what to trim. `fastp` has the option to detect it automatically.

Now we run `fastp`:

```console
$ cd $PROJ_DIR
$ mkdir fastp
$ fastp --in1 ${ECOLI_DIR}/SRR11874161_1.fastq \
        --in2 ${ECOLI_DIR}/SRR11874161_2.fastq \
        --out1 fastp/SRR11874161_trim_1.fastq \
        --out2 fastp/SRR11874161_trim_2.fastq
```

You can check the quality of your new datasets after trimming, using the same technique as above, under *Quality Control*. This published dataset was already trimmed and filtered for quality, so we don't expect to see a large difference before and after trimming. 

```console
$ mkdir fastqc_trim
$ fastqc -t 2 \
         fastp/SRR11874161_trim_1.fastq \
         fastp/SRR11874161_trim_2.fastq \
         -o fastqc_trim
$ # unzip and inspect as was done above, if interested
```

### Contig assembly

We'll build groups of overlapping short reads, called *contigs*. However, we don't know exactly where contigs belong in the genome. In some cases, these paired reads at the edges of these contigs can be used to order and link together contigs into *scaffolds*. We will focus on generating contigs, not scaffolds, for this lab.

<!--
In some cases, no suitable reference genome is available -- for example, if you want to generate the first genome for a rare plant species with no close relatives that have assembled genomes.
-->

We'll use two programs, *minia* and *spades*, to assemble contigs for the trimmed *E. coli* short read data.


#### minia

*minia* is relatively simple and fast. It is ultra low-memory software that assembles short reads into contigs. It does not create scaffolds. It also only uses sequence data, while disregarding sequence quality, information during assembly. 

You can learn more about *minia* from the manual ([link](https://github.com/GATB/minia/raw/master/doc/manual.pdf)) or by typing the following command:
```console
$ minia --help
```

To assemble contigs with *minia* using standard settings, type:

```console
$ mkdir minia
$ minia -in fastp/SRR11874161_trim_1.fastq \
        -in fastp/SRR11874161_trim_2.fastq \
        -kmer-size 55 \
        -abundance-min 2 \
        -out minia/minia.55 \
        -nb-cores 2 > minia/minia.55.log
```

Notice the option `-kmer-size` above was set to 55bp. This kmer length is used when constructing the de Bruijn graph used for assembly. Ultimately, a lower kmer size will mean it is easier to map short reads when assembling a contig, which will both increase read depth but also increase the number of poorly-matching mapped reads. Use lower kmer sizes with smaller low-coverage with few repetitive genomic regions. 

Conversely, a higher kmer size will lead to more accurate contigs with but possible with lower map depths levels. Use higher kmer sizes to help with larger high-coverage genomes that contain main repetitive regions in the genome.

Let's assemble additional datasets using kmers for 33bp and 77bp in length.

```console
$ minia -in fastp/SRR11874161_trim_1.fastq \
        -in fastp/SRR11874161_trim_2.fastq \
        -kmer-size 33 \
        -abundance-min 2 \
        -out minia/minia.33 \
        -nb-cores 2 > minia/minia.33.log
$ minia -in fastp/SRR11874161_trim_1.fastq \
        -in fastp/SRR11874161_trim_2.fastq \
        -kmer-size 77 \
        -abundance-min 2 \
        -out minia/minia.77 \
        -nb-cores 2 > minia/minia.77.log
```

Let's compare the results. How many contigs did each assembly produce? We can learn this by counting the number of sequence header records in the outputted fasta files:

```console
$ grep -n -c ">" minia/minia.*.contigs.fa
minia/minia.33.contigs.fa:1021
minia/minia.55.contigs.fa:537
minia/minia.77.contigs.fa:488
```

These numbers agree with each assembly log:
```console
$ grep "nb_contigs" minia/minia.*.log
minia/minia.33.log:        nb_contigs                               : 1021
minia/minia.55.log:        nb_contigs                               : 537
minia/minia.77.log:        nb_contigs                               : 488
```

The last 15 lines of each log file contains useful assembly statistics:
```console
$ tail -n15 minia/minia.77.log
    stats
        traversal                                : contig
        nb_solid_kmers                           : 4968565
        nb_contigs                               : 488
        nb_small_contigs_discarded               : 623
        nt_assembled                             : 4958907
        max_length                               : 154744
        graph simpification stats
            tips removed                             : 2298 + 8 + 0 + 3 + 0
            bulges removed                           : 76 + 3 + 1 + 0 + 0 + 0
            EC removed                               : 18 + 4 + 0 + 0 + 0
        assembly traversal stats
    time                                     : 38.237
        assembly                                 : 0.089
        graph construction                       : 38.148
```

Which kmer value produced the longest contig (`max_length`)? Which kmer value assembled the most nucleotides (`nt_assembled`)? How would you explain the patterns you see?

#### spades

*spades* has a richer set of features, allows for higher quality assemblies, but is generally slower than *minia*.

Learn more about *spades* by visiting the manual webpage ([link](https://ablab.github.io/spades/)) or by typing the following command:

```console
$ spades --help
```

To assemble contigs with *spades* under standard settings, type:

```console
$ mkdir spades
$ spades -o spades \
         -1 fastp/SRR11874161_trim_1.fastq \
         -2 fastp/SRR11874161_trim_2.fastq \
         -t 2 -m 8 --only-assembler
```

By default, *spades* will generate contigs using kmers of length 21, 33, 55, and 77bp.

```console
$ grep -nc ">" spades/K*/*contigs.fasta
spades/K21/simplified_contigs.fasta:2187
spades/K33/simplified_contigs.fasta:1003
spades/K55/simplified_contigs.fasta:526
spades/K77/final_contigs.fasta:195
```

Notice that this dataset yielded similar numbers of contigs for 33 and 55bp kmers when compared to *minia*, but the number of final contigs the 77bp kmer directory are fewer. The result from K77 is copied into the main directory for *spades*.

How many nucleotides are covered by the final assembled contigs?

```console
$ grep -c ">" spades/contigs.fasta
195
$ grep -v ">" spades/contigs.fasta | wc -c
5034383
```

### Assembly stats

Next, let's evaluate read depth across our contigs. To do this, we'll use *bowtie2* to create a genome index for the original *minia* asssembly made using 55bp kmers:

```console
$ mkdir -p bowtie
$ bowtie2-build ./minia/minia.55.contigs.fa ./bowtie/minia.55.contigs_index
```

Then we map our reads against the new index (this can take a little while):
```console
$ bowtie2 -x bowtie/minia.55.contigs_index \
             -1 fastp/SRR11874161_trim_1.fastq \
             -2 fastp/SRR11874161_trim_2.fastq \
             -S bowtie/minia.55.aligned_reads.sam
```

Now we can use *samtools* to generate a table of read depth across the contigs. First, we convert our human-readable sam file into a compact and sorted bam file:

```console
$ samtools view -bS bowtie/minia.55.aligned_reads.sam > bowtie/minia.55.aligned_reads.bam
$ samtools sort bowtie/minia.55.aligned_reads.bam -o bowtie/minia.55.aligned_reads_sorted.bam
```

Then we use *samtools* to generate one file with read depth per site and a second file with coverage statistics per contig:

```console
$ samtools depth bowtie/minia.55.aligned_reads_sorted.bam > bowtie/minia.55.depth.txt
$ samtools coverage bowtie/minia.55.aligned_reads_sorted.bam > 
bowtie/minia.55.coverage.txt
```

Compared to the *samtools* program, *assembly_stats* reports a simpler and more-concise set of assembly statistics:

```console
$ assembly_stats minia/minia.55.contigs.fa
```

You can visually inspect your assembly using the *samtools tview* command, after first creating a bam index file (*.bai*):

```console
$ samtools index minia.55.aligned_reads_sorted.bam
$ samtools tview minia.55.aligned_reads_sorted.bam
```

Press the `?` key to see options for using *samtools tview*:

<img src="https://github.com/WUSTL-Biol4220/home/blob/main/assets/lab_19/tview.png" width="550"/>

This lets you view your assembled reads!

---

## Running tasks through a non-interactive job


```console
#!/bin/bash

ECOLI_DIR="/storage1/fs1/workshops/Active/BIO4220/dataset/ecoli"
PROJ_DIR="/storage1/fs1/workshops/Active/BIO4220/users/michael.landis/lab-19-mlandis"

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

echo "...done!"
cd $PWD
```

Next make a script to submit the job to a non-interactive queue:

```console
#!/bin/bash
bsub -G compute-workshop \
-cwd /storage1/fs1/workshops/Active/BIO4220/users/michael.landis/lab-19-mlandis/ \
-o my_job.stdout.txt \
-J lab19 \
-q workshop \
-n 4 -M 4GB -R "rusage [mem=4GB] span[hosts=1]" \
-a 'docker(mlandis/biol4220:2024-v1)' /bin/bash /storage1/fs1/workshops/Active/BIO4220/users/michael.landis/lab-19-mlandis/my_job.sh
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
790125  michael RUN   workshop   compute1-ex 4*compute1- lab19      Oct 21 01:15
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

No exercises for Lab 19! Spend your extra time working on your course project.

---

Clone the Lab 19 repo to the cluster. Commit and push the `job.sh` and `job.log`, and `history > history.txt` to the cloned repo to complete the assignment.




