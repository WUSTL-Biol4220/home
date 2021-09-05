# Lab 05

*Lab 05 GitHub Classroom link:* to be provided

This lab will study how to process a variety of text files. 

The major tasks to complete for Lab 05 are
1. Learning new text manipulation commands
2. Modifying text-processing pipelines
3. Writing text-processing pipelines

To complete this lab, you will need to clone your GitHub Classroom repository for assignment Lab 05 on to your VM. Exercises will process the contents of the cloned repo's `data` directory in various ways.

---
## 1. Text processing commands

The first section of this lab will introduce you to several commands for processing text. Before you become acquainted with these new tools, let's reacquaint ourselves with our old friend, `grep`, to learn some of its more advanced features.

For this section, we'll process the text in the comma-delimited file, `data/Asteraceae_locations.csv`. This file reports where species in the daisy family (Asteraceae) are distributed worldwide. Call `head -n3` to review how the data is structured.

```console
$ head -n3 Asteraceae_locations.csv
LEVEL3_NAM,Level3,LEVEL2_COD,LEVEL1_COD,area_in_m_ESRI_54009,Genus,Species,Genus_Species
Borneo,BOR,42,4,2.13E+12,Abrotanella,nivigena,Abrotanella_nivigena
Borneo,BOR,42,4,2.13E+12,Achillea,alpina,Achillea_alpina
```

The country code for Borneo is BOR. Other country codes ending in "OR" are Korea (KOR) and Portugal (POR). Search for all rows that occur in countries ending in the code OR

```console
$ grep '[A-Z]OR' Asteraceae_locations.csv
# output not shown
```

Use two `grep` calls and the pipe operator to fetch all lines containing the string `KOR`, then return only those lines corresponding to the genus Wedelia. In doing so, instruct `grep` to report the line number (`-n`), adding the option to the first `grep` call, then moving the `-n` flag to the second `grep` call.

```console
$ # use `-n` in first `grep`
$ grep -n 'KOR' Asteraceae_locations.csv | grep Wedelia
42143:Korea,KOR,38,3,2.21E+11,Wedelia,chinensis,Wedelia_chinensis
42144:Korea,KOR,38,3,2.21E+11,Wedelia,prostrata,Wedelia_prostrata
$ # use `-n` in second `grep`
$ grep 'KOR' Asteraceae_locations.csv | grep -n Wedelia
311:Korea,KOR,38,3,2.21E+11,Wedelia,chinensis,Wedelia_chinensis
312:Korea,KOR,38,3,2.21E+11,Wedelia,prostrata,Wedelia_prostrata
```
In the output, the number preceding the colon (`:`) indicates on which line the remaining text was found. Why does this number differ depending on whether `-n` is set as an option in the first or the second `grep`? Are you surprised to see that the line numbers in the second `grep` call are smaller than those in the first?

Using pipes, lets now *sort* all records for species in the genus *Zaluzania* according to their species names, while filtering out individuals in Arizona (ARI) and New Mexico (NWM)

```console
$ grep Zaluzania Asteraceae_locations.csv | grep -v NWM | grep -v ARI | sort -k7,7 -t ","
Mexico Central,MXC,79,7,6.66E+10,Zaluzania,montagnifolia,Zaluzania_montagnifolia
Mexico Gulf,MXG,79,7,7.15E+10,Zaluzania,montagnifolia,Zaluzania_montagnifolia
Mexico Southwest,MXS,79,7,3.31E+11,Zaluzania,montagnifolia,Zaluzania_montagnifolia
Mexico Central,MXC,79,7,6.66E+10,Zaluzania,pringlei,Zaluzania_pringlei
Mexico Central,MXC,79,7,6.66E+10,Zaluzania,triloba,Zaluzania_triloba
Mexico Gulf,MXG,79,7,7.15E+10,Zaluzania,triloba,Zaluzania_triloba
Mexico Northeast,MXE,79,7,8.75E+11,Zaluzania,triloba,Zaluzania_trilob
```

Many file formats, such as those for data tables of comma-separated or tab-delimited values, can be parsed in a predictable way to extract information about table values. The `cut` program allows the user to cut out selected parts of each line of text in a file. A line can be `cut` at a fixed position in the file (e.g. "cut the 4th through 9th characters out of the line") or against a specified delimiter (e.g. "cut the file at each `,` delimiter, and print the 2nd and 3rd fields").

Try cutting out only the region code (field 2), the genus name (field 6), and the species name (field 7) from `Asteraceae_locations.csv`.

```console
$ cut -d "," -f2,6,7 Asteraceae_locations.csv | head -n5
Level3,Genus,Species
BOR,Abrotanella,nivigena
BOR,Achillea,alpina
BOR,Achillea,condensata
BOR,Achillea,squarrosa
```

The `cut` command can also be used in combination with other commands. For example, try calling `sort` against the previous 

```console
$ cut -d "," -f2,6,7 Asteraceae_locations.csv | sort -k2,3 -t "," | tail -n5
CPP,Zyrphelis,microcephala
CPP,Zyrphelis,montana
CPP,Zyrphelis,taxifolia
BLZ,Zyzyxia,lundellii
GUA,Zyzyxia,lundellii
```

Now, call `cut` with `uniq` against the column containing the three-letter region codes:
```console
$ cut -d "," -f2 Asteraceae_locations.csv | uniq | tail -n5
NAM
NAT
OFS
SWZ
TVL
```

Or, using `sort` with `cut`, list all species names in alphabetical order:
```console
$ sort -k9,9 -t "," Asteraceae_locations.csv | cut -d "," -f8 | head -n5
Acanthocephalus_amplexifolius
Acanthocephalus_benthamianus
Achillea_arabica
Achillea_bucharica
Achillea_filipendulina
```

The `tr` command *translates* the input text into output text by substituting and/or deleting characters. Let's print all species name, and translate the character that separates genus and species name in field 8 from `_` to ` `. (No need to call `sort` this time.)
```console
$ cut -d "," -f8 Asteraceae_locations.csv | tr -s "_" " " | tail -n5
Vernonia sutherlandii
Vernonia thodei
Vernonia triflora
Vernonia wollastonii
Zoutpansbergia caerulea
```

When processing text in files, a key step is often to collect the set of target files. The `find` function searches a target directory, and all directories nested within it, for all filesystem objects. Providing a search pattern with the `-name` option directs `find` to only show those file paths that match.

```console
$ find data -name "*0.txt"
data/Saavedra2013/n10.txt
data/Saavedra2013/n40.txt
data/Saavedra2013/n50.txt
data/Saavedra2013/n20.txt
data/Saavedra2013/n30.txt
```

---
## 2. Modifying text-processing pipelines 

Bioinformatics projects tend to rely on a variety of pipeline commands, developed by different researchers to achieve different goals. In this section of the lab, you'll be provided with an assortment of pipeline commands. Your job is to interpret what those pipeline commands do, how to modify the pipeline to fulfill a different objective, and/or how to select a pipeline to perform a desired task.

For each of the three problems below, you will need to produce (1) a file that modifies the behavior of the pipeline, (2) a file containing the output of the modified pipeline, and (3) a file that describes the steps of the modified pipeline, line-by-line. For each assignment, store these three files in the directory `part_2/problem_N`, where `N` corresponds to the problem in Part 3 that you've solved.

For example, an exercise might provide you with the pipeline commands
```
ls *.txt | wc -l > output.txt
```
and ask you to you instead print the number of *characters* for the output of `ls *.txt` to the file `output.txt`.

For the *modified pipeline file*, you will create a file called `pipeline.txt` that specifies how to modify the pipeline command for each problem to produce the desired output, e.g. 
```
ls *.txt | wc -c > output.txt
```

The *output file* in this case would be `output.txt`.

The *description file* (`description.txt`) will explain in simple language what each step in the modified pipeline does, e.g.
```
1. ls *.txt          # list local filesystem objects that match the search pattern *.txt
2. wc -c             # counts number of characters (files) listed in step 1
3. > output.txt      # character count outputted from step 2 redirected into output.txt
```

Finally, move the three files for each exercise in Step 2 into the directory `step_2/problem_N`, where `N` corresponds to exercises 1, 2, and 3.


**Problem 1.** Modify the following command to first sort the data table by the `AdultBodyMass_g` column before sorting by `Family`. (Hint: the command `sort -k4 -k2` would first sort by values in field 4, then subsort those results by values in field 2.)
```
cat data/Pacifici2013_data.csv | cut -d ";" -f2,3,4 | sort -k2 -t ";" | uniq | cut -d ";" -f1,3 > output.txt
```

**Problem 2.** Modify the following command to (1) target the last five characters of each line rather than the first three characters, and (2) to exclude the results associated with the binary strings `00000` and `11111` from the final output.
```
cat data/Saavedra2013/* | tr -d " " | cut -c1,2,3 | sort | uniq -c | sort -r > output.txt
```

**Problem 3.** Modify the following command to instead find all the contig lengths, and to list how many times the 10 shortest contig-lengths appear in the dataset.
```
cat data/Marra2014_data.fasta | grep ">" | tr -s " " | grep -v it_thresh | cut -d " " -f3 | cut -d "=" -f2 | sort | uniq -c | sort -nr | head -n10
```

---
## 3. Writing text-processing pipelines

In this final step for Lab 05, you will write several pipelines that can be used to process a data file. For each pipeline, I will provide a description of what information needs to be extracted from a given input file. Your job is to translate this request into a series of Unix commands to produce the desired output. Similar to the previous example, you will need to submit three files for each problem: a file containing the pipeline command (`pipeline.txt`); a file containing the pipeline output (`output.txt`); and a file providing a line-by-line description of your pipeline command (`description.txt`). For each assignment, store these three files in the directory `part_3/problem_N`, where `N` corresponds to the problem in Part 3 that you've solved.


**Problem 1.** Write a pipeline to extract all of the sequence names from all of the fasta-formatted files in a directory, then print the first 3 characters of each sequence name in alphabetical order and without duplicates. Use the file `data/miRNA` to produce `output.txt`.

**Problem 2.** Write a pipeline to find all `.fasta` files in the local directory or in any of its subdirectories (at any depth), then print only the first part of each filename -- e.g. if a file was found at `data/seq/cytB.fasta`, then the pipeline should only print `cytB`. Find files in the `data` directory to produce `output.txt`.

**Problem 3.** Write a pipeline to retrieve all of the sequence data from a fasta-formatted file, convert all lowercase basepairs to uppercase, convert all basepairs for thymine (T) to the uracil (U), replace each basepair with its base complement, then print the result sequence data. *(Biology note: Each nucleotide has a natural base complement on a DNA [or RNA] molecule. The complement for A is T [or U], for T [or U] is A, for C is G, and for G is C.)* Use the file `data/Marra2014_data.fasta` to produce `output.txt`.


---

## 4. Submit assignment

Push the`part_2` and `part_3` directories and their contents, along with a `history.txt` file, to your GitHub repo for Lab 05 to submit the assignment. As with previous exercises, the `history.txt` file will contain the redirected output from the `history` command.

