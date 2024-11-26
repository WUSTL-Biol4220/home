# Molecular phylogenetics pipeline (Option 1)

*Read more about the general pipeline project requirements [here](https://github.com/WUSTL-Biol4220/home/blob/main/course_project.md).*

## Pipeline script, `pipeline.sh`

Students will write a bioinformatics pipeline script that accepts a settings file name as an argument.

### Usage

`./pipeline.sh SETTINGS_FILE [JOB_DIR]`

### Behavior

The script `pipeline.sh` itself runs seven other pipeline steps, in the general order:

1. Parse settings
2. Gather sequences
3. Align sequences
4. Estimate phylogenetic tree from alignment
5. Characterize variation in molecular alignment
6. Test for signatures of positive selection
7. Generate output files

```
# pipeline schematic
# (order of steps)
                 
                  + → 6 ──+
                  |   ↓   ↓
 in → 1 → 2 → 3 → 4 → 7 → out
                  |       ↑
                  + → 5 ──+ 
```

Don't forget, each student must **add two or more custom features** to his/her pipeline. Where those steps will fit into the above schematic will depend on exactly what the features are.

All output is stored into the optional directory targetted by `JOB_DIR`. If no argument is provided for `JOB_DIR`, then the script outputs results into the directory `tmp`. The script creates the directory if it does not exist.


---

## 1. `parse_settings.sh`

This script will parse analysis settings from a setting file. Users will provide two arguments: (1) the file path to the pipeline settings file, and (2) the name of the pipeline step to parse.

### Usage

`./parse_settings.sh SETTINGS_FILE PIPELINE_STEP`

### Behavior

The pipeline settings file stores comma-separated values in the following format:
```
script,settings
get_seq.sh,accession=my_accessions.txt;sequence_dir=US_samples;overwrite=true;
make_align.sh,sequence_dir=US_samples;align_tool=mafft;align_tool_options='-gapopen 2';
make_phylo.sh,align_file=covid_align_mafft.fasta;phylo_tool=fasttree;phylo_tool_options='-gtr';
make_mol_stats.py,align_file=covid_align_mafft.fasta;
make_dnds.py,align_file=covid_align_mafft.fasta;phylo_file=covid_align_mafft_fasttree.tre;
make_results.py,sequence_dir=US_samples;
feature1.sh,setting1=my_feature1_settings.txt;parameter1=20;
feature2.py,setting2=my_feature2_settings.txt;parameter2=50;
```
The `script` column identifies a pipeline step by the script name. The `settings` column contains a list of `;`-delimited setting variables following the pattern `variable1=value1;variable2=value2;`.

For example, if we called `./parse_settings.sh settings.txt get_seq.sh` we should locate the row for the step labeled `get_seq.sh` then parse the settings string `accession=my_accessions.txt;overwrite=true;`. The `parse_settings.sh` script will then reformat the settings for a given pipeline step as-needed. Users may provide all or only some settings for any pipeline step. 

---

## 2. `get_seq.sh`

*(Relevant labs and lectures: 05, 06, 07)*

The `get_seq.sh` manages and downloads fasta-formatted accessions from GenBank. As input, the script accepts two arguments: (1) a list of accessions, and (2) a directory where the sequences are managed. The script will then check whether each accession has already been downloaded into the managed directory, download any missing sequences, and append any issues to the file `warnings.log`.

### Usage

`./get_seq ACCESSION_FILE SEQUENCE_DIR [OVERWRITE]`

### Behavior

The file `ACCESSION_FILE` will contain a list of accessions. Example format:
```
A12345678
H32183282
B32701283
G63645551
```

The script will:

1. Identify whether fasta-formatted accession already exists in the `SEQUENCE_DIR` subdirectory. For example, for accession `A12345678` the script will see whether `sequences/A12345678.fasta` exists.
     a. If the accession *does* exist, the script will further validate that the file contains two lines: line 1 contains the fasta description, e.g. `>sample_1|A12345678`; line 2 contains the sequence 
data, e.g. `ACGTACGTACT`.
     b. If the accession exists but is *invalid*, delete the accession from `SEQUENCE_DIR` and mark it to be downloaded. Record deleted files in the file `warnings.log`.
     c. If the optional `OVERWRITE` argument is provided and equals "true", then treat all sequences as missing accessions that will be overwritten.

2. For each missing accession -- either because it was not downloaded or because it was deleted for being invalid -- download that accession from GenBank. 
     a. Download and rename each GenBank accession as a fasta file. For example, accession `A12345678` fetched from GenBank using the `equery` and `efetch` commands, and saved as `A12345678.fasta`
     b. Invalid accessions that do not exist on GenBank will fail to download; report to `warnings.log` which files failed to download
     
---

## 3. `make_align.sh`

*(Relevant labs and lectures: 05, 06, 08)*

This script will align a set of fasta sequences located in a target directory.

### Usage

`./make_align SEQUENCE_DIR ALIGN_TOOL [ALIGN_TOOL_OPTIONS]`

### Behavior

The `make_align.sh` script will align the sequences in `SEQUENCE_DIR` using the method `ALIGN_TOOL` and the optional arguments defined by `ALIGN_TOOL_OPTIONS`.

The script will concatenate all fasta files in `SEQUENCE_DIR`, then take that concatenated sequence file as input for the alignment procedure. The script will then align the sequence file using a supported alignment tool (specified by `ALIGN_TOOL`), where supported tools must include Muscle, MAFFT, and PRANK. Students are welcome to add support for additional tools, but they will need to install that software on their virtual machine. The alignment procedure will use arguments/options passed in through `ALIGN_TOOL_OPTIONS`. Note that invalid input and/or invalid software options may cause the alignment software to fail. Script failures you encounter should be logged in `warnings.log`

In addition to supporting input and output arguments, other `ALIGN_TOOL_OPTIONS` to support are
- Muscle: gap open penalty (`-gapopen`)
- MAFFT: gap open penalty (`--op`) and gap extension penalty (`--ep`)
- PRANK: gap open rate (`-gaprate`) and gap extension probability (`-gapext`)

The script should write two files as output: (1) the output alignment file and (2) a log file that documents the alignment settings. If the `SEQUENCE_DIR` was `primates_cytb` and `ALIGN_TOOL` was MAFFT, then the output file should be saved as `primates_cytb.align_mafft.fasta` and `primates_cytb.align_mafft.log`.

The log file should report
- the name of the alignment file
- the command string used to align the sequences
- when the alignment was created (use output of `date`)
- the number of sequences and the number of sites in the aligned sequence
- (optional) the version of the alignment software
- (optional) list of the aligned accessions

---

## 4. `make_phylo.sh`

*(Relevant labs and lectures: 12)*

This script will estimate a phylogeny from a multiple sequence alignment.

### Usage

`./make_phylo ALIGN_FILE PHYLO_TOOL [PHYLO_TOOL_OPTIONS]`

### Behavior

The `make_phylo.sh` script will infer a phylogeny using the alignment stored in `ALIGN_FILE` using the software `PHYLO_TOOL` under the settings `PHYLO_TOOL_OPTIONS`. The script must support the phylogenetic inference methods: FastTree, IQ-Tree, and MPBoot. Students are welcome to include additional phylogenetic methods, but they will need to install that software on their virtual machine. The phylogenetic inference procedure will use arguments/options passed in through `PHYLO_TOOL_OPTIONS`. Note that invalid input and/or invalid software options may cause the phylogenetics software to fail. Script failures you encounter should be logged in `warnings.log`

In addition to supporting input and output arguments, other `PHYLO_TOOL_OPTIONS` to support are
- FastTree: use of a more complex model of nucleotide evolution (`-gtr`)
- IQ-Tree: use of a more complex model of nucleotide evolution (`-m GTR`) or a simpler model (`-m JC`)
- MPBoot: *no settings*

The script should write three files as output: (1) the output phylogenetic estimate stored as a Newick string, (2) a text representation of the phylogeny using NW Utilities, and (3) a log file that documents the phylogenetic inference settings. If the `ALIGN_FILE` was `primates_cytb.align_mafft.fasta` and `PHYLO_TOOL` was FastTree, then the output file should be saved as `primates_cytb.align_mafft.phylo_fasttree.tre`, `primates_cytb.align_mafft.phylo_fasttree.nw_display.txt`, and `primates_cytb.align_mafft.phylo_fasttree.log`.

The log file should report
- the name of the file containing the phylogenetic estimate, in Newick format
- the command string used to infer the phylogeny
- when the phylogeny was created (use output of `date`)
- (optional) the version of the phylogenetic software


---

## 5. `make_mol_stats.py`

*(Relevant labs and lectures: 16, 17)*

The `make_mol_stats.py` script generates a report of various summary statistics and transformations for a multiple sequence alignment.

### Usage

`./make_mol_stats.py ALIGN_FILE`

### Behavior

This Python script will perform several steps:
1. Store `ALIGN_FILE` into a container
2. Compute the GC-richness for each sequence
3. Compute the GC-richness for each site
4. Determine whether or not each site is phylogenetically informative
5. Compute codon frequencies for each sequence
6. Compute codon frequencies for each site
7. Compute codon usage proportions across amino acids for the entire alignment (this can be stored as a 2d array with amino acids indexing rows and codons indexing columns)

Precise definitions for GC-richness, codons, codon usage frequencies, and phylogenetic informativeness are defined in course materials. Briefly, GC-richness is the proportion of sites that are in G or C rather than A or T. Codons are the nucleotide triplets that encode amino acids during translation. Codon usage frequencies are the proportions that a particular codon-type is used to encode a particular amino acid. A phylogenetically informative site is an alignment site that contains at least two individuals of one variant, and at least two individuals of a different variant -- i.e. the site contains enough information to identify a phylogenetic "split".

**Note:** depending on what dataset you use, you may find that the aligned matrix contains a large number of gaps and/or that it contains an unusual frame shift. For this assignment, treat the alignment as being correct. You may discard any codon sites that contain a gap. You can also "trim" your alignment so that the total number of sites in the alignment is a multiple of three (i.e. drop 1-2 sites).

As output, this script should output five files in .csv format. The beginning of these files will share the name of the alignment 
- `prefix.seq_GC.csv`
- `prefix.site_GC.csv`
- `prefix.seq_phylo_inf.csv`
- `prefix.site_codon.csv`
- `prefix.seq_codon.csv`
- `prefix.codon_usage.csv`
where `prefix` is the alignment name except the file extension (`.fasta`) e.g. `primates_cytb.align_mafft` from `primates_cytb.align_mafft.fasta`.

---

## 6. `make_dnds.py`

*(Relevant labs and lectures: 22)*

The `make_dnds.sh` script will test for the molecular signature of positive selection using the modeling software, PAML. 

### Usage

`./make_dnds.py ALIGN_FILE PHYLO_FILE`

### Behavior

This script accepts a multiple sequence alignment and a phylogenetic tree as input to process using PAML. PAML settings are managed through a control file ([codeml.ctl](https://raw.githubusercontent.com/WUSTL-Biol4220/home/master/assets/course_project/codeml.ctl)), where the appropriate filenames will need to be assigned based on the `make_dnds.py` arguments. Note that the provided control file applies the model settings `NSsites = 0 1 2`, as was done in Lab 22.

PAML will not accept a standard fasta file as input. Instead, PAML uses a custom format, where the first row contains two numbers -- the number of sequences, and the number of sites per sequence -- and each following row gives the sequence name, followed by the sequence content. This [file](https://raw.githubusercontent.com/WUSTL-Biol4220/home/master/assets/course_project/example_convert_paml.py) contains modifiable code for converting fasta formatted files into PAML format.

The script should read in the default PAML output, saving per-site dN/dS scores as a csv file in `${ALIGN_FILE}.site_dnds.csv` and a Newick string estimated using the PAML codon model titled `${ALIGN_FILE}.paml.tre`.

As output, this script should output two files. The beginning of these files will share the name of the alignment -- e.g. `primates_cytb.align_MAFFT.fasta`
- `prefix.paml.tre`
- `prefix.site_dnds.csv`

---

## 7. `make_results.py`

*(Relevant labs and lectures: 02, 04, 05)*

This file will collect all pipeline output located in the target sequence directory, then combine any compatible results and/or logs and generate figures.

### Usage

`./make_results.py SEQUENCE_DIR`

### Behavior

This script should generate a `README.md` file in `SEQUENCE_DIR` that lists the analysis settings and the output files for each step. For example
```
# ./pipeline.sh my_settings.csv job1
# ./parse_settings.sh my_settings.csv
# ./get_seq.sh primates_cytb
primates_cytb/A12345678
primates_cytb/H32183282
primates_cytb/B32701283
primates_cytb/G63645551
# ./make_align.sh sequences mafft '-op 2 -ep 1'`
job1/primates_cytb.align_mafft.fasta
job1/primates_cytb.align_mafft.log
# ./make_phylo job1/primates_cytb.align_mafft.fasta fasttree '-gtr'
job1/primates_cytb.phylo_fasttree.tre
job1/primates_cytb.phylo_fasttree.nw_display.txt
job1/primates_cytb.phylo_fasttree.log
# ./make_mol_stats.py job1/primates_cytb.align_mafft.fasta
primates_cytb.align_mafft.seq_GC.csv
primates_cytb.align_mafft.site_GC.csv
primates_cytb.align_mafft.seq_phylo_inf.csv
primates_cytb.align_mafft.site_codon.csv
primates_cytb.align_mafft.seq_codon.csv
primates_cytb.align_mafft.codon_usage.csv
# ./make_dnds.py job1/primates_cytb.align_mafft.fasta job1/primates_cytb.align_mafft.phylo_fasttree.tre
primates_cytb.align_mafft.phylo_fasttree.paml.tre
primates_cytb.align_mafft.phylo_fasttree.site_dnds.csv
# ./make_results.py SEQUENCE_DIR [RESULTS_OPTIONS]
fig_phy.primates_cytb.align_mafft.phylo_fasttree.pdf
fig_plot.primates_cytb.align_mafft.phylo_fasttree.pdf
```

---

## Possible datasets
- [US SARS-CoV-2 sequences](https://raw.githubusercontent.com/WUSTL-Biol4220/home/master/assets/course_project/accessions_USA.txt) contains accessions for a set of viruses sampled in November, across the United States. Every state is represented once, except for Delaware (DE) and North Dakota (ND). Washington, DC, (DC) and Puerto Rico (PR) were included. This dataset has relatively little molecular variation, but genes are annotated in a manner that's easy to work with.
- [Global SARS-CoV-2 sequences](https://raw.githubusercontent.com/WUSTL-Biol4220/home/master/assets/course_project/accessions_global.txt) contains accessions for virus sequences obtained from roughly fifty countries, worldwide. For each country, the most recently available sequence was used; for most countries, the newest sequence was obtained <30 days ago, while for others the last sequence deposited on GenBank was in Spring 2020. Like the US dataset, the global dataset has relatively low amounts of molecular variation.
- [Orthocoronavirinae](https://raw.githubusercontent.com/WUSTL-Biol4220/home/master/assets/course_project/accessions_Orthocoronavirinae.txt) is a curated dataset hosted by GenBank [here](https://www.ncbi.nlm.nih.gov/genomes/GenomesGroup.cgi?taxid=2501931). Genes for these genomes are annotated in a useful manner that will allow you to compare, for example, the structural proteins (S, E, N, M). Not all coronaviruses have the same set of nonstructural proteins, so those will be more difficult to analyze for various reasons. This dataset also presents extremely high levels of molecular variation, as RNA viruses evolve very rapidly. Aligning the sequences in a meaningful way may be challenging, but you should try if you find this dataset appealing.
- [SARS-like bat and human coronaviruses](https://raw.githubusercontent.com/WUSTL-Biol4220/home/master/assets/course_project/accessions_bat_sarslike.txt) contains over 67 coronavirus sequences sampled from bat and human populations, mostly referenced from [Wells et al. (2020)](wells_et_al_2020_bioRxiv.pdf). These genomes include one SARS-CoV sequence (NC_004718), four SARS-CoV-2 sequences (MW315209, MW320728, MW326508, MW327510), with all remaining sequences originating in bats. These genomes do not share a common naming convention for genes, making it fairly difficult to extract the genes from the dataset. To simplify your analyses, you may use alignments for the four structural proteins, shared here: [S](https://raw.githubusercontent.com/WUSTL-Biol4220/home/master/assets/course_project/CoV_sarslike_bat/S.fasta), [E](https://raw.githubusercontent.com/WUSTL-Biol4220/home/master/assets/course_project/CoV_sarslike_bat/E.fasta), [N](https://raw.githubusercontent.com/WUSTL-Biol4220/home/master/assets/course_project/CoV_sarslike_bat/N.fasta), [M](https://raw.githubusercontent.com/WUSTL-Biol4220/home/master/assets/course_project/CoV_sarslike_bat/M.fasta)
- Bacteria/viruses (TBD)
- Vertebrates (TBD)
- Angiosperms (TBD)
- Birds (TBD)
- Mammals (TBD)
- Primates (TBD)


