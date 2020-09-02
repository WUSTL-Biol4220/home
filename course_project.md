# Course project

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

Students will be welcome to make richer pipelines, explore whatever they want. All students will have to add at least 2 features. **Feature ideas must be approved by the instructor.**

We will be borrowing some ideas from [https://github.com/roblanf/sarscov2phylo](https://github.com/roblanf/sarscov2phylo).

---

## 1. Parse user input for pipeline settings

--

## 2. Download sequences

Users should be able to provide a list of accession numbers. The script will then query NCBI to download those files.


--

## 3. Align sequences

Users should be able to align their sequences using Muscle.

Allow users to provide settings x, y, z.

Extra ideas: allow users to use different software with different arguments.

Input file: unaligned.fasta
Output file: alignment.fasta, report.txt

--

## 4. Characterize variation in molecular alignment

Python script to process alignment.

Read alignment as a matrix.

Report the GC-richness of each sequence
Report GC-richness of each site

Find all coding regions, identify all codons, report codon usage frequencies

Search for all sites with 2+ changes (parsimony-informative sites)

Input file: alignment.fasta
Output file: various report.txt


--

## 5. Estimate phylogenetic tree from alignment

Run a simple analysis, generate quick phylogeny plot

Input file: alignment.fasta
Output file: phylogeny.tre, figure

--

## 6. Test for signatures of positive selection

Run PAML under different settings

Reformat input for PAML
Reformat output from PAML so it's readable


Input file: alignment.fasta, phylogeny.tre
Output file: PAML results

--

## 7. Generate output files

Take all previous report files, then summarize it in a compact representation.

Have it update README.md so the results are visible in your github repo

Input: report.txt files
Output: README.md
