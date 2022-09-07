# Lab 03

*Lab 03 GitHub Classroom link:* https://classroom.github.com/a/lMbCKZZR

In this lab, we'll learn the basics for using the version control software, `git`, and how to use `git` with [GitHub](https://github.com). Using `git` to manage your code or other projects becomes natural with practice, but it can feel complicated or overwhelming when you first begin to use the tool. If you are nervous about how to use a certain command, you can always create a "test example" like what we'll use below to understand how the commands work in a safe environment. The other good news is that, generally, `git` itself does not forget the versioned history of files its watching; that means that even if you do make a mistake, it's almost certain that you can recover from a previously saved version. That's the beauty of version control.

The major tasks to complete for Lab 03 are
1. Exploring `git` basics
2. Working within a single branch
3. Working with multiple branches

**Important.** To complete this lab and all future labs, you will need to generate an SSH key for your VM and associate that key with your GitHub account. Instructions for this can be found here: [link](https://github.com/WUSTL-Biol4220/home/blob/main/how_to_guide.md#add-ssh-key-to-github-account).

<!--
You will need to create a Personal Authentication Token (PAT) to complete this lab. Instructions to do so are here: [link](https://github.com/WUSTL-Biol4220/home/blob/main/how_to_guide.md#create-a-github-personal-authentication-token-pat).
-->

---

## 1. Clone your Lab 01 repo to your VM

Enter your Lab 01 repo hosted at https://github.com/WUSTL-Biol4220. For example, the repo for Lab 01 for my user account (`mlandis`) is located at https://github.com/WUSTL-Biol4220/lab-01-mlandis.

<img src="https://github.com/WUSTL-Biol4220/home/raw/main/assets/lab_03/clone_01.png" width="350"/>

Click on the green "Code" button, which will present you with three options to acquire the code. We'll use the top option to "Clone" or copy the repository to our VM using the `git clone` command. 

Select "SSH" as the clone option. By using SSH to clone a GitHub project, you will not need to enter your GitHub username and password for standard `git` commands, such as `push` and `pull`. Instead, GitHub authenticates your access using your VM's SSH key (see [link](https://github.com/WUSTL-Biol4220/home/blob/main/how_to_guide.md#add-ssh-key-to-github-account)). Using SSH also avoids the need to configure other complicated authentication schemes -- e.g. two factor authentication or personalized authentication tokens.

Copy the SSH link to your clipboard. For example, my SSH link is `git@github.com:WUSTL-Biol4220/lab-01-mlandis.git`.

Log into your VM and change directories to `~/labs`; we'll store all course lab work in this directory from now own. From here, we'll instruct `git` to `clone` (copy) the repository hosted at `git@github.com:WUSTL-Biol4220/lab-01-mlandis.git`.

```console
mlandis@biol4220-mlandis:~/labs$ git clone git@github.com:WUSTL-Biol4220/lab-01-mlandis.git
Cloning into 'lab-01-mlandis'...
remote: Enumerating objects: 15, done.
remote: Counting objects: 100% (15/15), done.
remote: Compressing objects: 100% (9/9), done.
remote: Total 15 (delta 0), reused 3 (delta 0), pack-reused 0
Receiving objects: 100% (15/15), done.
```

And we see that all files and folders from Lab 01 on GitHub are now in our VM filesystem!
```console
mlandis@biol4220-mlandis:~/labs$ ls
lab-01-mlandis
mlandis@biol4220-mlandis:~/labs$ ls lab-01-mlandis/
output.txt
mlandis@biol4220-mlandis:~/labs$ cat lab-01-mlandis/output.txt
Hello, world!
```

Call `git status` to learn whether any files in your local repo contain changes that are absent in GitHub's copy of the repo

```console
mlandis@biol4220-mlandis:~/labs$ cd lab-01-mlandis
mlandis@biol4220-mlandis:~/labs/lab-01-mlandis$ git status
On branch main
Your branch is up to date with 'origin/main'.

nothing to commit, working tree clean
```

The command tells us which local branch we're using (`main`) and that our local branch contains no differences compared to GitHub's copy of the branch (`origin/main`). Quite expected, since we just copied our repo from GitHub!

Let's add a new file to our repository

```console
mlandis@biol4220-mlandis:~/labs$ cd lab-01-mlandis/
mlandis@biol4220-mlandis:~/labs/lab-01-mlandis$ nano more_output.txt

  ... add some text, then save and exit with ^X
  
mlandis@biol4220-mlandis:~/labs/lab-01-mlandis$ cat more_output.txt
Hey, world, what's going on with you?
```

Call the `git status` command to learn whether any files in your local repo contain changes that are absent in GitHub's copy of the repo
```console
mlandis@biol4220-mlandis:~/labs/lab-01-mlandis$ git status
On branch main
Your branch is up to date with 'origin/main'.

Untracked files:
  (use "git add <file>..." to include in what will be committed)
	more_output.txt

nothing added to commit but untracked files present (use "git add" to track)
```

Notice that the status continues to report that our local branch is in sync with GitHub's branch, but status notes a new *untracked file* has been added to the directory structure monitored by `git`. We'll use the `git add` command to track changes to `more_output.txt`, and alert us if the file is out-of-sync.

```console
mlandis@biol4220-mlandis:~/labs/lab-01-mlandis$ git add more_output.txt
mlandis@biol4220-mlandis:~/labs/lab-01-mlandis$ git status
On branch main
Your branch is up to date with 'origin/main'.

Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
	new file:   more_output.txt

```

Now we see that the file `more_output.txt` is listed under files with changes *to be committed*. Committing those changes will inform `git` to recognize that the local branch has been updated.

Before we commit these changes, we first need to set a few *global settings* for the operating system's installation of `git`; you should not need to type these commands again in future lab exercises when using `git` on your VM. We will also let `git` know your name, your email address, that you prefer to use `nano` as a text editor for `git`-related issues (like commit messages), and that you'd like to use a color-rich user interface for `git` output.

```console
git config --global user.name "Michael Landis"
git config --global user.email "michael.landis@wustl.edu"
git config --global core.editor nano
git config --global color.ui true
```

You can always view your global settings for `git` with the command `git config --list`.

Now, to commit our changes, we'll use the `git commit` with the `-m` flag to pass a commit message along with our changes.


```console
mlandis@biol4220-mlandis:~/labs/lab-01-mlandis$ git commit -m 'checking in with Planet Earth'
[main 517d999] checking in with Planet Earth
 1 file changed, 1 insertion(+)
 create mode 100644 more_output.txt
```

Our successful commit returns several useful pieces of information, in particular: the abbreviated *commit id* for our saved changes (`517d999`), how many files were updated (`1 file changed`); and how many lines were inserted or deleted (`1 insertion(+)`).

Now, let's check the status of our repo

```console
mlandis@biol4220-mlandis:~/labs/lab-01-mlandis$ git status
On branch main
Your branch is ahead of 'origin/main' by 1 commit.
  (use "git push" to publish your local commits)

nothing to commit, working tree clean
```

Our local branch is one commit ahead of GitHub's copy. This should seem correct to you, since all of our changes so far have been local, and still need to be communicated to the remote repo hosted by GitHub! To send *all local commits* to GitHub, we will use the `git push` command

```console
mlandis@biol4220-mlandis:~/labs/lab-01-mlandis$ git push
Username for 'https://github.com': mlandis
Password for 'https://mlandis@github.com':
Enumerating objects: 4, done.
Counting objects: 100% (4/4), done.
Delta compression using up to 2 threads
Compressing objects: 100% (2/2), done.
Writing objects: 100% (3/3), 366 bytes | 366.00 KiB/s, done.
Total 3 (delta 0), reused 0 (delta 0)
To https://github.com/WUSTL-Biol4220/lab-01-mlandis.git
   f67bd00..517d999  main -> main
```

And we now see that the local and remote repos are once again in-sync.

```console
mlandis@biol4220-mlandis:~/labs/lab-01-mlandis$ git status
On branch main
Your branch is up to date with 'origin/main'.

nothing to commit, working tree clean
```

Now, return to your the GitHub web page that hosts your copy of the Lab 01 repo. Again, for reference, mine is https://github.com/WUSTL-Biol4220/lab-01-mlandis. You should now see your `more_output.txt` file listed in the repo contents.

Congratulations! You've just cloned a local copy of a remote repo, added a file to it, committed the changes, then pushed your changes back to the remote repo. This covers 99% of daily `git` usage. The remaining labs will exercise more difficult situations in repo management.

---

## 2. Configure Lab 03 directory as a GitHub repo

In this lab, we'll learn more about how to move between different commits within a single repo branch.

Similar to what you did in Part 1 of this lab, we will clone your Lab 03 assignment repo from GitHub to the `~/labs` directory on your VM. The process of cloning a repo to your workstation will become familiar over time, but revisit the Part 1 instructions if you don't remember the exact procedure. The general procedure is to: navigate to the Lab 03 assignment on GitHub, click Code, select HTTPS, then copy the link to your clipboard (e.g. `https://github.com/WUSTL-Biol4220/lab-03-mlandis.git`). Then, enter `~/labs` and call `git clone` while using the copied link as the argument.

```console
mlandis@biol4220-mlandis:~/labs$ git clone git@github.com:WUSTL-Biol4220/lab-03-mlandis.git
Cloning into 'lab-03-mlandis'...
Warning: Permanently added the ECDSA host key for IP address '140.82.112.3' to the list of known hosts.
remote: Enumerating objects: 13, done.
remote: Counting objects: 100% (13/13), done.
remote: Compressing objects: 100% (6/6), done.
remote: Total 13 (delta 0), reused 12 (delta 0), pack-reused 0
Receiving objects: 100% (13/13), done.
mlandis@biol4220-mlandis:~/labs$ cd lab-03-mlandis/
mlandis@biol4220-mlandis:~/labs/lab-03-mlandis$ ls
data  README.md
mlandis@biol4220-mlandis:~/labs/lab-03-mlandis$ cat README.md
This repo contains nucleotide sequences for the species in two closely related genera in Felidae, *Panthera* and *Neofelis*:
``
data/panthera/leo.fasta
data/panthera/tigris.fasta
data/panthera/onca.fasta
data/panthera/pardua.fasta
data/panthera/uncia.fasta
data/neofelis/nebulosa.fasta
data/neofelis/diardi.fasta
``
```

Let's begin by reviewing our *commit history* using `git log`

```
mlandis@biol4220-mlandis:~/labs/lab-03-mlandis$ git log
commit 5c48daca1e1cc668a041602637811586591933ed (HEAD -> main, origin/main, origin/HEAD)
Author: Michael Landis <mlandis@gmail.com>
Date:   Fri Sep 11 11:25:22 2020 -0500

    Initial commit
```

In my case, the commit id for my first commit begins with `5c48dac`. Let's modify a file, commit the changes, then view the commit history again.


```console
mlandis@biol4220-mlandis:~/labs/lab-03-mlandis$ mv data/panthera/leo.fasta data/neofelis/
mlandis@biol4220-mlandis:~/labs/lab-03-mlandis$ git status
On branch main
Your branch is up to date with 'origin/main'.

Changes not staged for commit:
  (use "git add/rm <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
	deleted:    data/panthera/leo.fasta

Untracked files:
  (use "git add <file>..." to include in what will be committed)
	data/neofelis/leo.fasta

no changes added to commit (use "git add" and/or "git commit -a")
```

We need to inform `git` to add any new files within `data` subdirectories, then commit any relevant changes

```console
mlandis@biol4220-mlandis:~/labs/lab-03-mlandis$ git add data
mlandis@biol4220-mlandis:~/labs/lab-03-mlandis$ git commit -m 'move lion to clouded leopard genus'
[main b96cfb5] move lion to clouded leopard genus
 1 file changed, 0 insertions(+), 0 deletions(-)
 rename data/{panthera => neofelis}/leo.fasta (100%)
```

Now, move `data/panthera/tigris.fasta` into `data/neofelis`, and commit that change.


We now see these two commits as the most recent entries in `git log`

```console
mlandis@biol4220-mlandis:~/labs/lab-03-mlandis$ git log
commit 10ee6fb7a13af2e5854b0e203a17e88958375a7f (HEAD -> main)
Author: Michael Landis <michael.landis@wustl.edu>
Date:   Fri Sep 11 12:06:26 2020 -0500

    move tiger into clouded leopard genus

commit b96cfb5bacf3e1c6de1bc546a60d2dfa4b769bc8
Author: Michael Landis <michael.landis@wustl.edu>
Date:   Fri Sep 11 12:02:38 2020 -0500

    move lion to clouded leopard genus

commit 5c48daca1e1cc668a041602637811586591933ed (origin/main, origin/HEAD)
Author: Michael Landis <mlandis@gmail.com>
Date:   Fri Sep 11 11:25:22 2020 -0500

    Initial commit
```

If we want to remember what commit `b96cfb5` was for, we can always read the associated message ("move lion to clouded leopard genus"). But what exactly changed in the filesystem? For this, we can use the command `git diff` to identify *differences* in the filesystem between the two commits.

```console
mlandis@biol4220-mlandis:~/labs/lab-03-mlandis$ git diff b96cfb5 5c48dac
diff --git a/data/neofelis/leo.fasta b/data/panthera/leo.fasta
similarity index 100%
rename from data/neofelis/leo.fasta
rename to data/panthera/leo.fasta
```

Suppose we discover this change was in error. We can use `git revert` to *revert* any changes applied in a particular commit. 

```console
mlandis@biol4220-mlandis:~/labs/lab-03-mlandis$ git revert b96cfb5

   ... use commit message to explain purpose of the revert, if useful ...

[main 8ec9fc0] Revert "move lion to clouded leopard genus"
 1 file changed, 0 insertions(+), 0 deletions(-)
 rename data/{neofelis => panthera}/leo.fasta (100%)
```

A reversion is itself a commit that is added to the repo history.

```console
mlandis@biol4220-mlandis:~/labs/lab-03-mlandis$ git log -n1
commit 8ec9fc0e2935214238013f1b12f54bbfbd328818 (HEAD -> main)
Author: Michael Landis <michael.landis@wustl.edu>
Date:   Fri Sep 11 12:14:34 2020 -0500

    Revert "move lion to clouded leopard genus"

    This reverts commit b96cfb5bacf3e1c6de1bc546a60d2dfa4b769bc8.
```

Revert the other commit, which placed `tigris.fasta` in `data/neofelis`, then commit the reversion. After this, verify that `leo.fasta` and `tigris.fasta` are in `data/panthera` and not in `data/neofelis`. By calling `git status`, it will report that your repo is out-of-sync with GitHub: "`Your branch is ahead of 'origin/main' by 4 commits.`"). Use `git push` to synchronize your local repo with GitHub. Refer to the first part of Lab 03 if you are unsure of how to do this.

Now, if someone were to clone your repo from GitHub, they would have access to all of your changes, including the reversions. Validate this by visiting your Lab 03 repo on GitHub. Notice that your newest commit appears at the top of your repo's page.

<img src="https://github.com/WUSTL-Biol4220/home/raw/main/assets/lab_03/view_03.png" width="350"/>

Click on the "5 commits" (or however many commits your branch has) to view the commit history through the GitHub GUI.

<img src="https://github.com/WUSTL-Biol4220/home/raw/main/assets/lab_03/commit_03.png" width="350"/>

Suppose now that you wanted to view and interact with the filesystem as it existed before your two reversions. Return to your VM and checkout the commit prior to the commit in which you applied `git revert` (for me, it's `10ee6fb`).

```console
mlandis@biol4220-mlandis:~/labs/lab-03-mlandis$ git checkout 10ee6fb
Note: switching to '10ee6fb'.

You are in 'detached HEAD' state. You can look around, make experimental
changes and commit them, and you can discard any commits you make in this
state without impacting any branches by switching back to a branch.

If you want to create a new branch to retain commits you create, you may
do so (now or later) by using -c with the switch command. Example:

  git switch -c <new-branch-name>

Or undo this operation with:

  git switch -

Turn off this advice by setting config variable advice.detachedHead to false

HEAD is now at 10ee6fb move tiger into clouded leopard genus
mlandis@biol4220-mlandis:~/labs/lab-03-mlandis$ ls data/panthera/
onca.fasta  pardua.fasta  uncia.fasta
mlandis@biol4220-mlandis:~/labs/lab-03-mlandis$ ls data/neofelis/
diardi.fasta  leo.fasta  nebulosa.fasta  tigris.fasta
```

The files `leo.fasta` and `tigris.fasta` have returned to the `data/neofelis` folder, as they were in commit `10ee6fb`. What we can't ignore is the long warning message, indicating that the branch is now in a `detached HEAD` state. A detached HEAD state means that the commit you are interacting with (via checkout) is not associated with a branch. Commits you make while detached will not be stored to the commit history of the previously checked out branch. A detached head state can allow you to modify older versions of the files in your repo, observe how the new changes behave, and (if useful) save those changes into a new branch.

For this lab, we will modify the filesystem while in a detached state by deleting a directory. Then we will return to our original position in the git history with a second checkout command, which will restore the directory as it was originally saved in the main branch.

```console
mlandis@biol4220-mlandis:~/labs/lab-03-mlandis$ rm -rf data
mlandis@biol4220-mlandis:~/labs/lab-03-mlandis$ ls data
ls: cannot access 'data': No such file or directory
mlandis@biol4220-mlandis:~/labs/lab-03-mlandis$ git checkout main data
Updated 7 paths from ed02d3c
mlandis@biol4220-mlandis:~/labs/lab-03-mlandis$ git checkout main
Switched to branch 'main'
Your branch is up to date with 'origin/main'.
mlandis@biol4220-mlandis:~/labs/lab-03-mlandis$ git status
On branch main
Your branch is up to date with 'origin/main'.

nothing to commit, working tree clean
mlandis@biol4220-mlandis:~/labs/lab-03-mlandis$ ls data
neofelis  panthera
```

Your local VM and GitHub repos should now be viewing the same commit -- i.e. the most recent commit in the repo's history.

---

## 3. Commit and push Lab 03 to VM using `git`

In this final section, we'll learn how to work with multiple `git` branches, including how to create new branches, how to merge branches, and resolve merge conflicts. Each `git` branch manages its own commit history. This allows the user to freely modify different versions of the git repo's filesystem, with options to reconcile differences between branch histories should that be useful in some way. Becoming comfortable with branch management is key to unlocking the full potential of `git`.

To begin, we can use the `git branch` command to observe what branches are locally available, and which branch we are currently modifying.

```console
mlandis@biol4220-mlandis:~/labs/lab-03-mlandis$ git branch
* main
```

We are using (`*`) the default branch (`main`), which is the only branch, currently. Suppose you wanted to add the new file `data/puma/concolor.fasta` to the repo filesystem, but you wanted to introduce those changes in a way that wouldn't interfere with the contents of `main`. We will create a new branch called `add_puma`, then switch into it.

```console
mlandis@biol4220-mlandis:~/labs/lab-03-mlandis$ git branch add_puma
mlandis@biol4220-mlandis:~/labs/lab-03-mlandis$ git branch
  add_puma
* main
mlandis@biol4220-mlandis:~/labs/lab-03-mlandis$ git checkout add_puma
Switched to branch 'add_puma'
mlandis@biol4220-mlandis:~/labs/lab-03-mlandis$ git branch
* add_puma
  main
```

Now, create a new directory called `data/puma` and the file `data/puma/concolor.fasta` with the contents
```console
> Puma_concolor
ACGTTATTACAT
```

Next, add that file to be monitored by the repo, then commit the changes to the branch's history. Once those changes are committed, try to push the commit history to GitHub.

```console
mlandis@biol4220-mlandis:~/labs/lab-03-mlandis$ git push
fatal: The current branch add_puma has no upstream branch.
To push the current branch and set the remote as upstream, use

    git push --set-upstream origin add_puma
```

When you create a new branch in `git` through your local machine, you will need to inform GitHub (`origin`) before you can push the current branch 
```console
mlandis@biol4220-mlandis:~/labs/lab-03-mlandis$ git push --set-upstream origin add_puma
Username for 'https://github.com': mlandis
Password for 'https://mlandis@github.com':
Enumerating objects: 7, done.
Counting objects: 100% (7/7), done.
Delta compression using up to 2 threads
Compressing objects: 100% (3/3), done.
Writing objects: 100% (5/5), 474 bytes | 474.00 KiB/s, done.
Total 5 (delta 0), reused 0 (delta 0)
remote:
remote: Create a pull request for 'add_puma' on GitHub by visiting:
remote:      https://github.com/WUSTL-Biol4220/lab-03-mlandis/pull/new/add_puma
remote:
To https://github.com/WUSTL-Biol4220/lab-03-mlandis.git
 * [new branch]      add_puma -> add_puma
Branch 'add_puma' set up to track remote branch 'add_puma' from 'origin'.
```

Now go to GitHub. Notice that the GitHub repo now lists two branches: `main` and `add_puma`.

<img src="https://github.com/WUSTL-Biol4220/home/raw/main/assets/lab_03/new_branch_03.png" width="350"/>

Unfortunately, we forgot to update the `README.md` file to reflect the new contents of `data` in the `add_puma` branch. Use the GitHub editor to correct the text of `README.md`. This edit will appear as a new commit in the branch history.

<img src="https://github.com/WUSTL-Biol4220/home/raw/main/assets/lab_03/view_03.png" width="350"/>

To apply the new GitHub branch commits to your local copy of the branch, you will need *pull* them from GitHub (`origin`), like so

```console
mlandis@biol4220-mlandis:~/labs/lab-03-mlandis$ git pull
Username for 'https://github.com': mlandis
Password for 'https://mlandis@github.com':
remote: Enumerating objects: 5, done.
remote: Counting objects: 100% (5/5), done.
remote: Compressing objects: 100% (3/3), done.
remote: Total 3 (delta 1), reused 0 (delta 0), pack-reused 0
Unpacking objects: 100% (3/3), 754 bytes | 754.00 KiB/s, done.
From https://github.com/WUSTL-Biol4220/lab-03-mlandis
   dd7156a..d443871  add_puma   -> origin/add_puma
Updating dd7156a..d443871
Fast-forward
 README.md | 3 ++-
 1 file changed, 2 insertions(+), 1 deletion(-)
mlandis@biol4220-mlandis:~/labs/lab-03-mlandis$ cat README.md
This repo contains nucleotide sequences for the species in three Felidae genera, *Panthera*, *Neofelis*, and *Puma*:
``
data/panthera/leo.fasta
data/panthera/tigris.fasta
data/panthera/onca.fasta
data/panthera/pardua.fasta
data/panthera/uncia.fasta
data/neofelis/nebulosa.fasta
data/neofelis/diardi.fasta
data/puma/concolor.fasta
``
```

Let's now return to the `main` branch on our VM using the `git checkout` command. Once in `main`, create a new file (and directories) for `data/acinonyx/jubatus.fasta`. That file will contain the text
```console
> Aciononyx_jubatus
CCGTTCTTACAT
```
Be sure to also update `README.md` to reflect the changes in our `data` directory. Commit your changes and push them to GitHub.

The two branches, `main` and `add_puma`, contain new data additions that we would somehow like to reunify into a single branch. This can be done using the `git merge` command. To *merge* in `git`, you will merge another branch into the branch you are currently using. In our case, we will merge `add_puma` into `main`.

```console
mlandis@biol4220-mlandis:~/labs/lab-03-mlandis$ git branch
  add_puma
* main
mlandis@biol4220-mlandis:~/labs/lab-03-mlandis$ git merge add_puma
Auto-merging README.md
CONFLICT (content): Merge conflict in README.md
Automatic merge failed; fix conflicts and then commit the result.
```

The merge had no problem copying the separate `data/acinonyx/jubatus.fasta` and `data/puma/concolor.fasta` files

```console
mlandis@biol4220-mlandis:~/labs/lab-03-mlandis$ ls data
acinonyx  neofelis  panthera  puma
```

But our merge reported a *merge conflict* in `README.md` that needs to be resolved. Of course! Both `main` and `add_puma` modified the contents of `README.md`. To *resolve* the merge conflict, open `README.md` in `nano`. You will see text similar to this

```console
<<<<<<< HEAD
This repo contains nucleotide sequences for the species in three genera in Felidae, *Panthera*, *Neofelis*, and *Acinonyx*:
=======
This repo contains nucleotide sequences for the species in three Felidae genera, *Panthera*, *Neofelis*, and *Puma*:
>>>>>>> add_puma
``
data/panthera/leo.fasta
data/panthera/tigris.fasta
data/panthera/onca.fasta
data/panthera/pardua.fasta
data/panthera/uncia.fasta
data/neofelis/nebulosa.fasta
data/neofelis/diardi.fasta
<<<<<<< HEAD
data/acinonyx/jubatus.fasta
=======
data/puma/concolor.fasta
>>>>>>> add_puma
``
```

Blocks of text that are in conflict are demarcated by `<<<<<<` and `>>>>>>>`. The first section between `<<<<<<< HEAD` and `=======` represents the text from your current branch, and the text from the second section between `=======` and `>>>>>>> add_puma` represents new text from the *merging* branch.

Resolve the merge conflict by editing the `README.md` file, unifying any text that lies between the `>>>>>>>` and `<<<<<<<` markers by manually editing it, then deleting any lines that contain the `>>>>>>>`, `=======`, and `<<<<<<<` markers. For example, my `README.md` was edited to appear as

```console
This repo contains nucleotide sequences for the species in four Felidae genera, *Panthera*, *Neofelis*, *Acinonyx*, and *Puma*:
``
data/panthera/leo.fasta
data/panthera/tigris.fasta
data/panthera/onca.fasta
data/panthera/pardua.fasta
data/panthera/uncia.fasta
data/neofelis/nebulosa.fasta
data/neofelis/diardi.fasta
data/acinonyx/jubatus.fasta
data/puma/concolor.fasta
``
```

Save the edited file and return to the command line. View the status of the repo

```console
mlandis@biol4220-mlandis:~/labs/lab-03-mlandis$ git status
On branch main
Your branch is ahead of 'origin/main' by 1 commit.
  (use "git push" to publish your local commits)

You have unmerged paths.
  (fix conflicts and run "git commit")
  (use "git merge --abort" to abort the merge)

Changes to be committed:
	new file:   data/puma/concolor.fasta

Unmerged paths:
  (use "git add <file>..." to mark resolution)
	both modified:   README.md

```

The status report indicates that our changes to `README.md` must be added to the repo to resolve the merge conflict. Add `README.md` to the tracked files, commit all changes, then push the changes back to GitHub.

```console
mlandis@biol4220-mlandis:~/labs/lab-03-mlandis$ git add README.md
mlandis@biol4220-mlandis:~/labs/lab-03-mlandis$ git commit -am 'merge with add_puma; resolve README.md conflict'
[main b34d17b] merge with add_puma; resolve README.md conflict
mlandis@biol4220-mlandis:~/labs/lab-03-mlandis$ git push
Username for 'https://github.com': mlandis
Password for 'https://mlandis@github.com':
Enumerating objects: 16, done.
Counting objects: 100% (16/16), done.
Delta compression using up to 2 threads
Compressing objects: 100% (8/8), done.
Writing objects: 100% (10/10), 979 bytes | 326.00 KiB/s, done.
Total 10 (delta 3), reused 0 (delta 0)
remote: Resolving deltas: 100% (3/3), completed with 1 local object.
To https://github.com/WUSTL-Biol4220/lab-03-mlandis.git
   0004f47..b34d17b  main -> main
```

Return to the Lab 03 repo on GitHub. The `README.md` should show your merged changes.

<img src="https://github.com/WUSTL-Biol4220/home/raw/main/assets/lab_03/commit_03.png" width="350"/>
