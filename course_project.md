# Course project (rough draft)

## Overview

Fall 2020 students will build a bioinformatics pipeline to analyze genomic data for the spread of SARS-CoV-19.

Student pipelines will incorporate seven major steps

1. Parse user input for pipeline settings
2. Download sequences
3. Align sequences
4. Characterize variation in molecular alignment
5. Estimate phylogenetic tree from alignment
6. Test for signatures of positive selection
7. Generate output files

This document will provide the technical requirements for how each step is expected to operate. In the process of completing the lab exercises, we will learn how to use various programs and techniques to achieve these goals. Whenever possible, I'll make a point to emphasize how lab exercises will help you design scripts and code for these steps.

Each step of the pipeline must run as an independent script or program. As such, each pipeline program will have its own arguments, options, and expected output. In general


Students will be welcome to make richer pipelines, explore whatever they want. All students will have to add at least 2 features. **Feature ideas must be approved by the instructor.**


Elements of the pipeline project design were inspired by [https://github.com/roblanf/sarscov2phylo](https://github.com/roblanf/sarscov2phylo).

---

## General specifications

Students will develop a pipeline that provides the following functionality

```
NAME
     biol4220-pipeline -- analyze data

SYNOPSIS
     ls [-ABCFGHLOPRSTUW@abcdefghiklmnopqrstuwx1%] [file ...]

DESCRIPTION
     The pipeline accepts a list of accession numbers as input, downloads those accessions into
     as fasta formatted files into a user directory (if they do not already exist), aligns those
     sequences under a variety of settings to create an alignment-set, generates descriptive
     statistics for the alignment-set, and computes the molecular phylogeny for the alignment-set.

     If one operand is given, it assumes that all. If multiple files are given, then the program
     will combine all fasta files.

     The following options are available:

     --align     align settings
     --paml      PAML settings
     --phylo     phylo settings
     --feature   extra feature settings
     --output
       
```

---

## 1. Parse user input for pipeline settings

Pipeline users will be able to provide input in two ways: by passing arguments and optional flags to the pipeline program, or by populating a tab-delimited control file.

### Optional flags


### Control file


### Useful labs



---

## 2. Download sequences

The `gather_sequences.sh` file will accept one file as input. That input file will contain a list of GenBank accession numbers, one per row, where each accession corresponds to a target sequence. The script will then download all available sequences into the `sequences` subdirectory, and append any issues to the file `warnings.log`.

Input file example with four accessions
```
A12345678
H32183282
B32701283
G63645551
```

The script will:

1. Identify whether fasta-formatted accession already exists in the `sequences` subdirectory. For example, for accession `A12345678` the script will see whether `sequences/seq_A12345678.fasta` exists.
     a. If the accession *does* exist, the script will further validate that the file contains two lines: line 1 contains the fasta description, e.g. `>sample_1|A12345678`; line 2 contains the sequence 
data, e.g. `ACGTACGTACT`.
     b. If the accession exists but is *invalid*, delete the accession from `sequences` and mark it to be downloaded. Record deleted files in `warnings.log`.

2. For each missing accession -- either because it was not downloaded or because it was deleted for being invalid -- download that accession from GenBank. 
     a. Download and rename each GenBank accession as a fasta file. For example, accession `A12345678` can be downlaoded from GenBank using the command `wget XXX/A12345678`, and saved as `sequences/seq_A12345678.fasta`.
     b. Save all processed
     b. Accessions that do not exist on GenBank will fail to download; report to `warnings.log` which files failed to download


### Useful labs



---

## 3. Align sequences

Step 3 of the pipeline will retrieve and align the target accessions identified in in `./sequences` marked as valid from Step 2. Minimally, the pipeline should align the software using [Muscle] and [MAFFT].

#### Muscle

```
Basic usage

    muscle -in <inputfile> -out <outputfile>

Common options (for a complete list please see the User Guide):

    -in <inputfile>    Input file in FASTA format (default stdin)
    -out <outputfile>  Output alignment in FASTA format (default stdout)
    -diags             Find diagonals (faster for similar sequences)
    -maxiters <n>      Maximum number of iterations (integer, default 16)
    -maxhours <h>      Maximum time to iterate in hours (default no limit)
    -html              Write output in HTML format (default FASTA)
    -msf               Write output in GCG MSF format (default FASTA)
    -clw               Write output in CLUSTALW format (default FASTA)
    -clwstrict         As -clw, with 'CLUSTAL W (1.81)' header
    -log[a] <logfile>  Log to file (append if -loga, overwrite if -log)
    -quiet             Do not write progress messages to stderr
    -version           Display version information and exit
```

#### MAFFT

```
------------------------------------------------------------------------------
  MAFFT v7.453 (2019/Nov/8)
  https://mafft.cbrc.jp/alignment/software/
  MBE 30:772-780 (2013), NAR 30:3059-3066 (2002)
------------------------------------------------------------------------------
High speed:
  % mafft in > out
  % mafft --retree 1 in > out (fast)

High accuracy (for <~200 sequences x <~2,000 aa/nt):
  % mafft --maxiterate 1000 --localpair  in > out (% linsi in > out is also ok)
  % mafft --maxiterate 1000 --genafpair  in > out (% einsi in > out)
  % mafft --maxiterate 1000 --globalpair in > out (% ginsi in > out)

If unsure which option to use:
  % mafft --auto in > out

--op # :         Gap opening penalty, default: 1.53
--ep # :         Offset (works like gap extension penalty), default: 0.0
--maxiterate # : Maximum number of iterative refinement, default: 0
--clustalout :   Output: clustal format, default: fasta
--reorder :      Outorder: aligned, default: input order
--quiet :        Do not report progress
--thread # :     Number of threads (if unsure, --thread -1)
--dash :         Add structural information (Rozewicki et al, submitted)
```


Input file: unaligned.fasta
Output file: alignment.fasta, report.txt


### Useful labs


---

## 4. Characterize variation in molecular alignment

Python script to process alignment.

Read alignment as a matrix.

Report the GC-richness of each sequence
Report GC-richness of each site

Find all coding regions, identify all codons, report codon usage frequencies

Search for all sites with 2+ changes (parsimony-informative sites)

Input file(s)
* sequences.fasta

Output file(s)
* align_mafft.settings_XXXXXX.fasta
* align.muscle.settings_XXXXXX.fasta
* align_mafft.settings_XXXXXX.txt
* align_muscle.settings_XXXXXX.txt
* align.warnings.log


---

## 5. Estimate phylogenetic tree from alignment

Run a simple analysis, generate quick phylogeny plot

Input file: alignment.fasta
Output file: phylogeny.tre, figure

---

## 6. Test for signatures of positive selection

Run PAML under different settings

Reformat input for PAML
Reformat output from PAML so it's readable


Input file: alignment.fasta, phylogeny.tre
Output file: PAML results

---

## 7. Generate output files

Take all previous report files, then summarize it in a compact representation.

Have it update README.md so the results are visible in your github repo

Input: report.txt files
Output: README.md
