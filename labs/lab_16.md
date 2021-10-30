# Lab 16

*Lab 16 GitHub Classroom link: to be provided*

In this lab, we will use Python to extract various statistics about the patterns of molecular variation contained in a multiple sequence alignment.

To begin this lab, clone your GitHub assignment repository to your virtual machine, enter the newly cloned directory, then open the `python` or `ipython` command line interface.

---


## Exercises

You will create a separate Python script for each of the following problems.

Write a module file called `mol_stats.py`. This module will contain several functions to measure how 

**Part 1.** Write a function called `read_alignment(filename)` that accept the name for a fasta-formatted file as input. The function will create a dictionary of lists, where the keys in the dictionary correspond to species names, and each value corresponds to a list-of-strings that describes the aligned sequence associated with that species. The function reads the fasta file, then populates and returns the dictionary. For example, if the fasta file was

```
> Species_A
ACGCTG
> Species_B
AC-CTG
> Species_C
AGTATC
> Species_D
AGTCTC
```

the function would return the object

```python
>>> d = read_alignment('example.fasta')
>>> d
{'Species_A': ['A','C','G','C','T','G'],
 'Species_B': ['A','C','-','C','T','G'],
 'Species_C': ['A','G','T','A','T','C'],
 'Species_D': ['A','G','T','C','T','C']}
```

The remaining functions will expect a data object called the *alignment dictionary* with this format as input.

**Part 2.** Write a function called `nt_seq(d)` that reports the proportion of nucleotides in state A, C, G, T, and - for each sequence stored in the alignment dictionary, `d`. The function returns a dictionary-of-dictionaries, where the species names are the first key, the nucleotide is the second key, and the ultimate value is the corresponding nucleotide frequency

```python
>>> my_seq = nt_seq(d)
>>> my_seq
{ 'Species_A': {'A': 0.167, 'C': 0.333, 'G': 0.333, 'T': 0.167, '-': 0.0},
  'Species_B': {'A': 0.167, 'C': 0.333, 'G': 0.167, 'T': 0.167, '-': 0.167},
  'Species_C': {'A': 0.333, 'C': 0.167, 'G': 0.167, 'T': 0.333, '-': 0.0},
  'Species_D': {'A': 0.167, 'C': 0.333, 'G': 0.167, 'T': 0.333, '-': 0.0} }
>>> my_seq['Species_B']['C']
0.333
```

**Part 3.** Write a function called `nt_site(d)` that reports the proportion of nucleotides in state A, C, G, T, and - for each site in the alignment dictionary, `d`. The function returns a list-of-dictionaries, with the site position as the first index, the nucleotide as the key, which together identify the frequency for a particular nucleotide at a particular site

```python
>>> my_site = nt_site(d)
>>> my_site
[ {'A': 1.0, 'C': 0.0, 'G': 0.0, 'T': 0.0, '-': 0.0},
  {'A': 0.0, 'C': 0.5, 'G': 0.5, 'T': 0.0, '-': 0.0},
  {'A': 0.0, 'C': 0.0, 'G': 0.25, 'T': 0.5, '-': 0.25},
  {'A': 0.25, 'C': 0.75, 'G': 0.0, 'T': 0.0, '-': 0.0},
  {'A': 0.0, 'C': 0.0, 'G': 0.0, 'T': 1.0, '-': 0.0},
  {'A': 0.0, 'C': 0.5, 'G': 0.5, 'T': 0.0, '-': 0.0} ]
  
>>> my_site[2]['G']
0.25
```

**Part 4.** Write a function called `phyinfo_site(d)` that identifies whether a particular site is phylogenetically informative or not. A site is phylogenetically informative if that site has 2+ variants, with each variant represented by 2+ sequences. For example, if a site had the nucleotides `A`, `A`, `G`, `G` for four species, that would be phylogenetically informative. Sites with patterns like `A`, `A`, `A`, `A`; `A`, `C`, `A`, `A`; `A`, `C`, `T`, `A`; and `A`, `A`, `-`, `-` are not phylogenetically informative. The function will return a list of boolean values that report whether or not each site is phylogenetically informative.

```python
>>> my_phyinfo_site = phyinfo_site(d)
>>> my_phyinfo_site
[ False, True, False, False, False, True ]
>>> x[1]
True
```

To complete the lab, commit and push your `mol_stats.py` module script to your GitHub repository.

