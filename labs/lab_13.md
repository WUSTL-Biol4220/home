# Lab 12

*Lab 12 GitHub Classroom link:* https://classroom.github.com/a/Eku_G42u

In this lab, we'll learn how assemble genomes using different software and techniques

1. Genome assembly with short read data against reference
2. De novo genome assembly with short read data
3. De novo genome assembly with long read data

This lab is written to be performed through RIS WUSTL, our university's cluster. Review Lab 11 for a refresher on how to use RIS WUSTL.


---

## Configure your RIS profile

Add this line to the end of `~/.bash_profile`

```console
export STORAGE="/storage1/fs1/workshops/Active/BIO4220"
alias bsub-is="LSF_DOCKER_VOLUMES='${STORAGE}:${STORAGE}' bsub -Is -G compute-workshop -q workshop-interactive -a 'docker(ubuntu)' /bin/bash"
```

Add some new directories for programs to your path:
```console
export PATH="/storage1/fs1/workshops/Active/BIO4220/apps/sratoolkit/bin:$PATH"
```

Now you can open an interactive job with RIS by typing `bsub-is`. 


## Dataset

We'll be using these fastq files
These are the paired reads. The files ending with `_1.fastq` and `_2.fastq` represent a set of paired reads. The files encode information in groups of four lines. The first line is the sequence name, the second line contains the sequence data (base calls: A, C, G, T, and N), the third line contains a separator (+), and the fourth line reports quality scores.

```console
[michael.landis@compute1-client-1 arabiopsis]$ head -n4 SRR3156163_1.fastq
@1
TTTGCTTGTNNNNNNNNNNNNNTCATCATGAANNNNNNNNNNNNNNNNNNGTCAGATACAANNNNNNNNNNNNNNTTGTGGAAGCAGGAGATGTGGNNGT
+1
<<<@@????###########################################################################################
[michael.landis@compute1-client-1 arabiopsis]$ head -n4 SRR3156163_2.fastq
@1
NCNTNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNAACTTAGGAANNNNNNNNNNNNNNNNNCAATCTCCNNNNNNNNNNN
+1
####################################################################################################
```

How large is are the fastq files? List the file using a human-readable output (`-h`)

```console
[michael.landis@compute1-client-1 arabiopsis]$ ls -lh SRR3156163_1.fastq
-rw-------+ 1 michael.landis storage-workshops-bio4220-rw 11G Oct  3 16:10 SRR3156163_1.fastq
```
which shows the files is 11 gigabytes in size (about as large as 5 full length movies encoded in high definition).

How many sequences does the fastq file contain?

```console
[michael.landis@compute1-client-1 arabiopsis]$ wc -l SRR3156163_1.fastq
205331104 SRR3156163_1.fastq
```

Word count reports 205 million lines, meaning 50 million reads! Double that, because the paired read file contains a matching set.


## SPAdes

```
spades.py -t 68 -o 400_1500_3000 --12 paired_end_2x100_ins_400_c_50.fastq --12 paired_end_2x100_ins_1500_c_20.fastq --12 paired_end_2x100_ins_3000_c_25.fastq
spades.py -t 68 -o 400_and_1500 --12 paired_end_2x100_ins_400_c_50.fastq --12 paired_end_2x100_ins_1500_c_20.fastq
spades.py -t 68 -o 400_only --12 paired_end_2x100_ins_400_c_50.fastq
```

## Genome assembly with short read data against reference genome


## De novo genome assembly with short read data


## De novo genome assembly with long read data

---

Clone the Lab 12 repo to the cluster, then commit and push `history > history.txt` to the cloned repo to complete the assignment.




