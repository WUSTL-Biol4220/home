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

This document provides the technical requirements for how each step is expected to operate. In the process of completing the lab exercises, we will learn how to use various programs and techniques to achieve these goals. Whenever possible, I'll make a point to emphasize how lab exercises will help you design scripts and code for these steps.

Each step of the pipeline must run as an independent script or program. As such, each pipeline program will have its own functionality, and its own arguments, options, and expected output. At the same time, the program for each pipeline step may be required to produce output or accept input that is compatible with other pipeline steps. For example, the sequence aligner for Step 3 will accept the downloaded fasta-formatted sequences of Step 2 as input.

Students will be welcome to make richer pipelines, explore whatever they want. All students will have to add at least two new custom features. **Feature ideas must be approved by the instructor (date TBD).** 

Elements of the pipeline project design were inspired by [https://github.com/roblanf/sarscov2phylo](https://github.com/roblanf/sarscov2phylo).

... more to come.
