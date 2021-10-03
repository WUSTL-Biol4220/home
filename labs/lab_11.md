# Lab 11

*Lab 11 GitHub Classroom link:* to be provided

In this lab, we will learn how to estimate phylogenies from molecular sequence data using a variety of inference methods.

1. Install phylogenetics software
2. Representing phylogenies
3. Running phylogenetic analyses
4. Scripting phylogenetics analyses

---

## Install phylogenetics software

We will install four pieces of phylogenetics software for this lab.

### Install FastTree

FastTree (http://www.microbesonline.org/fasttree/) is phylogenetic inference software specializes in rapidly inferring molecular phylogenies using a variety of inference methods. For the purposes of our lab, we'll use FastTree to infer phyologenies using the distance-based neighbor-joining algorithm.

```
$ mkdir ~/fasttree
$ cd ~/fasttree
$ wget http://www.microbesonline.org/fasttree/FastTree
$ chmod +x FastTree
$ cp FastTree ~/.local/bin/fasttree
```

### Install IQ-Tree
IQ-Tree (http://www.iqtree.org/) is another phylogenetics package, which specializes in likelihood-based models for phylogenetic inference.

```
$ cd ~/apps
$ wget https://github.com/Cibiv/IQ-TREE/releases/download/v1.6.12/iqtree-1.6.12-Linux.tar.gz
$ tar zxvf iqtree-1.6.12-Linux.tar.gz
$ cp ~/apps/iqtree-1.6.12-Linux/bin/iqtree ~/.local/bin
```

Documnetation for IQ-Tree: http://www.iqtree.org/doc/

### Install MPBoot

MPBoot (http://www.iqtree.org/mpboot/), which is also written by the authors of IQ-Tree, is a phylogenetics package for rapidly estimating phylogenies using maximum parsimony.

```
$ cd ~/apps
$ wget http://www.iqtree.org/mpboot/mpboot-avx-1.1.0-Linux.tar.gz
$ tar zxvf mpboot-avx-1.1.0-Linux.tar.gz
$ cp ~/apps/mpboot-avx-1.1.0-Linux/bin/mpboot-avx ~/.local/bin/mpboot
```

### Installing newick_utils

Finally, we will us the software Newick Utilities (https://github.com/tjunier/newick_utils) to visualize what trees we estimate using these three phylogenetic methods.
```
$ cd ~/apps
$ wget https://github.com/WUSTL-Biol4220/home/raw/main/assets/files/newick-utils-1.6-Linux-x86_64-disabled-extra.tar.gz
$ tar zxvf newick-utils-1.6-Linux-x86_64-disabled-extra.tar.gz
# ... decompresses and extracts many files ...
$ cp ~/apps/newick-utils-1.6/src/nw_* ~/.local/bin
```
Documentation for Newick Utilities is hosted here: https://github.com/tjunier/newick_utils/blob/master/doc/nwutils_tutorial.pdf


---

## Representing phylogenies

Phylogenetic trees are generally represented either as human-readable visualizations, or computer-readable Newick strings.

Newick strings are compact and computer-readable formats for storing phylogenetic relationships. The simplest features of a Newick string report the phylogenetic relationships (or *topology*) of the taxa:

For example, suppose we create a file `simple_newick.tre` with the following contents
```
$ cat simple_newick.tre
((A,B),(C,D));
```

or in an expanded format
```
$ nw_indent simple_newick.tre
(
  (
    A,
    B
  ),
  (
    C,
    D
  )
);
```


We can visualize that Newick string with the command
```
$ nw_display simple_newick.tre
                                       +-------------------------------------+ A
 +-------------------------------------+
 |                                     +-------------------------------------+ B
=|
 |                                     +-------------------------------------+ C
 +-------------------------------------+
                                       +-------------------------------------+ D
```                                       

How does the Newick string relate to the visualization?
- Taxon labels (A, B, C, D) identify the tips of the phylogeny
- Parentheses identify the nested relationships among taxa. Taxa that share close relationships lie within a pair of parentheses, while taxa more distantly related sit outside the parentheses. For example, species A and B are more closely related to each other than to C or D.
- Commas identify divergence events between lineages. For example, we see that A and B are separate lineages, C and D are separate lineages, *and* the most recent common ancestor of A and B is separate from the most recent common ancestor of C and D.
- Each `)` character completes the definition of a clade, meaning all lineages within that `(...)` statement are more closely related to each other than to any other taxa. Equivalently, each `)` marks the internal node that is the most recent common ancestor of all taxa contained by the `(...)` statement.

Newick strings typically report richer information, including the amount of molecular divergence (*branch lengths* measured in expected numbers of substitution per site) or the degree of statistical support for recovering a certain phylogenetic relationship (called *clade support*)

Create a file called `richer_newick.tre` with the following contents:

```
$ cat richer_newick.tre
((A:0.1,B:0.2)0.75:0.3,(C:0.3,D:0.2)0.9:0.2);
```

The topology of `richer_newick.tre` is the same as `simple_newick.tre`, but it is annotated with branch lengths and clade support values. It can be viewed in in expanded format,

```
$ nw_indent richer_newick.tre
(
  (
    A:0.1,
    B:0.2
  )0.75:0.3,
  (
    C:0.3,
    D:0.2
  )0.9:0.2
);
```

can be also visualized as

```
$ nw_display richer_newick.tre
                                               +--------------+ A
 +---------------------------------------------+ 0.75
 |                                             +-----------------------------+ B
=|
 |                             +---------------------------------------------+ C
 +-----------------------------+ 0.9
                               +------------------------------+ D

 |--------------|--------------|---------------|--------------|--------------|
 0            0.1            0.2             0.3            0.4            0.5
 substitutions/site
```

What new features in the richer Newick string require description?
- The colon and number that immediately follows each node in the tree tells us the branch length for that lineage. For example, `A:0.1` indicates that the branch length for A is 0.1 expected substitutions/site.
- Internal nodes, identified by `)` characters in the Newick string, are marked with two pieces of information. For example, the clade that contains taxa and and B is defined by `(A:0.1,B:0.2)0.75:0.3`. This part of the string tells us that the clade (A+B) has a support metric of 75% and a branch length of 0.3 expected substitutions/site.

Read the contents of `richer_newick.tre` carefully and make sure you understand how each part of the Newick string relates the the `nw_display` visualization.

---


## Running phylogenetic analyses

In this section, we will familiarize ourselves with the syntax for each for each piece of phylogenetics software. Our example datasets are stored in `data`. We'll store out results in the directory `output` (create as needed).


### Neighbor-joining with FastTree

We will use FastTree to infer the phylogenetic relationships of cytB using aligned primate DNA. Because FastTree assumes the input dataset will be amino acids by default, we will supply the `-nt` flag to inform the software our alignment is composed of nucleotides. FastTree also uses an approximate maximum-likelihood method along with neighbor-joining methods for tree esimation; we will disable the use of maximum likelihood disable using the `-noml` flag, simply to illustrate what we obtain with neighbor-joining alone.

```
$ fasttree -nt -noml data/primates_and_galeopterus_cytb.fasta > output/primates-JC-NJ.tre
FastTree Version 2.1.11 SSE3
Alignment: data/primates_and_galeopterus_cytb.fasta
Nucleotide distances: Jukes-Cantor Joins: balanced Support: Local boot 1000
Search: Normal +NNI +SPR (2 rounds range 10) (no ML-NNI)
TopHits: 1.00*sqrtN close=default refresh=0.80
Ignored unknown character X (seen 1 times)
Initial topology in 0.01 seconds
Refining topology: 18 rounds ME-NNIs, 2 rounds ME-SPRs, 0 rounds ML-NNIs
Total branch-length 2.760 after 0.44 sec8, 1 of 21 splits
Total time: 0.67 seconds Unique: 23/23 Bad splits: 0/20
```

Upon completion, FastTree prints a Newick string to standard output
```
$ cat output/primates-JC-NJ.tre
(Galeopterus_variegatus:0.15599,((Saimiri_sciureus:0.12228,(Aotus_trivirgatus:0.09990,(Cebus_albifrons:0.10231,Callicebus_donacophilus:0.10515)0.589:0.00652)0.804:0.01115)1.000:0.05145,((Hylobates_lar:0.10901,Pan_paniscus:0.08691)0.959:0.01763,(Colobus_guereza:0.11724,(Chlorocebus_aethiops:0.08114,Macaca_mulatta:0.09615)0.990:0.02012)0.989:0.02182)0.999:0.03189)0.999:0.02692,(Daubentonia_madagascariensis:0.12656,((Lepilemur_hubbardorum:0.12315,((Microcebus_murinus:0.11794,Cheirogaleus_major:0.08173)0.958:0.01517,(Propithecus_coquereli:0.09400,(Varecia_variegata_variegata:0.11152,Lemur_catta:0.08932)0.720:0.00770)0.851:0.00814)0.562:0.00333)0.995:0.02072,(Tarsius_syrichta:0.14953,((Loris_tardigradus:0.10023,Nycticebus_coucang:0.10539)0.807:0.00894,(Perodicticus_potto:0.09784,(Galago_senegalensis:0.07533,Otolemur_crassicaudatus:0.08621)0.999:0.02583)0.921:0.01151)0.960:0.01641)0.936:0.01055)0.673:0.00590)0.547:0.00386);
```

### Maximum likelihood with IQ-Tree 

Now, we will estimate the maximum likelihood tree using IQ-Tree. IQ-Tree offers hundreds of features, but we will explore only a few in this lab. Type `iqtree --help` to review all available features.

Regardless of what features we use, we'll need to specify the input sequence file (`-s data/primates_and_galeopterus_cytb.fasta `). In addition, we will instruct IQ-Tree to use an extremely simple model where all nucleotide substitutions occur at the same rate, and all nucleotides occur at the same frequency in the data (`-m JC+FQ`). To compute clade support metrics, we compute 1000 site-permutation tests (a procedure called *bootstrapping*) to determine whether we would estimate the same phylogeny if we were to hypothetically sample different nucleotides for the same set of taxa (`-bb 1000`). Finally, molecular phylogenetic analyses often infer *unrooted* phylogenies, which disregard the notion of time -- i.e. that one pair of lineages diverged before another pair of lineages. To *root* our phylogeny, we will identify which taxon is most distantly related to all other taxa; this is called the *outgroup*, which in our case is the flying lemur, *Galeopterus variegatus* (`-o Galeopterus_variegatus`). Finally, we will ask IQ-Tree to following our naming scheme for output  files (`-pre output/primates-JC-MLE`):

```
$ iqtree -s data/primates_and_galeopterus_cytb.fasta -m JC+FQ -bb 1000 -o Galeopterus_variegatus -pre output/primates-JC-MLE
[ ... lots of output ... ]
Analysis results written to:
  IQ-TREE report:                output/primates-JC-MLE.iqtree
  Maximum-likelihood tree:       output/primates-JC-MLE.treefile
  Likelihood distances:          output/primates-JC-MLE.mldist

Ultrafast bootstrap approximation results written to:
  Split support values:          output/primates-JC-MLE.splits.nex
  Consensus tree:                output/primates-JC-MLE.contree
  Screen log file:               output/primates-JC-MLE.log
```

The IQ-Tree output that is of most interest is `output/primates-JC-MLE.contree`

```
$ cat output/primates-JC-MLE.contree
(((Saimiri_sciureus:0.1239752697,(Callicebus_donacophilus:0.1020864274,(Cebus_albifrons:0.0983848577,Aotus_trivirgatus:0.1042444580)45:0.0251511972)53:0.0349025280)100:0.0776567284,((Hylobates_lar:0.1146820143,Pan_paniscus:0.0808129287)93:0.0320053991,(Colobus_guereza:0.1254055000,(Chlorocebus_aethiops:0.0793995081,Macaca_mulatta:0.0980342609)96:0.0277058194)100:0.0441403542)100:0.0531336716)100:0.0461693791,(((Tarsius_syrichta:0.1666672071,(((Galago_senegalensis:0.0784946174,Otolemur_crassicaudatus:0.0846763436)100:0.0459002932,Perodicticus_potto:0.0974196762)91:0.0259484374,(Loris_tardigradus:0.0979654601,Nycticebus_coucang:0.1100940690)83:0.0323645409)80:0.0325003007)34:0.0234662782,(Lepilemur_hubbardorum:0.1267055210,(((Varecia_variegata_variegata:0.1124506063,Lemur_catta:0.0857991684)78:0.0357837557,Propithecus_coquereli:0.0900948559)49:0.0238106553,(Microcebus_murinus:0.1202963845,Cheirogaleus_major:0.0782454409)97:0.0394293337)59:0.0292536656)100:0.0539654199)23:0.0180351073,Daubentonia_madagascariensis:0.1293442077)52:0.0287209999,Galeopterus_variegatus:0.1667330484);
```

### Maximum parsimony with MPBoot

Finally, we will estimate the maximum parsimony tree for primate cytB using `mpboot`. The syntax is very similar to that for `iqtree`, except that parsimony methods do not have evolutionary models, so we do not specify the `-m` option

```
mpboot -s data/primates_and_galeopterus_cytb.fasta -bb 1000 -o Galeopterus_variegatus -pre output/primates-MP
```

(Note: like most parsimony methods, `mpboot` does not estimate branch lengths.)

We can now use `nw_display` to visualize the different relationships each method estimated, along with differences in clade support and branch lengths across methods. Which clades have the greatest 

Tree estimates can also be compared using *Robinson-Foulds distance* (or RF distance), which essentially measures the number of taxa that would have to be deleted from a pair of trees for the two trees to be identical. The larger the RF score, the more different the two trees are. To (quietly) compute the RF distance between the trees, use the following commands

```
$ iqtree -quiet -te output/primates-JC-MLE.contree -rf output/primates-MP.contree -pre output/MLE-MP-RF
$ cat output/MLE-MP-RF.rfdist
1 1
Tree0       2
```

This indicates that the maximum likelihood (MLE) and maximum parsimony (MP) trees have a RF distance of 2. This means each tree would have to delete one taxon from its tree for the two trees to be identical. Which taxon position differs between the MLE and MP estimates? Do the NJ and MLE or NJ and MP estimates differ?

---

## Scripting phylogenetics analyses

*Part 1.* Write a script called `build_phylo.sh` that accepts a DNA sequence alignment in fasta format as an input argument.  The script will then estimate the phylogeny from that alignment using `fasttree`, `iqtree`, and `mpboot`, using the settings defined in the previous section. Use a variable named `METHOD` to record whether the tree was estimated using neighbor-joining (`NJ`), maximum likelihood (`ML`), or maximum parsimony (`MP`). Store the input filename, except for the `.fasta` file extension, into a variable called e.g. `INPUT_PREFIX`. Then define the variable `OUTPUT_PREFIX` that is equal to `${INPUT_PREFIX}.${METHOD}`.

For each analysis, the script should ensure all standard output from the methods has the prefix `${OUTPUT_PREFIX}`. In addition, save text-plots for each phylogeny into the file `${OUTPUT_PREFIX}.tree_plot.txt` using `nw_display`. Finally, save three files that compute the Robinson-Foulds distance between the pairs trees estimated by the three methods: `${INPUT_PREFIX}.MLE_MP.rfdist`, `${INPUT_PREFIX}.MLE_NJ.rfdist`, and `${INPUT_PREFIX}.MP_NJ.rfdist`.

*Part 2.* Write a script called `batch_phylo.sh` that accepts a text file containing a list of fasta files as an argument. This script will apply `build_phylo.sh` to each fasta file in the list, and store output for each input file in an organized manner into a local directory `output/${INPUT_PREFIX}`. In particular, create the file `input_sequences.txt` that contains

```
data/primates_and_galeopterus_cytb.fasta
data/testudines_cytb.fasta
data/silverswords_its.fasta
```

then run `batch_phylo.sh input_sequences.txt`.

---

Submit the the following files to complete the assignment:
- `simple_newick.tre`
- `richer_newick.tre`
- `build_phylo.sh`
- `batch_phylo.sh`
- the `output` directory and its contents
- the output of `history > history.txt`
