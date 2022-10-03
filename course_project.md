# Course project

## Overview

Students will build a bioinformatics pipeline to analyze biological data:

- **Option 1** is a molecular phylogenetics pipeline that downloads, aligns, and analyzes sequence data in a phylogenetic context ([link](assets/course_project/mol_phylo_project.md)).
- **Option 2** is a custom pipeline on a research topic of your choosing. These pipelines, however, must minimally involve steps for (1) data collection, (2) data formatting, (3) data analysis, and (4) output generation.

All pipeline projects require instructor approval (see below).

Pipelines will be composed of a number of intermediate scripted steps. For example, the molecular phylogenetics pipeline is built from 10 steps (8 standard, 2 custom). Pipeline steps will extend techniques that we explored in various course lab assignments, although students are free to incorporate resources and ideas learned outside of the course into their pipeline design.

Each step of the pipeline must run as an independent script or program. As such, each pipeline program will have its own functionality, and its own input, arguments, options, and output. At the same time, the script for any pipeline may need to produce output or accept input that is compatible with other pipeline step. With the Option 1 pipeline, for example, sequence alignment in Step 3 accepts the downloaded sequences of Step 2 as input.

## Project submission
Students will submit their pipeline projects using a GitHub repository. Create your repository using this GitHub Classroom link: . This will create a new repository for your user account the location e.g. https://github.com/WUSTL-Biol4220/biol4220-pipeline-project-mlandis that can be viewed by the course instructors.
 
Each repository will contain all the relevant files needed for a naive user to analyze a provided dataset, or a new dataset. Project repositories must contain the following files:
  - pipeline scripts
  - input dataset
  - analysis output
  - pipeline manual
  - analysis report
  - presentation slides
  
These materials are described in more detail below.

## Pipeline manual

Create short manual entries for any custom pipeline steps. These entries should define the usage and behavior the scripts in a comparable detail to the entries in the molecular phylogenetics pipeline specification ([link](assets/course_project/mol_phylo_project.md)).

## Analysis report

Write a 1-2 page report (12pt font, single-spaced) that summarizes your research findings. At a minimum, report should contain these components:

1. An overview of your pipeline, the pipeline features, and the analysis results.
2. A detailed description of the custom pipeline features that you added to the project, why they might be interesting or useful, and any challenges you encountered introducing those features.
3. A discussion of how your analysis output (results) differed depending on what settings/datasets you analyzed, and how those differences might influence what biological hypotheses are supported or rejected. For example, an analysis run under Settings-A might cause our methods to infer high proportions of nonsynonymous substitutions relative to synonymous substitutions, while Settings-B might cause our methods to infer roughly equal proportions of nonsynonymous and synonymous substitutions. Do Settings-A and Settings-B support conflicting biological scenarios? Why is it important to compare results using both settings? 

## Project presentation

At the end of the course, each student will deliver a short presentation of their work on the pipeline project to the class. Your presentation should share:
  - your custom pipeline features
  - an overview of your pipeline settings/datasets
  - an overview of your findings
  - aspects of the pipeline you would like to improve
  - any technical challenges you were proud to overcome
  - ideas for new pipeline features
  
**Plan to present for no more than 10 minutes.** After your presentation, the class will ask the presenter questions. We'll discuss more after everyone has presented, if there's time.

## Project approval

**All projects must get approval from the instructor by Oct 27 2021. Students will upload a short 1/2-page document to their project repository that briefly summarizes the scope and goals of their approved project.** For Option 1 projects, the instructor must approve of the 2+ new pipeline features you plan to add and what dataset you plan to analyze. For Option 2 projects, the instructor must approve the entire project, including the general pipeline that you plan to build and the dataset that you plan to analyze.

## Important dates

- Pipeline features and datasets approved by the instructor by **Oct 26 2022**
- Students will present their work to the class on **Dec 05 2022**
- Grading of project repositories will begin on **Dec 12 2022**
