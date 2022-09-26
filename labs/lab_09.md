# Lab 09

*Lab 09 GitHub Classroom link:* https://classroom.github.com/a/21aidbIR

This lab will explore how to use regular expressions (regex) to search for patterns in text files using the `grep` command. Lecture 09 reviews the regex features that we'll explore in this lab. Each problem contains smaller exercises.

---

## More `grep` features

Completing the problems for this lab will require the use of `grep`. Several `grep` features will be especially useful. First, the lecture notes contain examples of Perl-compatible regular expressions (PCREs). To use PCREs with `grep`, you must provide the `-P` flag.

For some exercises, rather than having `grep` print the entire line containing the text that matches your regex, you may instead want to print only the exact text matching the regex search pattern. To only print the matched text, supply the `-o` flag.

Finally, may want to print each matched line of text along with several lines adjacent to any matches; this is called the *context*. You can instruct `grep` to print `n` lines of context before (`-B n`), after (`-A n`), or both before and after (`-C n`) the matched line, in addition to the matched line itself.

Here are examples for how to issue these flags with a `grep` call: 

```console
$ cat file.txt
Row, row, row your boat
Gently down the stream
Merrily, merrily, merrily, merrily
Life is but a dream
$ grep -P "[a-z]ow[a-z]?" file.txt
Row, row, row your boat
Gently down the stream
$ grep -o -P "[a-z]ow[a-z]?" file.txt
row
row
down
$ grep -B 1 -P "merrily" file.txt
Gently down the stream
Merrily, merrily, merrily, merrily
```

---

## Problems

You will be asked to write a script to solve each of the following problems. That script may either contain a simple pipeline command, or it may contain more advanced shell programming structures, but all scripts must centrally rely on `grep` and regex to solve the problem at hand.

**Problem 1.** Write a script called `problem1.sh` that accepts a list of Genbank accessions as input, then labels each accession as a nucleotide, protein, WGS, or MGA record. If the accesion is not one of these, then do not return aything for that acession. GenBank accessions differ in format depending on whether an accession identifies a nucleotide sequence, a protein sequence, or a whole genome sequence.

From https://www.ncbi.nlm.nih.gov/Sequin/acc.html:

| Data | Pattern |
|---|---|
| Nucleotide (Nuc) |	1 letter + 5 numerals<br>2 letters + 6 numerals<br>2 letters + 8 numerals |
| Protein (Prot) |	3 letters + 5 numerals<br>3 letters + 7 numerals |
| Whole genome sequences (WGS) |	4 letters + 2 numerals for WGS assembly version + 6 or more numerals<br>6 letters + 2 numerals for WGS assembly version + 7 or more numerals |
| Mass sequence for Genome Annotation (MGA) | 	5 letters + 7 numerals |

Example input:
```
KX734270
U57423
MH81092745
QAA47219
QFF5810257
SSAS01847294
BRAAZO830192789
DADDE7892341
HEIRU39384
X48374874
RR74832
FHI945082
YDHISER2390438912
```

Expected output:
```
KX734270,Nuc
U57423,Nuc
MH81092745,Nuc
QAA47219,Prot
QFF5810257,Prot
SSAS01847294,WGS
BRAAZO830192789,WGS
DADDE7892341,MGA
```

Note, the last five items in the example input are not valid NCBI accessions, so they are not printed. Modify the example input to see if the script behaves as intended!

**Problem 2.** Write a script called `problem2.sh` to identify all sequences of major histocompatibility complex (MHC) genes in `Marra2014_BLAST_data.txt` that are marked as genetic variants. The input file lists a number of unidentified gene sequences (`contigXXXXX`) and the potential function and/or identity of each sequence, as derived from BLAST searches. Sequences with descriptions that contain an asterisk character ("\*") MHC variants. (Hint: use `\*` to escape the asterisk character and search for the literal value `*`).

Expected results:
```
mhc class ii antigen drb1*4
mhc class i antigen cw*8
mhc class i antigen b*46
mhc class ii antigen drb1*1
```

**Problem 3.** Write a script called `problem3.sh` that searches *Origin of Species* for certain classes of words. Download the plain text file for *Origin of Species* from the URL https://raw.githubusercontent.com/WUSTL-Biol4220/home/main/assets/data/oos.txt, and save the file as `oos.txt`. Your script will process `oos.txt` and print a sorted list of the five most common words that begin with a "c" and end with a "d", ignoring upper/lower case. Hints: Use man to find out what the '-c' flag does for the tr command. Can you use character ranges to convert uppercase to lowercase or vice versa?
Expected results:
```
271 could
126 called
116 crossed
73 changed
60 considered
```
 
**Problem 4.**

Write a script called `problem4.sh` to process the file `bee_list.txt`, which contains information regarding bee biodiversity. `bee_list.txt` is a tab-delimited file reporting nearly 20,000 bee species, a list of papers for each species initial description, and unique identifiers for each bee species in the Taxonomic Information System. Your script should print the `N` authors in `bee_list.txt` that have the most publications. (Assume that each occurrence to the name [e.g.] "Eversmann" refers to the same person.) Also, the script should report the `N` years with the highest numbers of publications. The value of `N` is a user-provided argument. When printing the "top" results, also print their respective counts.

Expected results:
```
Top 5 authors:
 3394 Cockerell
 1330 Friese
 950 Smith
 864 Timberlake
 557 Vachal

Top 5 years of species descriptions:
 406 1903
 405 1910
 320 1904
 316 1909
 313 1879
```

Note, to use `cut` against the `\t` delimiter, use the option `cut -d $'\t'`. The `$'...'` format is a special escape string that allows the tab-character (and other escaped characters, like `\n`) be recognized by its literal value (`\t`).

---

To complete the assignment, please submit the four script files (`problem1.sh`, `problem2.sh`, `problem3.sh`, and `problem4.sh`) and the contents of `history > history.txt`.
