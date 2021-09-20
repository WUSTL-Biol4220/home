# Lab 08

*Lab 08 GitHub Classroom link:* to be provided

This lab will explore three different programs that employ multiple sequence alignment algorithm. Two are [MUSCLE](https://www.drive5.com/muscle/) and  [MAFFT](https://mafft.cbrc.jp/alignment/software/), which are progressive alignment methods. The other is [PRANK](http://wasabiapp.org/software/prank/), a phylogeny-aware alignment method. In this lab, you will install the two programs on your VM, experiment with the programs by running the program under various settings through the command line, then write a script to align a sequence dataset under a set of user-provided program options.

1. Program installation
2. Using alignment programs
3. Writing an alignment script

---

## 1. User-installed programs

For this lab we make use of several multiple sequence alignment programs that are already installed on to your VM. In general, it's important to know where these programs are stored in the filesystem, and how shell knows where to find them.

Your user account on your VM has complete access to modify your user's home directory (i.e. the directory printed by calling `echo $HOME`). While a user can always install programs locally within `$HOME`, they generally cannot install programs in the globally accessible directory of programs (e.g. in `/usr/bin` or `/usr/local/bin`).

For example, type `which ls` to discover exactly which copy of the `ls` program the shell uses when calling `ls` from the command line.

This part of the lab will give you some basic exposure to the local installation of a downloaded program. The program might be shared as source code, in which case it will need to be compiled and built into an executable program, called a *binary*. Alternatively, the program may be shared as a pre-compiled binary.

Once the binary is on your filesystem, the next task is to ensure the binary file itself or a shortcut (*symbolic link*) to the file is located in one of the directories defined in your `PATH`. The `PATH` variable is an environmental variable that is initialized every time you log in to your account. When you type a command, like `ls`, Unix will recognize that command as the first binary discovered in any directories listed in `PATH`. Most Unix systems recognize the directory `~/.local/bin` in `PATH`, which is where we will place copies or links to our alignment programs.

Your operating system should already contain the `~/.local/bin` directory by default. You can use the following command to silently create the directory and all necessary subdirectories if, for some reason, it is missing.
```console
$ mkdir -p ~/.local/bin
```

Because there is a chance that you created this new directory, we need to refresh your *user profile* settings. By default, your profile settings are determined when you log in to a new shell session by loading (or *sourcing*) the settings in the `~/.profile` file. Your profile file customizes your user account, such as how you want the command line interface to appear and behave, how command shortcuts ("aliases") are defined, and what values are assigned to environmental variables. We want the `PATH` variable to contain an entry for our new `~/.local/bin` directory. If you view the last lines of `~/.profile`, you'll see that it adds `~/.local/bin` to `PATH` if `~/.local/bin` exists

To update your `PATH`, you can either log-off then log back on to your user account, or call the command
```
$ source ~/.profile
```

Now, we can begin installing our alignment software. First, we'll install MUSCLE. Create a new directory for the program, then download the installation files.

```console
$ mkdir -p ~/apps/muscle
$ cd ~/apps/muscle
$ wget https://www.drive5.com/muscle/downloads3.8.31/muscle3.8.31_i86linux64.tar.gz
```

Files with the `.tar.gz` extension are archived into a single file (`.tar`) and zipped (`.gz`) as what's colloquially known as a *tarball*. We can unzip and decompress this tarball with the command `tar zxcf <tarball_file>`. In order, the options `zxvf` signify: un**z**ip the file, e**x**tract the files from the archive, print all filenames **v**erbosely, and that the argument is the input **f**ilename.

```console
$ tar zxvf muscle3.8.31_i86linux64.tar.gz
$ ls -lart muscle3.8.31_i86linux64
-rwxr-xr-x 1 mlandis mlandis 1058280 Oct  2 20:17 muscle3.8.31_i86linux64
```

Notice that the unzipped and extracted MUSCLE program permissions already allow it to be executed (`x`).

Next, we'll download the PRANK tarball, which contains the executable binaries for both the PRANK program itself, and for the MAFFT program. These programs can be installed and made accesible following a procedure that's similar to how we installed MUSCLE

```console
$ cd ~/apps
$ wget http://wasabiapp.org/download/prank/prank.linux64.170427.tgz
$ tar zxvf prank.linux64.170427.tgz
$ ls -lart prank/bin/prank
-rwx------ 1 mlandis mlandis 1138736 Jul  3  2017 prank
```

Finally, download and unzip the software for MAFFT
```console
$ cd ~/apps
$ wget https://mafft.cbrc.jp/alignment/software/mafft-7.471-linux.tgz
$ tar zxvf mafft-7.471-linux.tgz
$ ls -lart mafft-linux64/mafft.bat
-rwxr-x--- 1 mlandis mlandis 284 Jul 23  2018 mafft-linux64/mafft.bat
```

We might like to be able to execute these programs, by name, from anywhere in the filesystem. Programs located in any directory listed in the environmental variable called `PATH` can be excuted from anywhere in the filesystem.

```console
$ echo $PATH
/home/mlandis/.local/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin:/home/mlandis/edirect
```

`PATH` directories are separated by the `:` delimiter. In addition, `PATH` directories are explored from left to right when searching for a binary. Notice that the first directory in `PATH` is `/home/mlandis/.local/bin`. That directory is nested inside `HOME` directory, meaning every user can write files in that directory. Local installations of custom software will often involve moving or copying the binary for the program to `~/.local/bin`, or by creating a symbolic link within `~/.local/bin` to the binary.

Let's create links for `muscle` and `prank`
```console
cd ~/.local/bin
$ ln -s ~/apps/muscle/muscle3.8.31_i86linux64 muscle
$ ln -s ~/apps/prank/bin/prank prank
```

Installing MAFFT is more involved, largely because MAFFT requires access to various utilities located in `~/apps/mafft-linux64/mafftdir` to run properly. Rather than creating a symbolic link to the file `~/apps/mafft-linux64/mafft.bat`, we will copy that file and its directory of utilities into the `.local/bin` directory.

```console
$ cp ~/apps/mafft-linux64/mafft.bat ~/.local/bin/mafft
$ cp -R ~/apps/mafft-linux64/mafftdir ~/.local/bin/mafftdir
```

When listing files, symbolic links are identified as `link_name -> actual_link_target` when calling `ls -lart`.  Listing our three new programs in `~/.local/bin` shows that `muscle` and `prank` are symbolic links, while `mafft` is an actual file. In fact, if you open `~/.local/bin/mafft` in `nano`, you'll discover it's a shell script!

```console
$ cd ~/.local/bin
$ ls -lart muscle
lrwxrwxrwx 1 mlandis mlandis 49 Oct  3 10:59 muscle -> /home/mlandis/apps/muscle/muscle3.8.31_i86linux64
$ ls -lart prank
lrwxrwxrwx 1 mlandis mlandis 35 Oct  2 22:02 prank -> /home/mlandis/apps/prank/bin/prank
$ ls -lart mafft
-rwxr-x--- 1 mlandis mlandis 284 Oct  3 11:30 mafft
```

Finally, we will install the program [alv](https://github.com/arvestad/alv) to view sequence alignments in the command line. `alv` is written in Python, and is easily installed using the Python package installer, `pip`
```
$ pip install --upgrade pip
$ pip install alv
```

The program `alan` is another command line tool for viewing multiple sequence alignments. `alan` is written purely with Unix shell commands, meaning we only need to download the shell script and place it in a `PATH` directory to use it anywhere in the filesystem.

```
$ mkdir ~/apps/alan
$ cd ~/apps/alan
$ wget https://raw.githubusercontent.com/mpdunne/alan/master/alan
$ chmod +x alan
$ cd ~/.local/bin
$ ln -s ~/apps/alan/alan alan
```

---

## 2. Using alignment programs

Three sets of sequences are provided for this lab. We will focus on sequences that encode alcohol dehydrogenase (ADH) for highly divergent prokaryotic and eukaryotic species (`adh.fasta`). However, cytochrome B sequences for various turtle species (`testudines_cytB.fasta`) and ITS sequences for members of the Hawaiian silversword alliance (`silverswords_ITS.fasta`) are also available for experimentation. 

To begin, we will align `adh.fasta` using MUSCLE. MUSCLE supports fairly few options, but it is fast.

```
$ muscle -in adh.fasta  -out adh.muscle_it1.fasta -maxiters 1

MUSCLE v3.8.31 by Robert C. Edgar

http://www.drive5.com/muscle
This software is donated to the public domain.
Please cite: Edgar, R.C. Nucleic Acids Res 32(5), 1792-97.

adh 11 seqs, max length 1173, avg  length 1102
00:00:00    10 MB(-2%)  Iter   1  100.00%  K-mer dist pass 1
00:00:00    10 MB(-2%)  Iter   1  100.00%  K-mer dist pass 2
00:00:01    22 MB(-5%)  Iter   1  100.00%  Align node
00:00:01    22 MB(-5%)  Iter   1  100.00%  Root alignment
```

The entire alignment can be viewed in `alv` with the command
```
$ alv -k -w 80 adh.muscle_it1.fasta  | less -R
```
which will call `alv` while preserving color formatting (`-k`) with a screen-width of 80 characters (`-w 80`) then pipe that output into the file-viewing program `less` while using the raw-character flag (`-R`) to display the color codes transmitted by `alv`.

Alternatively, you can call use `alan` to view the alignment as nucleotides (`-n`), where arrow keys allow you to scroll through the alignment
```
$ alan -n adh.muscle_it1.fasta
```

Run MUSCLE again, this time for a maximum of 16 iterations. Increasing the number of iterations improves how likely it is that the resultant alignment is optimal alignment. Be sure to change the output file name so the earlier result is not overwritten.

MAFFT behaves similarly to MUSCLE, but MAFFT provides more features. Notably, the user can impose different gap-open (`--op`) and gap-extension (`--ep`) costs to the alignment algorithm. Run MAFFT under the following conditions.

```
$ mafft adh.fasta > adh.mafft_default.fasta                          # op=1.53, ep= 0.123  (default)
$ mafft --op 5.0 --ep 5.0 adh.fasta > adh.mafft_op5_ep5.fasta        # op=5.0, ep=5.0
$ mafft --op 0.5 --ep 0.5 adh.fasta > adh.mafft_op05_ep05.fasta      # op=0.5, ep=0.5
$ mafft --op 0.0 --ep 0.0 adh.fasta > adh.mafft_op0_ep0.fasta        # op=0.0, ep=0.0
```

What happens when the value of `--op` is small? when it is large? What happens when the value of `--ep` is small? when it is large? What settings would you provide to MAFFT to generate an alignment that with very few, but very large, gaps? for an alignment with very many, but very small gaps?

Finally, we will run the phylogeny-aware alignment tool, PRANK. In contrast to the progressive aligners, MUSCLE and MAFFT, PRANK instead employs evolutionary rules ("tree-thinking") to determine what sequence variation is due to substitution, insertion, or deletion. We will generate alignments manually under several
```
$ prank -d=adh.fasta -o=adh.prank_default                                        # gaprate=0.025 gapext=0.75 (default)
$ prank -gaprate=0.001 -gapext=0.750 -d=adh.fasta -o=adh.prank_open00001_ext075 
$ prank -gaprate=0.025 -gapext=0.950 -d=adh.fasta -o=adh.prank_open0025_ext095
$ prank -gaprate=0.500 -gapext=0.750 -d=adh.fasta -o=adh.prank_open05_ext075
$ prank -gaprate=0.001 -gapext=0.001 -d=adh.fasta -o=adh.prank_open0001_ext0001
prank -iterate= # number of repeated tries
```

Construct a Unix command to measure the number of positions in the alignment. Construct another command to count the number of gaps in the alignment. What is the length of each alignment? How many gaps does each alignment contain?


---


## 3. Writing an alignment script

In this part of the lab, you will be asked to write two scripts that align an unaligned fasta file under a battery user-provided settings. Use `adh.fasta` to test, since alignment programs can take minutes (or hours) to complete when the dataset is large and/or if it contains highly variable sequences that prove difficult to align. 

**Problem 1.** Write a script to align a target dataset using MAFFT, with different gap open and extension costs. The script should accept a fasta file as the first argument and a file with gap-open and gap-extension costs as a second argument: `./align_mafft.sh adh.fasta mafft_costs.txt`

The cost file contains comma separated values, where the first column indicates the (arbitrary) setting ID, second column is the gap-open cost, and the third column is the gap-extension cost

```
$ cat mafft_costs.txt
1,1.53,0.123
2,5.0,5.0
3,0.5,0.5
4,0.0,0.0
```

**Problem 2.** Write a script to align the dataset under various PRANK settings. This script will also accept the fasta file as the first argument, and the cost file as the second argument: : `./align_prank.sh adh.fasta prank_costs.txt`

The PRANK cost file will also be comma-separated, where the first column is the setting ID, the second column is the rate of gap-open events, and the third column is the probability of gap-extension events.

```
$ cat prank_costs.txt
1,0.025,0.75
2,0.0001,0.75
3,0.025,0.95
4,0.5,0.75
5,0.001,0.001
```

**For Problems 1 and 2.** Each script will align the input fasta file once for each the settings in each row of the cost file. For example, if the `./align_prank.sh` script was applied against the input was `seq.fasta`, the script would generate the file `seq.prank_1.fasta` by running PRANK using the settings from the first row of the cost file, `seq.prank_2.fasta` for the second row, etc.

In addition, the scripts should record alignment statistics for each setting under the alignment program, then save those statistics to the file `seq.prank_stats.csv` -- again, assuming the input file was `seq.fasta` and the alignment program was PRANK. This file should contain columns that report the setting ID, the total number of gaps in the alignment, the average number of gaps per sequence (total # gaps / # sequences), and the total alignment length (total # characters / # sequences) for each setting in the costs file.

What settings under MAFFT and what settings under PRANK produce roughly similar numbers of gaps?  Does one program seem to produce "gappier" alignments over a wide range of settings?

**Challenge problem.** Report the mean gap-length per alignment. The mean gap-length can be computed as the total number of gap characters divided by the total number of distinct gaps in a given alignment. How does mean-gap length respond to different MAFFT and PRANK costs?

---

To turn in this assignment, please commit and push the following files to your GitHub assignment repo:
- all `.fasta` files generated in Part 2
- `align_mafft.sh` and `align_prank.sh` from Part 3
- `seq.mafft_stats.csv` and `seq.prank_stats.csv` from Part 3
- a file named `history.txt` that contains the output from the `history` command
