# Lab 05B

*Lab 05B GitHub Classroom link:* https://classroom.github.com/a/V9caiVdr

In the previous lab, we explored how to use the `grep` command with regular expressions to search and print general text patterns found within a text file or stream. Refer to the Lecture 05A for a review on regular expressions for search patterns.

Regular expressions may also be used to *find and replace* content within text files or streams. Among Unix tools, the `sed` command is the simplest, most flexible, and most widely proliferated tool. Lecture 05B provides an overview of how to construct various stream editing commands using `sed`, including find-and-replace commands.

---

## Text processing

This lab will ask you to write several scripts that use `sed` to process text files of with a format.

**Problem 1.** Write the script `problem1.sh` to construct a table of sequence information based on sequence headers in `Marra_2014_data.fasta`. Format the information as comma-separated values
```
$ ./problem1.sh Marra_2014_data.fasta | head -n5
contig,length,numreads,gene,status
00001,527,2,00001,it_thresh
00002,551,8,00001,it_thresh
00003,541,2,00001,it_thresh
00004,291,3,00001,it_thresh
```

The lines that process the text and print output can be written in just two lines, with the first line being a simple `echo` to write the header names, and the second line being a `sed` command to reformat the sequence information.

**Problem 2.** Write a script named `problem2.sh` to extract interesting sequence motifs from `ecoli.fasta`, a fasta-formatted file containing one sequence. For example, task 1 will be to find all lines in which the motif `[GC]ATTACA` occurs. The output for exercise 1 will be formatted as
```
1,82,GATTACA
1,135,GATTACA
1,236,CATTACA
1,336,CATTACA
1,549,GATTACA
```
where the first column gives the task ID (`1`), the second column gives line number containing the pattern, and the third column prints the matched pattern itself.

You can `cat -n` or `grep -n ""` to prefix the line number to each line in `ecoli.fasta`. Use `sed` with regex and group captures to extract useful information (e.g. motifs) from the text, and backreferences to format your output. Note, we will ignore motifs that begin at the end of one line, and continue into the next line.

For the following tasks, report lines that contain 1+ instances of following motifs:

- *Task 1:* Report all instances of the motifs `GATTACA` or `CATTACA`.
- *Task 2:* Report all instances of motifs that are 10 basepairs in length, begin with `AAA` and with `TTT` and contain no `C`s. 
- *Task 3:* Report all instances of motifs that repeat `xA` between 5 and 6 times, and are flanked by the basepair `C` on both sides; only list the repeating region, not the flanking region. For example, `CTATATATATAC` would match, and the printed motif would be `TATATATATA`. The motifs `CGATAGACATAC` and `CTATATATATAG` would not match.
- *Task 4:* Report all lines that begin with `ATG` and end with `TAT`, `GAA`, or `CGA`. However, only print the first and last the nucleotides for the matched line in the output. For example if a line read `ATGCAGTATAGGACCATAGATACAGATATGGTAAGACCGA`, then the printed text for the motif should read `ATGCGA`.

**Problem 3.** Write a script named `problem3.sh` to organize the chapter descriptions in *Origin of Species*. *Origin of Species* can be download from http://www.gutenberg.org/cache/epub/2009/pg2009.txt.

Your script will reformat the descriptions for each Chapter listed after `CONTENTS.` and before `  GLOSSARY OF SCIENTIFIC TERMS.` For example, the original text for the Chapter 2 title (`VARIATION UNDER NATURE.`) and topics (e.g. `Variability`, `Individual Differences`, ...) appear as
```
  CHAPTER II.

  VARIATION UNDER NATURE.

  Variability--Individual Differences--Doubtful species--Wide ranging,
  much diffused, and common species, vary most--Species of the larger
  genera in each country vary more frequently than the species of the
  smaller genera--Many of the species of the larger genera resemble
  varieties in being very closely, but unequally, related to each other,
  and in having restricted ranges.
```
Chapter titles and topics should be reformatted to appear as
```
2. Variation Under Nature
  - Variability
  - Individual Differences
  - Doubtful species
  - Wide ranging, much diffused, and common [...]
  - Species of the larger genera in each cou[...]
  - Many of the species of the larger genera[...]
```
where Chapter 2 would be printed between Chapters 1 and 3 in the output. Number and title each chapter entry. Within each chapter, use two spaces and a hyphen (`  -`) to list chapter topics. Only print the first 40 characters of each topic description. Topics with more than 40 characters will instead be terminated with `[...]` rather than the remaining text.

Consider using `grep -n` in combination with `sed 'a,b p' oos.txt` to extract the raw text describing the chapters in `oos.txt`. Use `tr` to reformat each list of chapter topics into a single line of text, then use `tr` again to split the topics against the `-` delimiter. To truncate the topic descriptions to 40 characters, this can be done with `sed` and backreferences.



---

To submit your lab assignment, please commit and push the scripts `problem1.sh`, `problem2.sh`, `problem3.sh`, and the redirected output of `history > history.txt` to your GitHub assignment repo.
