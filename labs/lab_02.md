
# Lab 02

*Lab 02 GitHub Classroom link:* [https://classroom.github.com/a/vFiNOEUv](https://classroom.github.com/a/p3M3nBA3)

In this lab, we'll familiarize ourselves with the Unix command line interface (CLI) and filesystem.

The major tasks to complete for Lab 02 are
1. [Commands, options, and arguments](https://github.com/WUSTL-Biol4220/home_staging/blob/main/labs/lab_02.md#1-commands-options-and-arguments)
2. [Working with the filesystem](https://github.com/WUSTL-Biol4220/home_staging/blob/main/labs/lab_02.md#2-working-with-the-filesystem)
3. [Command line tricks](https://github.com/WUSTL-Biol4220/home_staging/blob/main/labs/lab_02.md#3-command-line-tricks)
4. [Save your work to GitHub](https://github.com/WUSTL-Biol4220/home_staging/blob/main/labs/lab_02.md#4-submit-your-work)

If you don't remember how to perform specific tasks for any of these steps, review the materials in [Lab 01](https://github.com/WUSTL-Biol4220/home/blob/main/labs/lab_01.md) and in the ["How To"](https://github.com/WUSTL-Biol4220/home/blob/main/how_to_guide.md) guide.


---
## 1. Commands, options, and arguments

In this section, we'll learn how to use several basic Unix commands.

To begin, SSH into your VPN. You'll be greeted by the command line prompt
```console
mlandis@biol4220-mlandis:~$
```
The command line tells you who are you (`mlandis`), what computer you've logged in to (`biol-4220-mlandis`), and what directory you're currently located in (`~`). At first, `~` may not look like a directory, but it is in fact a Linux "shortcut" or alias for your user account's home directory. Most daily activities only involve manipulating files that are located within that home directory.

As we apply various Unix commands, we'll eventually be moving into new folders throughout the filesystem. At some point, you may get lost. Two commands can help you return to a familiar part of the filesystem.

First, let's learn where you are in the filesystem with the *print working directory* command, `pwd`

```console
mlandis@biol4220-mlandis:~$ pwd
/home/mlandis
```

To *list* the contents of the directory, call the `ls` command
```console
mlandis@biol4220-mlandis:~$ ls
mlandis@biol4220-mlandis:~$
```

Nothing was printed because your directory has no visible contents. Let's create a new directory, called `labs`, which we'll use to store the labs for the course. We'll *make a directory* with the `mkdir` command
```console
mlandis@biol4220-mlandis:~$ mkdir labs
mlandis@biol4220-mlandis:~$ ls
labs
```

Whereas the `ls` and `pwd` commands can be executed successfully without any additional text, the `mkdir` command requires that you provide the name of the new directory to create; put another way, `mkdir` is a command that expects an argument. As we'll see, the ability for commands to take a variety of text-based arguments is what make Unix so versatile.

To enter the newly created `labs` directory, use the *change directories* command, `cd`, while providing the `labs` directory as an argument
```console
mlandis@biol4220-mlandis:~$ cd labs
mlandis@biol4220-mlandis:~/labs$
```

Notice that the command prompt now lists `~/labs` as your current directory. Now, let's return to the home directory.

```console
mlandis@biol4220-mlandis:~/labs$ cd ~
mlandis@biol4220-mlandis:~$
```
No matter where you are on the filesystem, `cd ~` will always take you home.

Now, let's create a file called `readme.txt` to explain the purpose of the `labs/` folder. To create this file, we'll combine multiple commands. First, we will use the text editing program, Nano, to create a new file called `readme.txt`. Run the command

```console
mlandis@biol4220-mlandis:~$ nano readme.txt
```
to open the Nano editor. You can edit text documents in Nano simply by typing into the console. Add the text to the effect of
```
This directory contains the lab assignments for Practical Bioinformatics (Biol 4220).
```

<img src="https://raw.githubusercontent.com/WUSTL-Biol4220/home/main/assets/lab_02/nano1.png" width="350"/>

Once you've entered this text, press `^X` (ctrl-X) on the keyboard to Exit Nano.

<img src="https://raw.githubusercontent.com/WUSTL-Biol4220/home/main/assets/lab_02/nano2.png" width="350"/>

Before exiting, Nano will ask if you would like to `Save modified buffer?`, which refers to the text you added. Press `Y` to confirm the save.

<img src="https://raw.githubusercontent.com/WUSTL-Biol4220/home/main/assets/lab_02/nano3.png" width="350"/>

When Nano asks `File Name to Write`, press Enter to keep the default name `readme.txt`. Once saved, you will return to the command prompt.

You can view the contents of one (or multiple) file(s) using the *concatenate* command, `cat`. Execute `cat` with `readme.txt` as an argument
```console
mlandis@biol4220-mlandis:~$ cat readme.txt
This directory contains the lab assignments for Practical Bioinformatics (Biol 4220).
```

Now, let's *move* the `readme.txt` file into our `labs` directory with the `mv` command.

```console
mlandis@biol4220-mlandis:~$ ls
labs  readme.txt
mlandis@biol4220-mlandis:~$ mv readme.txt labs
mlandis@biol4220-mlandis:~$ cat readme.txt
cat: readme.txt: No such file or directory
mlandis@biol4220-mlandis:~$ ls
labs
mlandis@biol4220-mlandis:~$ ls labs
readme.txt
mlandis@biol4220-mlandis:~$ cat labs/readme.txt
This directory contains the lab assignments for Practical Bioinformatics (Biol 4220).
```

The `readme.txt` file, and the content we saved to the file through Nano, is now located in `~/labs` rather than in `~`.

Suppose we wanted to edit `~/labs/readme.txt` but didn't want to risk losing our original file content. A common technique is to create a *copy* of the original file using the `cp` command, edit the original file, then delete the copy once we decide we're happy with the changes.

```console
mlandis@biol4220-mlandis:~$ cd labs
mlandis@biol4220-mlandis:~/labs$ cp readme.txt readme.txt.bak
mlandis@biol4220-mlandis:~/labs$ ls
readme.txt  readme.txt.bak
```
By adding the text `.bak` to the end of the filename, we are indicating that this file is a backup, and not a working copy. Changing the file extension (e.g. from `.txt.` to `.bak`) does not change the contents of the file; that is, file extensions might communicate something to the *user*, but they are indistinguishable from the rest of the file name to the *computer*.

```console
mlandis@biol4220-mlandis:~/labs$ nano readme.txt

# ... here I've used nano to change and save the contents of readme.txt

mlandis@biol4220-mlandis:~/labs$ cat readme.txt
Computers have no place in biology!
mlandis@biol4220-mlandis:~/labs$ cat readme.txt.bak
This directory contains the lab assignments for Practical Bioinformatics (Biol 4220).
```

Suppose you now wanted to restore the original content of `readme.txt`. The `mv` command not only allows you to move files between folders, but it allows you rename the newly moved file. A moved file will overwrite any file at its destination that shares its name. 

```console
mlandis@biol4220-mlandis:~/labs$ mv readme.txt.bak readme.txt
mlandis@biol4220-mlandis:~/labs$ cat readme.txt
This directory contains the lab assignments for Practical Bioinformatics (Biol 4220).
```

The `readme.txt` file is not so important, after all, so let's *remove* it

```console
mlandis@biol4220-mlandis:~/labs$ rm readme.txt
mlandis@biol4220-mlandis:~/labs$ ls readme.txt
ls: cannot access 'readme.txt': No such file or directory
```

Now, return to the home directory, which contains the now-empty `labs` subdirectory
```console
mlandis@biol4220-mlandis:~/labs$ cd ~
mlandis@biol4220-mlandis:~$ ls
labs
```

This concludes Part 1 of Lab 02.


---

## 2. Working with the filesystem

We'll learn more about manipulating filesystems here. For this part of the lecture, we will create a 

Enter the `labs` directory, make a directory called `lab_02`, and enter the directory.

```console
mlandis@biol4220-mlandis:~$ cd labs
mlandis@biol4220-mlandis:~/labs$ mkdir lab_02
mlandis@biol4220-mlandis:~/labs$ cd lab_02
mlandis@biol4220-mlandis:~/labs/lab_02$ pwd
/home/mlandis/labs/lab_02
```

As an aside, it is possible to run multiple commands in a single line by separating each command by the `;` character. For example, let's return to the home directory, print the working directory, then re-enter the `labs/lab_02` directory.

```console
mlandis@biol4220-mlandis:~/labs/lab_02$ cd ~;pwd;cd labs;cd lab_02
/home/mlandis
mlandis@biol4220-mlandis:~/labs/lab_02$
```

Now, let's create an empty file called `output.txt` with the `touch` command. The `touch` command will (1) update the "last accessed" and "last modified" times for a file if the targeted file exists or (2) create a new file with the name of the target file if no such file exists.

```console
mlandis@biol4220-mlandis:~/labs/lab_02$ touch output.txt
```

we can see the file
```console
mlandis@biol4220-mlandis:~/labs/lab_02$ ls
output.txt
```

but it contains no text
```console
mlandis@biol4220-mlandis:~/labs/lab_02$ cat output.txt
mlandis@biol4220-mlandis:~/labs/lab_02$
```

Let's create a second file called, `.hidden.txt`

```console
mlandis@biol4220-mlandis:~/labs/lab_02$ touch .hidden.txt
```

Now list the contents of the directory
```console
mlandis@biol4220-mlandis:~/labs/lab_02$ ls
output.txt
```

Files and folders that begin with the `.` are considered *hidden* filesystem objects. Hidden files and folders behave as normal, but they don't appear during standard `ls` calls. Filesystem objects are typically hidden because those objects contain important information for running programs, but users are not expected to tinker with the contents of those files and folders on a regular basis.

To display `.hidden.txt` in a `ls` call, we can provide the `-a` option to list *all contents*
```console
mlandis@biol4220-mlandis:~/labs/lab_02$ ls -a
.  ..  .hidden.txt  output.txt
```

Now we see two items that we expected to see (`output.txt` and `.hidden.txt`) and two items we might not have expected to see (`.` and `..`). The `.` and `..` items are special hidden directories. The `.` folder always refers to the currently occupied directory, while `..` refers to the parent directory of the current directory. Of the two, the `..` has more daily usefulness. The `.` and `..` directories exist in every directory in the filesystem, except for the root directory, `/`, which does not contain the `..` parent directory, since `/` has no parents. 

For example, we can go "up" in the directory structure, into the parent directory, by using `cd ..`

```console
mlandis@biol4220-mlandis:~/labs/lab_02$ pwd
/home/mlandis/labs/lab_02
mlandis@biol4220-mlandis:~/labs/lab_02$ cd ..
mlandis@biol4220-mlandis:~/labs$ cd ..
mlandis@biol4220-mlandis:~$ pwd
/home/mlandis
```

When you go the "down" in the directory structure, towards child folders, you can change multiple folders at a time.

```console
mlandis@biol4220-mlandis:~$ cd labs/lab_02/
mlandis@biol4220-mlandis:~/labs/lab_02$
```

However, if *any* of the directories in a longer filepath do not exist, you the error message won't tell you *which* directory is missing

```console
mlandis@biol4220-mlandis:~/labs/lab_02$ cd ~
mlandis@biol4220-mlandis:~$ cd yabs/yab_02
-bash: cd: yabs/yab_02: No such file or directory
mlandis@biol4220-mlandis:~$ cd labs/yab_02
-bash: cd: labs/yab_02: No such file or directory
```

Just as you can change into directories with `cd` that are far from your current directory, you can also modify, copy, and move distant files by providing the relative location of the file to your current location
```console
mlandis@biol4220-mlandis:~$ cp labs/lab_02/output.txt labs/lab_02/output.txt.bak
mlandis@biol4220-mlandis:~$ ls labs/lab_02
output.txt  output.txt.bak
```

In this case, the directory `labs/lab_02` is called the *relative filepath*, since it refers to `labs/lab_02` directories that exist in your current working directory (`~`). The command `cp labs/lab_02/output.txt labs/lab_02/output.txt.bak` will generate an error if issued from within a different directory

```console
mlandis@biol4220-mlandis:~$ cd labs
mlandis@biol4220-mlandis:~/labs$ cp labs/lab_02/output.txt labs/lab_02/output.txt.bak
cp: cannot stat 'labs/lab_02/output.txt': No such file or directory
```

If you want a command to target particular file or folder, no matter where you execute the command, you must use the *absolute filepath* for the target. An absolute filepath will begin with the `/` symbol, which represents the root directory of the entire filesystem.

```console
mlandis@biol4220-mlandis:~/labs$ rm labs/lab_02/output.txt.bak
rm: cannot remove 'labs/lab_02/output.txt.bak': No such file or directory
mlandis@biol4220-mlandis:~/labs$ rm /home/mlandis/labs/lab_02/output.txt.bak
mlandis@biol4220-mlandis:~/labs$ ls /home/mlandis/labs/lab_02
output.txt
```

Where do you think you would be located if you called `cd ../..` from the directory `~/labs`?

Let's return to the home directory and erase the `lab_02` directory.

```console
mlandis@biol4220-mlandis:~/labs$ cd ~
mlandis@biol4220-mlandis:~$ rmdir labs/lab_02
rmdir: failed to remove 'labs/lab_02': Directory not empty
```

When deleting a non-empty directory, there are two options: (1) you can manually delete the contents of the soon-to-be-deleted directory, then use the `rmdir` command against that directory, but this can be a tedious task when the target directory is full of multiple levels of other non-empty directories; or (2) you can use the more powerful and general, but dangerous, remove command (`rm`) with special options to apply `rm` recursively (`-r`) to all subdirectories. When `rm -r` encounters a non-empty subdirectory, it will ask for user confirmation to delete that directory. Users who are absolutely sure they know what they are doing will often call `rm -rf` to delete a directory and all its contents recursively and to *force* those deletions to occur without user confirmation.

Now, let's very carefully apply `rm -rf`

```console
rm -rf labs/lab_02
```

You can imagine how dangerous it would be to apply `rm -rf` to the wrong folder system accidentally; that folder would be wiped from your hard drive! Here, it's important to note that Linux does not have a "recycling bin" or "trash can" like Mac OS X or Windows machines. When a file is deleted, it is generally gone for good, and can only be recovered by retrieving the file from an external backup system.

That's all for now.

---

## 3. Command line tricks

Linux is often operated by sending commands entirely through the command line, rather than through a graphical user interface (GUI), as is done with Windows or Mac OS X. Because of the emphasis Unix-based operating systems offer many "tricks" to improve the command line experience.

One extremely useful trick is *tab autocomplete*. Pressing tab will cause Linux to suggest ways to complete whatever text you are typing. Tab autocompletion not only reduces the number of keystrokes needed to execute commands, it also eliminates any possibility of mistyping or misspelling filesystem objects.

To see how tab autocomplete works, type the following commands, but press the "Tab" key when `<TAB>` is written in the code block
```console
mlandis@biol4220-mlandis:~$ ls /h<TAB>
mlandis@biol4220-mlandis:~$ ls /home/<TAB><TAB>
mlandis/  technoid/ testuser/
mlandis@biol4220-mlandis:~$ ls /home/m<TAB>
mlandis@biol4220-mlandis:~$ ls /home/mlandis/
labs
```
(Here, I entered `m` because it's the first character in my username, `mlandis`.)

Notice how pressing `<TAB>` once will complete the text automatically, if there's only one unambiguous way to complete it. When it is ambiguous, pressing `<TAB>` twice will list all possible options. At that point, you must enter a long-enough and distinct string of characters to yield an unambiguous completion for `<TAB>` to complete your text.

Another useful keystroke is the cancel command, issued by pressing `^C` (ctrl-C). Cancel has two important roles. One, it will wipe clean any text written laying unexecuted in your command prompt (an *open command*) to save you the effort of manually deleting that text with the backspace key. Cancel will also terminate "active" foreground jobs that control the screen; we'll learn more about this second role in future labs.

```console
mlandis@biol4220-mlandis:~$ ls /home/ml^C
mlandis@biol4220-mlandis:~$
```

Sometimes you don't want to completely erase a command, but instead want to modify it. The left-arrow and right-arrow keys can be used to move the cursor, and modify it. The shortcuts to go to the start of the command (`^A`) or to the end of the command (`^E`) are both helpful for rapidly jumping to different positions in the command.

```console
mlandis@biol4220-mlandis:~$ ls /home/ml^A
                            ^--- cursor moves here
mlandis@biol4220-mlandis:~$ cd /home/ml
                            ^--- delete ls, add cd
mlandis@biol4220-mlandis:~$ cd /home/ml<TAB>
mlandis@biol4220-mlandis:~$ cd /home/mlandis/^E
                                             ^--- cursor moves here
mlandis@biol4220-mlandis:~$ cd /home/mlandis/labs
mlandis@biol4220-mlandis:~/labs$
```

In some cases, you may want to retrieve an earlier command to re-run it, perhaps with a few modifications. The up-arrow will begin searching through recently issued commands, in order of most recent to least recent. Pressing down-arrow will cycle through commands in the opposite direction.

```console
mlandis@biol4220-mlandis:~/labs$ <up-arrow>
mlandis@biol4220-mlandis:~/labs$ cd /home/mlandis/labs
                                 ^--- text appears in command line
mlandis@biol4220-mlandis:~/labs$ cd /home/mlandis/labs^C
                                                      ^--- clears command line text
mlandis@biol4220-mlandis:~/labs$ cd ~                                                      
```

The up-arrow and down-arrow commands are in fact searching through a special file, known as your user *history*. By default, Linux records the sequence of all commands issued by a user into a history file. To view your history

```console
mlandis@biol4220-mlandis:~$ history

(only the final 10 lines shown)

  467  ls
  468  rm -rf lab_02/
  469  s
  470  ls
  471  cd ..
  472  ls
  473  ls /home/mlandis/
  474  cd /home/mlandis/labs
  475  history
  476  cd ~
  477  history
```

Notice that the `history` output contains a column of numbers, followed by a column of commands. Earlier commands can be re-sent in a variety of ways, using the `!` command.

Calling `!!` will re-execute the last command
```console
mlandis@biol4220-mlandis:~$ cd labs
mlandis@biol4220-mlandis:~/labs$ !!
cd labs
-bash: cd: labs: No such file or directory
```

You can also re-send specific commands either based on relative position in history (e.g. `!-6` to call the sixth-to-last command) or absolute position in history (e.g. `!31` to call the command numbered `31` by `history`). Finally, calling `!mv` will execute the last command that began with the text `mv`.

Where is the actual log for the content of `history` stored? Every time a command is issued from the command prompt, whether it succeeds or not, that command is stored into the history log. Typically, the history log is stored as a hidden file in the user's home directory, called `~/.bash_history`.

---

## 4. Submit your work

To complete Lab 02, you will upload an excerpt of `history` output to GitHub.

From the command line on your VM, call the `history` command. Through your SSH terminal on your personal computer, highlight and copy the text that was printed to the screen. Then, paste the text into a text editor, then save that text to a file called `history.txt` on your personal computer.

Accept your GitHub Classroom assignment for Lab 02 using the link at the top of these instructions. Navigate to your newly created Lab 02 repo, then add and save your local copy of `history.txt` to the repo, as you did with `output.txt` in Lab 01. Once you have saved (committed) the `history.txt` file to the Lab 02 repo, you should see a green checkmark at the top of your repo page.

Transferring information from your virtual machine to your person computer in this way may feel "hacky" to you -- because it is! Beginning with the next lab, we'll begin to use `git` to update and share files in a far more elegant manner.
