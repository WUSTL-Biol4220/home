# Lab 03B

*Lab 03B GitHub Classroom link:* https://classroom.github.com/a/2segectg

Many complex tasks cannot be completed with a single shell command, or even with several commands joined together with pipes. *Shell scripts* are useful in situations that require multiple commands, access to intermediate variables, for-loops, if-statements, mathematical operations, and/or unusual procedures that cannot easily be done with existing programs. In this lab, we will learn how to run, annotate, modify, and create shell scripts.

The major tasks to complete for Lab 03B are
1. Annotating a shell script
2. Complete a shell script
3. Creating a new shell script

To complete this lab, you will need to clone your GitHub Classroom repository for assignment Lab 03B on to your VM. Exercises will process the contents of the cloned repo's `data` directory in various ways.

---

## 1. Annotating a shell script

For each script, annotate what each line of the script does using a comment `#`. After the first line (`#!/bin/bash`) add a comment that gives a brief description of what the script does, what the script expects as input (if anything), and a description and example of the output. Redirect the output for each script to `output.txt` to, simply to show that you have successfully run each script.

**Problem 1.** `part_1/problem_1/run.sh` takes a directory as input. Try calling `./run.sh tmp` to see what the script does.

**Problem 2.** `part_1/problem_2/run.sh` processes the file `data/Gesquiere2011_data.csv`, a file that records hormone levels among blood samples, where some individuals had their blood sampled multiple times.


---

## 2. Complete a shell script

For Part 2 of the lab, you will provided with `run.sh` scripts that contain some of the code needed to solve each problem. Your task is to complete the script for each problem as requested. In addition, provide a description for the script and annotate the scripts in the same manner was required for the Part 1 problems.

**Problem 1.** The file `data/numbers.txt` contains a data table with three columns of integers. Modify the script `/part_2/problem_1/run.sh` to report which value for each row in `data/numbers.txt` is the largest. The output should read
```
27571 is the largest number.
23589 is the largest number.
...
```


**Problem 2.** The data table written to `data/Pacifici2013_data.csv` reports species traits, such as body mass and longevity, for a large number of mammals species. Modify the script `/part_2/problem_2/run.sh` to report the family, the species, and the body mass for the species with the *largest* body mass and the species with the *smallest* body mass within each family. For example, the entries output for Ursidae (the bear family) would be:
```
...
Ursidae;Helarctos malayanus;57075.78
Ursidae;Ursus maritimus;371703.8
...
```
To do this, you'll likely need to apply the `sort` with the `-g` option to compare mass values as floating point numbers during sort. As an optional challenge, how would you report the ratio of the largest-to-smallest body mass per family, then report the family with the largest and smallest ratio?

---

## 3. Creating a new shell script
The Part 3 problems will ask you to write a script to process a dataset. When writing a new script, remember that it helps to (1) first outline the script with pseudocode sketch how you want the script to behave, and (2) to create copies of filesystem objects or to simplify the size/format of a target file so that output is easier to interpret. 

**Problem 1.** Write a script that swaps the the names of two files. For example, if `file1.txt` contained the text `Hello` and `file2.txt` contained the text `world!`, then after calling the script `part_3/problem_1/run.sh`, `file1.txt` would contain the text `world!` and `file2.txt` would contain the text `Hello`. Running the script should not result in any other lasting changes to the filesystem (e.g. new permanent folders and/or files, etc.)

**Problem 2.** The directory `data/Saavedra2013` contains a number of files, where each file reports if a pollinator (row) and an plant (column) interacted, where a 1 indicates an recorded interaction, and 0 indicates no recorded interaction. Write a script (`part_3/problem_2/run.sh`) that finds the number of pollinators and the number of plants for each file, then stores those records the output in the following format
```
/home/mlandis/labs/lab-03b-mlandis/data/Saavedra2013/n9.txt 12 45
/home/mlandis/labs/lab-03b-mlandis/data/Saavedra2013/n8.txt 19 67
/home/mlandis/labs/lab-03b-mlandis/data/Saavedra2013/n7.txt 16 51
...
```

---

## Submit assignment

To submit the assignment, you will need to commit and push
1. a total of six `run.sh` and six `output.txt` files for the problems listed across the three parts. These files should be located at `part_X/problem_Y/run.sh` and `part_X/problem_Y/output.txt` for Part X and Problem Y.
2. the output from `history > history.txt`
