# Lab 04

*Lab 04 GitHub Classroom link:* https://classroom.github.com/a/1vHHcKtw

This lab will explore how to generate and manipulate character strings in various ways. The lab will also explore how to use the pipe (`|`) and redirect (`>`) commands to link together independent programs.

The major tasks to complete for Lab 04 are
1. Character strings
2. Wildcards
3. More Unix commands
4. Redirects and pipes
5. Submit assignment

---
## 1. Character strings

A sequence of characters is known as a *text string* (or string, for short). Understanding how strings are defined, read, and written is crucial to using shell effectively, because shell commands are sent as text, they accept arguments and options as text, and they generally write output as text (either to screen or to file). Strings in shell, Python, R, C, HTML, etc. share many common properties, meaning they behave in a similar way across a wide range of operating systems and programming languages.

A primary goal of this exericse is to better understand how strings are constructed. Strings are constructed using a pair of `'` or `"` *delimiter* tokens to identify the beginning and end for the content of the string. The content of the string is then evaluated to produce a value for the string, called the *string literal*. In Unix, how string content is evaluated into a string literal varies depending on (1) what text was supplied as content during string construction, (2) what string delimiters were used to delimit the string, and (3) what special characters in the string were *escaped*. For reference, all text content in strings delimited with `'` tokens will be interepreted as-is, i.e. the string literal will equal the text supplied to the string upon construction. Also, an escaped character is a text character that is preceded by the *escape symbol*, which is the backslash `\` on Unix; table of common escape sequences for special characters is below. 

| escape sequence<br>for special character | literal value | special meaning |
| --- | --- | --- |
| `\\` | `\` | escape character |
| `\'` | `'` | single-quote string delimiter |
| `\"` | `"` | double-quote string delimiter |
| `\$` | `$` | shell variable identifier (*we'll learn more about variable soon*) |
| `\n` | *new line* | new line |
| `\t` | *tab-indent* | tab indent |


Let's consider a few examples for how string constructions translate into string literals. For this, we'll use the `echo` command, which accepts a string as input, and prints it to standard output (your screen).

```console
$ echo "Hello, world!"
Hello, world!
```

Next, try printing `Hello, world!` with one word per line:
```console
$ echo "Hello,\nworld!"
Hello,\nworld!
```

Use `echo` with the `-e` option to evaluate escaped characters for their string literals.

```console
$ echo -e "Hello,\nworld!"
Hello,
world!
```

Now try using `echo -e` to print `\` to standard output.
```console
$ echo -e "\"
>
```

This `>` prompt appears when a command is still *open* -- i.e. the command has not been completed or *closed*. In this case, we have opened the string with `"` but the second `"` that usually terminates the string has been escaped as `\"`!

When you see the `>` prompt, you either need to (1) close the call, in this case by providing the rest of the string and the terminal `"` delimiter, or (2) pressing `^C` (ctrl-C) to terminate the open call. It's likely that you'll need to terminate your command while attempting to produce the correct string literal

Section 1 question: **What is the one-line text string that you would construct to produce the string literal output with `echo -e` below?**
```
Special symbols are easy to escape! See?
	\n
	\"
	\'
	\$
```
Note, that lines 2-5 each begin with a tab character, not a series of single-space (` `) characters. This problem can be solved using either double-quotes (`""`) or single-quotes (`''`) to construct the string. Try experimenting with both.

You will likely need to call `echo -e` against several candidate strings to get this right. To get started, try calling
```console
$ echo -e "Special symbols are easy to escape! See?\n'"
Special symbols are easy to escape! See?
'
```

Save the command you used to produce the requested output into a file titled `string_literal.txt`. For example, that file might contain the content
```
echo -e "Special symbols are easy to escape! See?\n\"\'\$'"
```
Commit the `string_literal.txt` file to your repo when complete.

---

## 2. Wildcards

Strings are often used to identify filesytem resources. In many cases like this, the user wants to identify a set of strings that share a common pattern. The wildcard characters useful in these cases. A *wildcard* is used as a placeholder in a search pattern to match any other suitable character(s) during a search. Two wildcards we'll learn about today are `*` and `?`. The `*` character will match zero or more characters of any type, while the `?` character will match exactly one character. Any number of wildcards can appear anywhere in a search pattern: it's your choice. We will learn about other types of wildcards in a future lab on regular expressions.

In this section, you will determine what command would accomplish the specified objectives below.

1. What command lists all files in the current directory that start with `new_` and end with `.txt`?
2. What command moves all files ending with `.zip` into a directory called `text_files`?
3. What command removes all directories (empty and non-empty) containing the text `_old` at the end of their directory names? (Hint: directories have `/` at the end of their path while files do not)
4. What command would you use to list all `.fasta` files within a subdirectory named `data/`

To verify that your command behaves as intended, and that it doesn't have unintended effects, I would recommend creating a test directory with test files to run experiments. The objectives of some of the wildcard commands are *destructive*, meaning that you might want to create a copy of your test directory before accidentally deleting or moving any files!

Save your commands into a file called `wildcards.txt`, where the command for each objective is entered into that corresponding row. For example, if the objective 1 was to remove all files starting with the text `file_`, then `wildcards.txt` should contain the text `rm file_*` on the first line of the file. Objective 2 will be on the second row, and so on.

Commit `wildcards.txt` to your repo when this part of the lab is complete.

---

## 3. More Unix commands

In this section, we'll become familiar with several Unix commands that are useful for text processing. Although you won't need to turn in any specific files for this section, your history file should show that you executed these commands.

But before that, it is good to know how to access the built-in documentation system for Unix-based systems. These are called the manual pages or the *man pages*. Almost every core Unix resources -- including commands, library functions, special files, file formats, etc. -- has its own man page that can be accessed with the `man` command. For example:

```console
$ man ls
LS(1)                            User Commands                           LS(1)

NAME
       ls - list directory contents

SYNOPSIS
       ls [OPTION]... [FILE]...

DESCRIPTION
       List  information  about  the FILEs (the current directory by default).
       Sort entries alphabetically if none of -cftuvSUX nor --sort  is  speci‐
       fied.

       Mandatory  arguments  to  long  options are mandatory for short options
       too.

       -a, --all
              do not ignore entries starting with .
...
```

Each `man` page is written in plain text and follows a standard format with standard sections. This allows users to quickly learn how to apply a command from the comfort of the command line with just a few keystrokes. Of the man page sections: `NAME` identifies the resource; `SYNOPSIS` provides the syntax for usage; `DESCRIPTION` explains what exactly the command does and how its behavior can be modified with options or flags; `EXAMPLES` often contains working examples for how to use a command in a specific context; and `SEE ALSO` suggests related Unix resources that might be of interest.

Man pages are often helpful to learn more about how Unix works, but they are written for a technical audience. Some man pages are not written to be accessible to novice users (or even expert users) -- so don't feel too discouraged if a man page is indeciperhable to you. In those cases, it's often worth referencing online resources, like StackOverflow for help. That said, even if learning to read man pages is challenging, it's worth the investment, as the man pages often provide the most accurate and precise description of what any Unix command does (and doesn't) do. 

What command would you run to learn how the `mv` command worked? And what command would you excute to learn more about the `man` command itself?

Read the `man` page for five commands that you have used before, either inside this course or outside of it.

The *word count* command accepts a file as an argument, and outputs the number of lines, words, and characters that file contains. For example, executing
```console
wc data/Marra2014_data.fasta
    9515   13335  566026 data/Marra2014_data.fasta
```
informs us that the file `data/Marra2014_data.fasta` contains 9515 lines, 13335 words, and 566026 characters. Quite a large file! We might not want to print all of its contents with `cat` or load the entire file into memory to read it with `nano`. Instead, we can peek at the start (or *head*) of the file, using the `head` command

```console
$ head data/Marra2014_data.fasta
>contig00001  length=527  numreads=2  gene=isogroup00001  status=it_thresh
ATCCTAGCTACTCTGGAGACTGAGGATTGAAGTTCAAAGTCAGCTCAAGCAAGAGATTTG
TTTACAATTAACCCACAAAAGGCTGTTACTGAAGGTGTGGCTTAAGTGTCAGAGCAACAG
CTATGAGTGGAGGAATTTTCTATTACAATATAATTTCATCTCTGGTAAATTGACCAATTA
ACTGGAACTTTTTCCAACTGAAATAAATGGTAAACTTTTTATCCACCATTCTGCCATCTG
ACTCACAAAGACCCATGGGAATGGGTGATGAAATCCAACATGCTTCTTTGTAGCAAAAAT
AAATAAAATCCCCAGAAGGGTGAGGTAAATGGAAAACTCCAAACTCGCCCCTCAGGTGGG
TGTAATTTACCCAAGTCTGAGAGGAGGCAGAGTTTTTCCCAATGGACTTTGGTTAAGTGA
GATATGCTGGTCTGTAGAAGGAGGGAGTTCTAGGAAAACAGACACTTAAGTAGGGCCGAA
CTAAAAATTGTATCAGTCAGATCTTCATGTGAAGTCCTGTGTGCCCA
$ head -n2 data/Marra2014_data.fasta
>contig00001  length=527  numreads=2  gene=isogroup00001  status=it_thresh
ATCCTAGCTACTCTGGAGACTGAGGATTGAAGTTCAAAGTCAGCTCAAGCAAGAGATTTG
```

...or we could view the end (or *tail*) of the file with the `tail` command
```console
tail -n5 data/Marra2014_data.fasta
tttgtgtatttgctaattattttttattcctactcatatctgaaggaggaggaacacagg
aatattttgattatagaaatataacctacaagttctgtttattcagttattactccaata
ttttctgacactatctttctgtagatgaaattgattgttattttaaagtaatagaggaaa
atccagtttatatgagccagcagaatgctgtttagaagtctgtttgattcaacacaatcc
taacttgtgcttttgttcttcaggatatggttaatagaagaattg
```

To identify any differences between two files, use the `diff` command
```console
$  diff data/Marra2014_data.fasta data/Marra2014_data_with_errors.fasta
593c593
< gcactgcaccgccagccattccttcaacacagatgatgccctcgtcctctgctttgtgag
---
> gcactgcaccg_A_SUSPICIOUS_ERROR_caacacagatgagtcctctgctttgtgag
1023a1024
> gctgaaggggtagatgagagccaccatggcatggcagcacttggacagggtgctgagctt
1277d1277
< TGGAATGCGGAGACGGCTTCTGTGGCTTTGGCAAAATCAGCAATTCTCTTCTAAAATGGA
```

Differences between the two files are reported in blocks of text beginning with the involved line numbers and the nature of the difference. The first block above (`593c593`) pertains to line 593 and involved a change (`c`) in text; the following three lines indicate the text for the first file (`<`) relative to (`---`) the text for the second file (`>`) -- and indeed, there seems to be a suspicious error. The next block indicates added text (`a`) inserted into line 1023 in the first file or 1024 in the second file, where that new line matches the text from the line that follows (`>`). Finally, line 1277 was deleted in the first text file, with content matching that in following line (`<`).

We'll learn more advanced uses for `grep` (*get regular expression pattern*). For now, we'll use it as a simple tool that accepts text as input, and only prints out lines that match a particular search pattern as output. Suppose we instead wanted to verify whether `data/Marra2014_data.fasta` and `data/Marra2014_data.fasta` indeed contained the text `ERROR` using a different program:
```console
$ grep ERROR data/Marra2014_data.fasta
$ grep ERROR data/Marra2014_data_with_errors.fasta
gcactgcaccg_A_SUSPICIOUS_ERROR_caacacagatgagtcctctgctttgtgag
```
You can expand the *context* of the search with the `-C` option. To search for `ERROR` and return the two lines before and after any match:
```console
$ grep -C2 ERROR data/Marra2014_data_with_errors.fasta
atgggaatttcccaattttgtactcaataccctcttccttcaactgctcttctgatttgc
caacccaggcaacttccggatgtgtgtaaatcactgatggcacacagttgtagtcgatgt
gcactgcaccg_A_SUSPICIOUS_ERROR_caacacagatgagtcctctgctttgtgag
ccagcattggaccagcgaccacatcaccaatagcatagatatttggaattttggtttgga
atctgctattcactggaattctacctctgggatctagttcaattccaagctcttctagtc
```

Another use of `grep` might be to list all instances of a genetic motif within a file, while also printing the line numbers (`-n`) for any matches:

```console
$ grep -n gattaca data/Marra2014_data.fasta
574:Accaacaacaaaaatcttaggattacaaatacaagatacagccttataaaataataaata
1003:ccttagatctcagcctcctgagtggctaggattacaggCATGAGCCATCGGCgCCCGGCT
1515:ctaagagaaatttatcatagattacattttaaataattctttattatagcaggggcatta
3693:ATCTAAaCTCAAGATCCTCcTAtCTCAGgTTcttaaggggctgggattacaaactgagcc
5281:aaatcttatgaccgtcaaggaaatagggtgcagagcaattaaaacttgcctaagattaca
5289:ctttgggattacacacagttagtgtg
6018:ggctatggcacctcagggagctcccacaaaatctattaacatttcagattacagtccata
```

Finally, you might choose to *invert* (`-v`) the search, and only print lines that fail to satisfy the match pattern. To keep the example output short, let's use a version of `data/Marra2014_data.fasta` that contains only the first sequence entry.

```console
$ head -n5 Marra2014_data_n1.fasta
>contig00001  length=527  numreads=2  gene=isogroup00001  status=it_thresh
ATCCTAGCTACTCTGGAGACTGAGGATTGAAGTTCAAAGTCAGCTCAAGCAAGAGATTTG
TTTACAATTAACCCACAAAAGGCTGTTACTGAAGGTGTGGCTTAAGTGTCAGAGCAACAG
CTATGAGTGGAGGAATTTTCTATTACAATATAATTTCATCTCTGGTAAATTGACCAATTA
ACTGGAACTTTTTCCAACTGAAATAAATGGTAAACTTTTTATCCACCATTCTGCCATCTG
$ grep -v "A" Marra2014_data_n1.fasta
>contig00001  length=527  numreads=2  gene=isogroup00001  status=it_thresh
```

---


## 4. Redirects and pipes

Many Unix programs print their output directly to the screen (stdout). Instead, a user may want to store a program's output directly to a file. This can be done easily with the redirection operator (or the *redirect*). When calling a program, a direct can be used to use a file in place of the default stdout (e.g. the screen) or stdin (e.g. typed command line text). This allows files to serve as links between programs, thus redirects are a fundamental part of constructing Unix pipelines.

There are three flavors of redirects: the *output* redirect (`>`), the *append* redirect (`>>`), and the *input* redirect (`<`). The output redirect and append redirects are used frequently, while the input redirect has a a reduce role in regular computing exercises.

The output redirect (`>`) simply sends all output from an executed command to the specified file rather than printing it to screen.

```console
$ echo "Hello, world!" > output.txt
$ cat output.txt
"Hello, world!
$ grep -v "A" data/Marra2014_data_n1.fasta > invert_grep.txt
$ cat invert_grep.txt
>contig00001  length=527  numreads=2  gene=isogroup00001  status=it_thresh
```

Any file targeted as a destination by `>` will be *overwritten* by the newly redirected output. This means output redirect, if used carelessly, can result in unintended data loss!

The append redirect (`>>`) is behaves similarly to `>`, in that they both write program output to a file. Rather than overwriting any existing files, `>>` instead appends the new program output to the target file. Tasks that need to create sequential records of output often make use of `>>` when storing results to file.


```console
$ echo "upstairs" > house.txt
$ echo "downstairs" >> house.txt
$ echo "cellar" >> house.txt
$ cat house.txt
upstairs
downstairs
cellar
```

Finally, the input redirect (`>`) sends a file as the argument for a target program. In the following example, we send `house.txt` as the argument for a `grep` search for the `stairs` pattern

```console
$ grep stairs < house.txt
upstairs
downstairs
```

This is command would be equivalent to calling `grep stairs house.txt`, which is part of why the input redirect is rarely used in practice. Input and output redirects can be combined. In the following example, first `houst.txt` is redirected into `grep stairs` as input, then the output of `grep stairs` is redirected into `above_ground.txt`.

```console
$ grep stairs < house.txt > above_ground.txt
$ cat above_ground.txt
upstairs
downstairs
```

Rather than storing a program's input to file, a user might instead want to treat the output of one program as the input of a second program. This can be done with the *pipe* operator (`|`). Pipes take the output of the command on the left, and pass it as input to the command on the right. Additionally, several commands can be piped together, or combined with redirects -- e.g. `command1 | command2 | command3 > output.txt`.

For example, if we call the command `ls data` by itself, it will list the contents in the `data` directory. However, if we pipe that content into a second command, `wc -w`, which prints the number of *words* in its input file, the `wc -w` command will treat the output of `ls data` as its input.

```console
$ ls data
Buzzard2015_about.txt            Gesquiere2011_data.csv           Marra2014_data_n1.fasta          Pacifici2013_data.csv            invert_grep.txt
Buzzard2015_data.csv             Marra2014_about.txt              Marra2014_data_with_errors.fasta Saavedra2013                     miRNA
Gesquiere2011_about.txt          Marra2014_data.fasta             Pacifici2013_about.txt           Saavedra2013_about.txt
$ ls data | wc -w
      14
```

The output of these piped commands could be redirected into a file, for later consideration.

```console
$ ls data | wc -w > num_data_files.txt
$ cat num_data_files.txt
      14
```

The last part of this lab will require you to construct three command pipelines.

1. Write a pipeline to find all rows in `data/Pacifici2013_data.csv` for species belonging to `Primates`, but are *not* in the groups `Hominidae` or `Lemuridae`, then print those rows to the file `output/only_some_primates.txt`.
2. Write a pipeline to extract all lines in `data/Marra2014_data.fasta` that contain the string `GATTACA`, then write only lines 21 through 25 for the matched lines to the file `output/matches_21_to_25.txt`
3. The directory `data/Saavedra2013` contains 59 text files describing network relationships for a network property called nestedness. A value of `1` in any file indicates an interaction between the entity represented by each row, and the entity represented by each column. Scan all files in `data/Saavedra2013`, find all lines that contain four consecutive interactions (`1 1 1 1`) as its largest interaction-set, and save the count of such lines to the file `output/count_max4.txt`

Save the three commands into a file called `pipelines.txt`.

---

# 5. Submit assignment

Several files must be present in your GitHub repository to submit your assignment
1. `string_literal.txt` (Section 1)
2. `wildcards.txt` (Section 2)
3. `pipelines.txt` (Section 4)
4. the `output` directory and the three output products (Section 4)
5. a `history.txt` file that contains the redirected (`>`) the output of the `history` command



