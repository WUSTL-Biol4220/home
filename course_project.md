# Course project

*GitHub Classroom link:* TBD

## Overview

Students will build a bioinformatics pipeline to analyze biological data:

- **Phylogenetics Pipeline** is a molecular phylogenetics pipeline that downloads, aligns, and analyzes sequence data in a phylogenetic context ([link](assets/course_project/mol_phylo_project.md)).
- **Custom Pipeline** is a custom pipeline on a research topic of your choosing. These pipelines, however, must minimally involve steps for (1) data collection, (2) data formatting, (3) data analysis, and (4) output generation.

All pipeline projects require instructor approval (see below).

Pipelines will be composed of a number of intermediate scripted steps. For example, the molecular phylogenetics pipeline is built from 10 steps (8 standard, 2 custom). Pipeline steps will extend techniques that we explored in various course lab assignments, although students are free to incorporate resources and ideas learned outside of the course into their pipeline design.

Each step of the pipeline must run as an independent script or program. As such, each pipeline program will have its own functionality, and its own input, arguments, options, and output. At the same time, the script for any pipeline may need to produce output or accept input that is compatible with other pipeline step. With the Option 1 pipeline, for example, sequence alignment in Step 3 accepts the downloaded sequences of Step 2 as input.

## Project submission
Students will submit their pipeline projects using a GitHub repository. Create your repository using this GitHub Classroom link (see top of page). This will create a new repository for your user account the location e.g. https://github.com/WUSTL-Biol4220/biol4220-pipeline-project-mlandis that can be viewed by the course instructors.
 
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

Write a 2 page report (12pt font, single-spaced) that summarizes your research findings. At a minimum, report should contain these sections:

1. **Summary**. Describes the overall purpose of your pipeline, the pipeline features, and the analysis results.
2. **Design**. This section describes in detail important decisions you made in the design of your pipeline.
3. **Analysis**. A discussion of how your analysis output (results) differed depending on what settings/datasets you analyzed, and how those differences might influence what biological hypotheses are supported or rejected.
4. **Future ideas**. An overview of how you might want to improve your pipeline or the quality of your analyses in the future.

The analysis report is not due until after the project presentation.

## Project presentation

At the end of the course, each student will deliver a short presentation of their work on the pipeline project to the class. Your presentation should share:
  - your custom pipeline features
  - an overview of your pipeline settings/datasets
  - an overview of your findings
  - aspects of the pipeline you would like to improve
  - any technical challenges you were proud to overcome
  - ideas for new pipeline features
  
**Plan to present for 15 minutes.** After your presentation, the class will ask the presenter questions. We'll discuss more after everyone has presented, if there's time.

## Project approval

Students will describe the scope and goals of their proposed project in a 1-page document. Upload the document to `docs/proposal_yourname_biol4220_F2024.pdf` in your pipeline project repository. This document should be online for meeting with the instructor for project approval. All projects **must get approval from the instructor by Oct 23 2024**. 

For Option 1 projects, the instructor must approve of the 2+ new pipeline features you plan to add and what dataset you plan to analyze.

For Option 2 projects, the instructor must approve the entire project, including the general pipeline that you plan to build and the dataset that you plan to analyze.


## Important dates

- Pipeline features and datasets approved by the instructor by **Oct 23 2024**.
- Students will present their work to the class on **Dec 02 2024** and **Dec 04 2024**.
- Grading of project repositories will begin on **Dec 09 2022**. All pipeline materials must be uploaded to your GitHub repository at this time.
