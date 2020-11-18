# Lab 10B

*Lab 10B GitHub Classroom link:* https://classroom.github.com/a/U1cmZxrD

In this lab, we will learn how to use the Biopython library.

To begin this lab, clone your GitHub assignment repository to your virtual machine, enter the newly cloned directory, then open the `python` or `ipython` command line interface.

---

## Biopython

[Biopython](https://biopython.org/) is a Python library design by and for bioinformaticians, with an emphasis on sequence manipulation. The Biopython [Tutorial and Cookbook](http://biopython.org/DIST/docs/tutorial/Tutorial.html) provides a detailed walkthrough with working code snippets to showcase the library's capabilities. Refer to the Biopython [documentation](https://biopython.org/wiki/Documentation) for a complete description for how each function is defined. Your virtual machine should already have Biopython installed on it.

Biopython stores raw sequence data using `Seq` objects. `Seq` objects behave much like immutable strings, in terms of how they're created and accessed. First, we will `import` the code for the `Seq` class, so that we can make `Seq` objects, then we will create our first `Seq` variable.

```python
>>> from Bio.Seq import Seq       # import Seq class definition
>>> my_seq = Seq('GATTACA')       # create a sequence object
>>> my_seq                        # return value
Seq('GATTACA')
>>> my_seq[0:2]                   # extact subsequence
Seq('GA')
>>> len(my_seq)                   # get length
7
>>> Seq('r u rly a string?')      # no alphabet imposed
Seq('r u rly a string?')
```

In addition, `Seq` objects are equipped with the same general methods as strings

```python
>>> my_seq = Seq('GATTACA')   # make sequence
>>> str(my_seq)               # typecast as string
'GATTACA'
>>> my_seq.lower()            # change case (.upper supported)
Seq('gattaca')
>>> my_seq.find('TAC')        # find start index for subseq
3
>>> my_seq.count('TAC')       # count occurrences
1
>>> Seq('AAAA').count('A')    # non-overlapping count
2
>>> Seq('AAAA').count_overlap('AA') # overlapping count
3
>>> (my_seq.count('C')+my_seq.count('G')) / len(my_seq) * 100
28.57142857142857             # compute GC content
```

The elements of a `Seq` object can be indexed and concatenated in the same manner as with strings.

```python
>>> my_seq = Seq('GATCGATGGGCCTATATAGGA')
>>> my_seq[4:12]              # extract subsequence
Seq('GATGGGCC')
>>> my_seq[0::3]              # first codon position
Seq('GCTGTAG')
>>> my_seq[1::3]              # second codon position
Seq('AGGCATG')
>>> my_seq[2::3]              # third codon position
Seq('TAGCTAA')
>>> my_seq[:7]+Seq('NNNNNNN')+ my_seq[14:]
Seq('GATCGATNNNNNNNTATAGGA')
```

`Seq` objects are immutable, meaning we cannot assign new values to the object after is created; the `MutableSeq` object does not have this restriction, however.


```python
>>> my_seq                         # create sequence
Seq('GATTACA')
>>> my_seq[0] = 'C'                # attempt to modify seq
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'Seq' object does not support item assignment
>>> mut_seq = my_seq.tomutable()   # convert to mutable seq
>>> mut_seq[0] = 'C'               # modify seq successfuly
>>> mut_seq
MutableSeq('CATTACA')
>>> new_seq = mut_seq.toseq()      # convert to immutable seq
>>> new_seq
Seq('CATTACA')
```

`Seq` objects also provide several methods that are useful to the analysis of sequence data.

```python
>>> my_seq = Seq('GATCGATGGGCCTATATAGGATCGAAAATCGC')
>>> my_seq
Seq('GATCGATGGGCCTATATAGGATCGAAAATCGC')
>>> my_seq.complement()          # return complement
Seq('CTAGCTACCCGGATATATCCTAGCTTTTAGCG')
>>> my_seq.reverse_complement()  # return reverse-complement
Seq('GCGATTTTCGATCCTATATAGGCCCATCGATC')
>>> from Bio.SeqUtils import GC
>>> GC(my_seq)                   # what is the GC content?
46.875
```

Recall the Central Dogma of Molecular Biology, which explains how DNA is converted into protein: DNA sequences are transcribed into RNA, and RNA sequences are translated (as codons) into amino acid sequences. `Seq` objects possess transcription and translation methods that modify sequence content accordingly. The `.translate()` method allows you to specify which genetic code is used for translation (see below), and to terminate amino acid sequenced upon translating the first stop codon under that genetic code.

```python
>>> cDNA = Seq('ATGGCCATTGTAATGGGCCGCTGAAAGGGTGCCCGATAG')
>>> cDNA                          # coding DNA sequence       
Seq('ATGGCCATTGTAATGGGCCGCTGAAAGGGTGCCCGATAG')
>>> mRNA = cDNA.transcribe()      # transcribe DNA into mRNA
>>> mRNA
Seq('AUGGCCAUUGUAAUGGGCCGCUGAAAGGGUGCCCGAUAG', RNAAlphabet())
>>> mRNA.translate()              # translate mRNA into AA
Seq('MAIVMGR*KGAR*', HasStopCodon(ExtendedIUPACProtein(), '*'))
>>> cDNA.translate()              # translate DNA into AA
Seq('MAIVMGR*KGAR*', HasStopCodon(ExtendedIUPACProtein(), '*'))
>>> cDNA.translate(to_stop=True)  # terminate AA at stop codon
Seq('MAIVMGR', ExtendedIUPACProtein())
>>> # consider an alternate table (default: 'Standard')
>>> cDNA.translate(table='Vertebrate Mitochondrial')
Seq('MAIVMGRWKGAR*', HasStopCodon(ExtendedIUPACProtein(), '*')
>>> cDNA.translate(table='"'Vertebrate Mitochondrial'"', to_stop=True)
Seq('MAIVMGRWKGAR', ExtendedIUPACProtein())
```

The `table` arguments provided in the previous example determine how each codon is translated into each amino acid (and vice versa). Which table is appropriate for translation depends on which organism and what part of the genome (e.g. nuclear vs. mitochondrial) is being translated. The "Standard" table, for example, correspons to nuclear genes for most eukaryotes.

```python
>>> from Bio.Data import CodonTable      # import CodonTable class definition
>>> standard_table = CodonTable.unambiguous_dna_by_name["Standard"]
>>> standard_table.stop_codons           # returns all stop codons
['TAA', 'TAG', 'TGA']
>>> standard_table.start_codons          # returns all start codons
['TTG', 'CTG', 'ATG']
>>> standard_table.forward_table['GTG']  # returns AA for codon
'V'
>>> standard_table.back_table['V']       # returns ONE codon for AA
'GTT'
>>> print(standard_table)
```

To read sequence data, like fasta files, we can use functions int he `SeqIO` module. Data structures read using `SeqIO.parse()` are iterable containers that contain `SeqRecord` elements. `SeqRecord` objects contain a number of properties, including the sequence's identifier, identity, etc. However, the container's `SeqRecord` elements cannot be readily accessed with index operations. Instead, such elements can be read by iterating through the container (e.g. with a for-loop), or by converting the container into something with index-support, like a dictionary.

```python
>>> from Bio import SeqIO                 # import the SeqIO methods
>>> from Bio.SeqRecord import SeqRecord   # import SeqRecord class definition
>>> # create iterable container of SeqRecords
>>> f = SeqIO.parse('example.fasta', 'fasta')
>>> for row in f:
...   print( row.id + ' : ' + row.seq )
...

Species_A : ACGCTG
Species_B : ACTCTG
Species_C : AGTATC
Species_D : AGTCTC

>>> # convert to dict of SeqRecords
>>> d = SeqIO.to_dict(SeqIO.parse('example.fasta','fasta'))
>>> d
{'Species_A': SeqRecord(seq=Seq('ACGCTG', SingleLetterAlphabet()), id='Species_A', name='Species_A', description=' Species_A', dbxrefs=[]),
 'Species_B': SeqRecord(seq=Seq('ACTCTG', SingleLetterAlphabet()), id='Species_B', name='Species_B', description=' Species_B', dbxrefs=[]),
 'Species_C': SeqRecord(seq=Seq('AGTATC', SingleLetterAlphabet()), id='Species_C', name='Species_C', description=' Species_C', dbxrefs=[]),
 'Species_D': SeqRecord(seq=Seq('AGTCTC', SingleLetterAlphabet()), id='Species_D', name='Species_D', description=' Species_D', dbxrefs=[])}
>>> d['Species_A']
SeqRecord(seq=Seq('ACGCTG', SingleLetterAlphabet()), id='Species_A', name='Species_A', description=' Species_A', dbxrefs=[])
```

A list of `SeqRecord` elements, whether read from a file or constructed manually, can be written to file using the function `SeqIO.write()`.

```python
>>> # make sequence records to write
>>> rec1 = SeqRecord(seq=Seq('ACGTTA'),id='Species_A',description='')
>>> rec2 = SeqRecord(seq=Seq('TCGTTA'),id='Species_B',description='')
>>> rec3 = SeqRecord(seq=Seq('ACGTGT'),id='Species_C',description='')
>>> my_records = [rec1, rec2, rec3]  # list of records
>>> SeqIO.write(my_records, 'new_file.fasta', 'fasta')
```

Sequence alignments may also be read in as multiple sequence alignments (`MultipleSeqAlignment`). Because, by definition, all sequences in an alignment share the same number of sites, `MultipleSeqAlignment` objects can be indexed both in terms of rows (sequence) and columns (sites). To read in a multiple sequence alignment file, we use `AlignIO.read()`.

```python
>>> from Bio import AlignIO
>>> alignment = AlignIO.read("new_file.fasta", "fasta")
>>> print(alignment)             # full alignment
SingleLetterAlphabet() alignment with 3 rows and 6 columns
ACGTTA Species_A
TCGTTA Species_B
ACGTGT Species_C
GCATGT Species_D
>>> print(alignment[1:3,:])
SingleLetterAlphabet() alignment with 2 rows and 6 columns
TCGTTA Species_B
ACGTGT Species_C
>>> print(alignment[:,3:5])
SingleLetterAlphabet() alignment with 4 rows and 2 columns
TT Species_A
TT Species_B
TG Species_C
TG Species_D
>>> print(alignment[1:3,3:5])
SingleLetterAlphabet() alignment with 2 rows and 2 columns
TT Species_B
TG Species_C
```

`MultipleSeqAlignment` objects may also be constructed manually, using a list of `SeqRecord` objects. Writing `MultipleSeqAlignment` objects to file is done without effort, using `AlignIO.write()`

```python
>>> from Bio.Align import MultipleSeqAlignment
>>> alignment = MultipleSeqAlignment(
...     [
...         SeqRecord(Seq("ACTCCTA"), id='seq1'),
...         SeqRecord(Seq("AAT-CTA"), id='seq2'),
...         SeqRecord(Seq("CCTACT-"), id='seq3'),
...         SeqRecord(Seq("TCTCCTC"), id='seq4'),
...     ]
... ) # create a list of SeqRecord objects
...
>>> print(alignment)
Alignment with 4 rows and 7 columns
ACTCCTA seq1
AAT-CTA seq2
CCTACT- seq3
TCTCCTC seq4

>>> # write new alignment to file
>>> AlignIO.write(alignment, 'new_alignment.fasta', 'fasta')
```

## Exercises

You will create a separate Python script for each of the following problems.

Write a module file called `biopython_stats.py`. The module will define several functions to read a sequence aligment of nucleotides, to translate the codons into amino acids depending on the reading frame, to classify amino acids into classes of physicochemical properties, and to report codon usage frequencies per amino acid.

**Part 1.** Write a function called `read_alignment(filename)` that accepts the name for a fasta-formatted sequence alignment of DNA as input. The function will read the file using the function  `AlignIO.read(filename, "fasta")`, translate the codons into amino acids, and return the amino acid alignment.

For example, if the file `example.fasta` contained

```
> Species_A
ACGCTG
> Species_B
ACTCTG
> Species_C
AGTATC
> Species_D
AGTCTC
```

then calling `read_alignment('example.fasta')` would return the amino acid alignment

```python
>>> a = read_alignment('example.fasta')
>>> a
<<class 'Bio.Align.MultipleSeqAlignment'> instance (4 records of length 2, ExtendedIUPACProtein()) at 7f3cdada9670>
>>> for x in a:
...   print(f'{x.id} : {x.seq}')
...
Species_A : TL
Species_B : TL
Species_C : SI
Species_D : SL
```

**Part 2.** Write a function called `find_physicochemical_seq(aa_alignment)` that identifies the physicochemical properties for each amino acid in the alignment. The `aa_alignment` argument is an alignment of amino acids, similar to that output by `read_alignment()`. Below is a list of  amino acid properties, and the amino acids with that property.

```
hydrophobic: I, V, L, F, C, M, A, W
hydrophilic: N, D, Q, E, K, R
negative: D, E
positive: R, H, K
tiny: A, G, S
huge: F, W, Y
polar: R, N, D, Q, E, H, K, S, T, Y
```

The script should return a dictionary-of-dictionaries that reports the percent of amino acids that fall into each class. For example, using the amino acid alignment above, the script would return

```
>>> d = find_physicochemical_seq(aa_alignment)
>>> d
{'Species_A': {'hydrophobic': 0.5, 'hydrophilic': 0.0, 'negative': 0.0, 'positive': 0.0, 'tiny': 0.0, 'huge': 0.0, 'polar': 0.5},
 'Species_B': {'hydrophobic': 0.5, 'hydrophilic': 0.0, 'negative': 0.0, 'positive': 0.0, 'tiny': 0.0, 'huge': 0.0, 'polar': 0.5},
 'Species_C': {'hydrophobic': 0.5, 'hydrophilic': 0.0, 'negative': 0.0, 'positive': 0.0, 'tiny': 0.5, 'huge': 0.0, 'polar': 0.5},
 'Species_D': {'hydrophobic': 0.5, 'hydrophilic': 0.0, 'negative': 0.0, 'positive': 0.0, 'tiny': 0.0, 'huge': 0.0, 'polar': 0.5}}
```

**Part 3.** Write a function called `codon_usage_bias(nt_alignment)` that accepts a nucleotide alignment (`nt_alignment`) as input, translates all codons into amino acids, then reports the percents that each codon was used per amino acid.

For example, we know that the file `example.fasta`

```
> Species_A
ACGCTG
> Species_B
ACTCTG
> Species_C
AGTATC
> Species_D
AGTCTC
```

translates to

```
> Species_A
TL
> Species_B
TL
> Species_C
SI
> Species_D
SL
```

the function would return the dictionary-of-dictionaries

```python
>>> z = codon_usage_bias(nt_alignment)
>>> z
{'T': {'ACA': 0, 'ACC': 0, 'ACG': 1, 'ACT': 1},
 'L': {'CTA': 0, 'CTC': 1, 'CTG': 2, 'CTT': 0, 'TTA': 0, 'TTG': 0},
 'S': {'TCA': 0, 'TCC': 0, 'TCG': 0, 'TCT': 0, 'AGC': 0, 'AGT': 2},
 'I': {'ATA': 0, 'ATC': 1. 'ATT': 0}}
```
where the first key gives the amino acid, the second key gives the codon translated into that amino acid, and the second key's value gives the count for how many times that particular codon appears in the sequence alignment. By listing codons with counts of 0, the dictionary can easily be used to test for codon usage bias, if so desired.

(**Bonus problem.** Let `find_physicochemical_seq()` and `codon_usage_bias()` accept an argument `frame_shift` that "shifts" the reading from to the right by 0, 1, or 2 sites. Do your molecular statistics for physicochemical properties and codon usage bias change in response to different `frame_shift` values?)

To complete the lab, commit and push your script to your GitHub repository.

