# Course project

## Overview

Practical Bioinformatics (Biol4220) students will build a bioinformatics pipeline to analyze biological data. There are two options for students to pursue:

- **Option 1.** a molecular phylogenetics pipeline *with two new features*
- **Option 2.** a custom pipeline *with instructor approval*

This document outlines the technical requirements for the molecular phylogenetics pipeline (Option  1): [link](assets/course_project/mol_phylo_project.md).

Custom pipeline projects (Option 2) let you explore a research topic of your choosing. These pipelines, however, must minimally involve steps for (1) data collection, (2) data formatting, (3) data analysis, and (4) output generation.

Pipelines will be composed of a number of intermediate scripted steps. For example, the molecular phylogenetics pipeline is built from 10 steps (8 standard, 2 custom). Pipeline steps will extend techniques that we explored in various course lab assignments, although students are free to incorporate resources and ideas learned outside of the course into their pipeline design.

Each step of the pipeline must run as an independent script or program. As such, each pipeline program will have its own functionality, and its own input, arguments, options, and output. At the same time, the script for any pipeline may need to produce output or accept input that is compatible with other pipeline steps (with the Option 1 pipeline, for example, sequence alignement in Step 3 will accept the downloaded sequences of Step 2 as input).

### Project submission
Students will submit their pipeline projects as GitHub repositories. Each repository will contain all the relevant files needed for a naive user to analyze a provided dataset, or a new dataset. Project repositories must contain the following files:
  - pipeline scripts
  - pipeline manual
  - input dataset
  - analysis output
  - analysis report
  - presentation slides
  
These materials are described in more detail below.

### Project presentation

At the end of the course, each student will deliver a short presentation of their work on the pipeline project to the class. Your presentation should share:
  - your custom pipeline features
  - an overview of your pipeline settings/datasets
  - an overview of your findings
  - aspects of the pipeline you would like to improve
  - any technical challenges you were proud to overcome
  - ideas for new pipeline features
  
Plan to present for at least 10 minutes. After your presentation, the class will discuss what was presented, and ask the presenter questions.

### Important dates

- Feature ideas must be approved by the instructor by **Wed, Oct 27, 2021**
- Students will present their work to the class on **Mon, Dec 06, 2021**
- Grading of project repositories will begin on **Mon, Dec 13, 2021**

---

### Pipeline manual

Create short manual entries for your two (or more) custom pipeline steps. These entries should define the usage and behavior the scripts in a comparable detail to the entries in this document (`course_project.md`).

---

### Analysis report

Write a 1-2 page report (12pt font, single-spaced) that summarizes your research findings. At a minimum, report should contain these components:

1. An overview of your pipeline, the pipeline features, and the analysis results.
2. A detailed description of the custom pipeline features that you added to the project, why they might be interesting or useful, and any challenges you encountered introducing those features.
3. A discussion of how your analysis output (results) differed depending on what settings/datasets you analyzed, and how those differences might influence what biological hypotheses are supported or rejected. For example, an analysis run under Settings-A might cause our methods to infer high proportions of nonsynonymous substitutions relative to synonymous substitutions, while Settings-B might cause our methods to infer roughly equal proportions of nonsynonymous and synonymous substitutions. Do Settings-A and Settings-B support conflicting biological scenarios? Why is it important to compare results using both settings? 



<!--


(*Elements of the pipeline project design were inspired by [https://github.com/roblanf/sarscov2phylo](https://github.com/roblanf/sarscov2phylo).*)

---

## SARS-CoV-2

In 2020, the common name "coronavirus" is synonymous with a specific virus lineage, more precisely known as as Severe Acute Respiratory Syndrome-related Coronavirus-2 (SARS-CoV-2). SARS-CoV-2 is the virus that causes the infectious disease known as COVID-19. The first SARS-CoV was identified in China in 2003, and remained largely contained within that geographical region. A great deal has been learned since then about the molecular basis for how SARS-related coronaviruses infect humans, along with the genomic structure and composition of coronavirus lineages.

This section gives a brief overview of SARS-related coronavirus biology, including the genome architecture of SARS-CoV-2, the apparent functions of different proteins in the genome, and a suggested dataset that could be used to analyze with the pipeline.

Coronaviruses (family [Coronaviridae](https://talk.ictvonline.org/ictv-reports/ictv_9th_report/positive-sense-rna-viruses-2011/w/posrna_viruses/222/coronaviridae)) are enveloped single-stranded RNA viruses. At roughly 30kb in length, coronavirus genomes are large (if not the largest) among RNA viruses. Coronaviridae includes two virus subfamilies, Coronavirinae and Torovirinae. Coronavirinae contains a subgroup called Orthocoronavirinae, which is further divided into the virus genera *Alphacoronavirus*, *Betacoronavirus* , *Deltacoronavirus* , and *Gammacoronavirus*. SARS-related coronaviruses belong to *Betacoronavirus*, which primarily infect mammals, and include SARS-CoV, MERS-CoV, and now SARS-CoV-2.

The genome structure for SARS-CoV-2 is shown in the image below. Figure from [Kim et al. (2020, Cell)](https://github.com/WUSTL-Biol4220/home/blob/master/assets/course_project/kim_et_al_2020_cell_sarscov2_architecture.pdf).

![](assets/course_project/sars_cov_2_genome.jpg)

Major features of the genome include
- Structural proteins (from exterior to interior)
  - S, the spike protein, facilitates the attachment of the virion to the cell, and the entry of the virion into the cell.
  - E, the envelope protein, is the smallest of the structural proteins, facilitates protein-protein interactions and protein-environment interactions, but appears to have varied and "enigmatic" roles
  - M, the membrane protein, mediates the formation of the envelope protein, integrates spike proteins into the envelope protein, and determines the general shape of the viral envelope.
  - N, the nucleocapsid protein, directly binds to the coronavirus RNA genome, encapsulating it.
- The open reading frame, ORF1ab, contains overlapping reading frames that encode the polyproteins PP1ab and PP1a. PPA1ab and PP1a themselves encode 16 nonstructural proteins (NSPs) when cleaved.
- Nonstructural proteins, nsp1 through nsp16, play various roles in replication, transcription, and host translation interference.

## Sequence data

Most SARS-CoV-2 sequences are deposited to GenBank as annotated genomes. Here are several datasets that you might decide to analyze.
- [US SARS-CoV-2 sequences](https://raw.githubusercontent.com/WUSTL-Biol4220/home/master/assets/course_project/accessions_USA.txt) contains accessions for a set of viruses sampled in November, across the United States. Every state is represented once, except for Delaware (DE) and North Dakota (ND). Washington, DC, (DC) and Puerto Rico (PR) were included. This dataset has relatively little molecular variation, but genes are annotated in a manner that's easy to work with.
- [Global SARS-CoV-2 sequences](https://raw.githubusercontent.com/WUSTL-Biol4220/home/master/assets/course_project/accessions_global.txt) contains accessions for virus sequences obtained from roughly fifty countries, worldwide. For each country, the most recently available sequence was used; for most countries, the newest sequence was obtained <30 days ago, while for others the last sequence deposited on GenBank was in Spring 2020. Like the US dataset, the global dataset has relatively low amounts of molecular variation.
- [Orthocoronavirinae](https://raw.githubusercontent.com/WUSTL-Biol4220/home/master/assets/course_project/accessions_Orthocoronavirinae.txt) is a curated dataset hosted by GenBank [here](https://www.ncbi.nlm.nih.gov/genomes/GenomesGroup.cgi?taxid=2501931). Genes for these genomes are annotated in a useful manner that will allow you to compare, for example, the structural proteins (S, E, N, M). Not all coronaviruses have the same set of nonstructural proteins, so those will be more difficult to analyze for various reasons. This dataset also presents extremely high levels of molecular variation, as RNA viruses evolve very rapidly. Aligning the sequences in a meaningful way may be challenging, but you should try if you find this dataset appealing.
- [SARS-like bat and human coronaviruses](https://raw.githubusercontent.com/WUSTL-Biol4220/home/master/assets/course_project/accessions_bat_sarslike.txt) contains over 67 coronavirus sequences sampled from bat and human populations, mostly referenced from [Wells et al. (2020)](wells_et_al_2020_bioRxiv.pdf). These genomes include one SARS-CoV sequence (NC_004718), four SARS-CoV-2 sequences (MW315209, MW320728, MW326508, MW327510), with all remaining sequences originating in bats. These genomes do not share a common naming convention for genes, making it fairly difficult to extract the genes from the dataset. To simplify your analyses, you may use alignments for the four structural proteins, shared here: [S](https://raw.githubusercontent.com/WUSTL-Biol4220/home/master/assets/course_project/CoV_sarslike_bat/S.fasta), [E](https://raw.githubusercontent.com/WUSTL-Biol4220/home/master/assets/course_project/CoV_sarslike_bat/E.fasta), [N](https://raw.githubusercontent.com/WUSTL-Biol4220/home/master/assets/course_project/CoV_sarslike_bat/N.fasta), [M](https://raw.githubusercontent.com/WUSTL-Biol4220/home/master/assets/course_project/CoV_sarslike_bat/M.fasta).

The following command will download the genome for `MW264435` as a nucleotide-encoded fasta file, with each protein-coding gene stored as a different fasta entry:
```
$ efetch -db nuccore -format fasta_cds_na -id MW264435
>lcl|MW290939.1_cds_QPI19188.1_1 [gene=ORF1ab] [protein=ORF1ab polyprotein] [partial=3'] [exception=ribosomal slippage] [protein_id=QPI19188.1] [location=join(227..13429,13429..>21122)] [gbkey=CDS]
ATGGAGAGCCTTGTCCCTGGTTTCAACGAGAAAACACACGTCCAACTCAGTTTGCCTGTTTTACAGGTTC
GCGACGTGCTCGTACGTGGCTTTGGAGACTCCGTGGAGGAGGTCTTATCAGAGGCACGTCAACATCTTAA
AGATGGCACTTGTGGCTTAGTAGAAGTTGAAAAAGGCGTTTTGCCTCAACTTGAACAGCCCTATGTGTTC
... more sequence data ...
$ efetch -db nuccore -format fasta_cds_na -id MW264435 | grep ">"
>lcl|MW264435.1_cds_QPD96888.1_1 [gene=ORF1ab] [protein=ORF1ab polyprotein] [exception=ribosomal slippage] [protein_id=QPD96888.1] [location=join(250..13452,13452..21539)] [gbkey=CDS]
>lcl|MW264435.1_cds_QPD96889.1_2 [gene=ORF1ab] [protein=ORF1a polyprotein] [protein_id=QPD96889.1] [location=250..13467] [gbkey=CDS]
>lcl|MW264435.1_cds_QPD96890.1_3 [gene=S] [protein=surface glycoprotein] [protein_id=QPD96890.1] [location=21547..25368] [gbkey=CDS]
>lcl|MW264435.1_cds_QPD96891.1_4 [gene=ORF3a] [protein=ORF3a protein] [protein_id=QPD96891.1] [location=25377..26204] [gbkey=CDS]
>lcl|MW264435.1_cds_QPD96892.1_5 [gene=E] [protein=envelope protein] [protein_id=QPD96892.1] [location=26229..26456] [gbkey=CDS]
>lcl|MW264435.1_cds_QPD96893.1_6 [gene=M] [protein=membrane glycoprotein] [protein_id=QPD96893.1] [location=26507..27175] [gbkey=CDS]
>lcl|MW264435.1_cds_QPD96894.1_7 [gene=ORF6] [protein=ORF6 protein] [protein_id=QPD96894.1] [location=27186..27371] [gbkey=CDS]
>lcl|MW264435.1_cds_QPD96895.1_8 [gene=ORF7a] [protein=ORF7a protein] [protein_id=QPD96895.1] [location=27378..27743] [gbkey=CDS]
>lcl|MW264435.1_cds_QPD96896.1_9 [gene=ORF7b] [protein=ORF7b] [protein_id=QPD96896.1] [location=27740..27871] [gbkey=CDS]
>lcl|MW264435.1_cds_QPD96897.1_10 [gene=ORF8] [protein=truncated ORF8 protein] [protein_id=QPD96897.1] [location=27878..27958] [gbkey=CDS]
>lcl|MW264435.1_cds_QPD96898.1_11 [gene=N] [protein=nucleocapsid phosphoprotein] [protein_id=QPD96898.1] [location=28258..29517] [gbkey=CDS]
>lcl|MW264435.1_cds_QPD96899.1_12 [gene=ORF10] [protein=ORF10 protein] [protein_id=QPD96899.1] [location=29542..29658] [gbkey=CDS]
```

For genewise comparative analyses, you will likely need to partition each resulting fasta file into separate gene-specific fasta files. Here is an [example script](https://raw.githubusercontent.com/WUSTL-Biol4220/home/master/assets/course_project/example_get_seq.sh) that may be helpful.

If you are unsure of what datasets to analyze, I would suggest focusing on structural genes (S, E, M, N) for the US accessions (above). Of coursse, you're free to analyze any SARS-CoV-2 genetic dataset that you wish. That dataset might focus on a single state, a different country, a global perspective, other coronaviruses, different time periods, or nonstructural genes. Search for more SARS-CoV-2 accessions with this [tool](https://www.ncbi.nlm.nih.gov/labs/virus/vssi/#/virus?SeqType_s=Nucleotide&VirusLineage_ss=SARS-CoV-2,%20taxid:2697049).

---
-->
