# Lab 02A

*Lab 02A GitHub Classroom link:* https://classroom.github.com/a/4ZJF3Kfx

In this lab, we'll learn the basics of the version control software, `git`, and how to use `git` with [GitHub](https://github.com). Using `git` to manage your code or other projects becomes natural with practice. However, it can feel complicated at times. If you feel nervous about a certain command, you can always create a "test example" like what we'll use below to understand how the commands work in a safe environment. The other good news is that, generally, `git` itself does not forget the versioned history of files its watching; that means that even if you do make a mistake, its almost certain that you can recover from a previously saved version. That's the beauty of version control.

The major tasks to complete for Lab 02A are
1. Exploring `git` basics
2. Working within a single branch
3. Working with multiple branches

For this lab, you will be the only contributor to your repo. In a future lab, we will cover how to work with other contributors in a shared repo.

---

## 1. Clone your "Lab 01A" repo to your VM

Enter your Lab 01A repo hosted at https://github.com/WUSTL-Biol4220. For example, the repo for Lab 01A for my user account (`mlandis`) is located at https://github.com/WUSTL-Biol4220/lab-01a-mlandis.

<img src="https://github.com/WUSTL-Biol4220/home/raw/master/assets/lab_02A/clone_01a.png" width="350"/>

Click on the green "Code" button, which will present you with various options for how to acquire the code. One of the bottom two options is to open the repo in the GitHub Desktop repo management application (which we won't use in this course). Another option is to download the entire repo as a `.zip` file. What we'll do is clone (or copy) the repository to our VM using the `git clone` command.

We will clone using the HTTPS link, which needs no special configuration but does require you to enter your username and password to interact with GitHub. Your dropdown menu should read "Clone with HTTPS"; if it does not, click the blue "Use HTTPS" link. Copy the HTTPS link to your clipboard. For example, my HTTPS link is `https://github.com/WUSTL-Biol4220/lab-01a-mlandis.git`.

Log into your VM and change directories to `~/labs`; we'll store all course lab work in this directory from now own. From here, we'll instruct `git` to `clone` (copy) the repository hosted at `https://github.com/WUSTL-Biol4220/lab-01a-mlandis.git`.

```console
mlandis@biol4220-mlandis:~/labs$ git clone https://github.com/WUSTL-Biol4220/lab-01a-mlandis.git
Cloning into 'lab-01a-mlandis'...
Username for 'https://github.com': mlandis
Password for 'https://mlandis@github.com':
remote: Enumerating objects: 15, done.
remote: Counting objects: 100% (15/15), done.
remote: Compressing objects: 100% (9/9), done.
remote: Total 15 (delta 2), reused 0 (delta 0), pack-reused 0
Unpacking objects: 100% (15/15), 1.71 KiB | 28.00 KiB/s, done.
```

And we see that all files and folders from Lab 01A on GitHub are now in our VM filesystem!
```console
mlandis@biol4220-mlandis:~/labs$ ls
lab-01a-mlandis
mlandis@biol4220-mlandis:~/labs$ ls lab-01a-mlandis/
output.txt
mlandis@biol4220-mlandis:~/labs$ cat lab-01a-mlandis/output.txt
Hello, world!
```

Call `git status` to learn whether any files in your local repo contain changes that are absent in GitHub's copy of the repo

```console
mlandis@biol4220-mlandis:~/labs/lab-01a-mlandis$ git status
On branch master
Your branch is up to date with 'origin/master'.

nothing to commit, working tree clean
```

The command tells us which local branch we're using (`master`) and that our local branch contains no differences compared to GitHub's copy of the branch (`origin/master`). Quite expected, since we just copied our repo from GitHub!

Let's add a new file to our repository

```console
mlandis@biol4220-mlandis:~/labs$ cd lab-01a-mlandis/
mlandis@biol4220-mlandis:~/labs/lab-01a-mlandis$ nano more_output.txt

  ... add some text, then save and exit with ^X
  
mlandis@biol4220-mlandis:~/labs/lab-01a-mlandis$ cat more_output.txt
Hey, world, what's going on with you?
```

Call the `git status` command to learn whether any files in your local repo contain changes that are absent in GitHub's copy of the repo
```console
mlandis@biol4220-mlandis:~/labs/lab-01a-mlandis$ git status
On branch master
Your branch is up to date with 'origin/master'.

Untracked files:
  (use "git add <file>..." to include in what will be committed)
	more_output.txt

nothing added to commit but untracked files present (use "git add" to track)
```

Notice that the status continues to report that our local branch is in sync with GitHub's branch, but status notes a new *untracked file* has been added to the directory structure monitored by `git`. We'll use the `git add` command to track changes to `more_output.txt`, and alert us if the file is out-of-sync.

```console
mlandis@biol4220-mlandis:~/labs/lab-01a-mlandis$ git add more_output.txt
mlandis@biol4220-mlandis:~/labs/lab-01a-mlandis$ git status
On branch master
Your branch is up to date with 'origin/master'.

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
mlandis@biol4220-mlandis:~/labs/lab-01a-mlandis$ git commit -m 'checking in with Planet Earth'
[master 517d999] checking in with Planet Earth
 1 file changed, 1 insertion(+)
 create mode 100644 more_output.txt
```

Our successful commit returns several useful pieces of information, in particular: the abbreviated *commit id* for our saved changes (`517d999`), how many files were updated (`1 file changed`); and how many lines were inserted or deleted (`1 insertion(+)`).

Now, let's check the status of our repo

```console
mlandis@biol4220-mlandis:~/labs/lab-01a-mlandis$ git status
On branch master
Your branch is ahead of 'origin/master' by 1 commit.
  (use "git push" to publish your local commits)

nothing to commit, working tree clean
```

Our local branch is one commit ahead of GitHub's copy. This should seem correct to you, since all of our changes so far have been local, and still need to be communicated to the remote repo hosted by GitHub! To send *all local commits* to GitHub, we will use the `git push` command

```console
mlandis@biol4220-mlandis:~/labs/lab-01a-mlandis$ git push
Username for 'https://github.com': mlandis
Password for 'https://mlandis@github.com':
Enumerating objects: 4, done.
Counting objects: 100% (4/4), done.
Delta compression using up to 2 threads
Compressing objects: 100% (2/2), done.
Writing objects: 100% (3/3), 366 bytes | 366.00 KiB/s, done.
Total 3 (delta 0), reused 0 (delta 0)
To https://github.com/WUSTL-Biol4220/lab-01a-mlandis.git
   f67bd00..517d999  master -> master
```

And we now see that the local and remote repos are once again in-sync.

```console
mlandis@biol4220-mlandis:~/labs/lab-01a-mlandis$ git status
On branch master
Your branch is up to date with 'origin/master'.

nothing to commit, working tree clean
```

Now, return to your the GitHub web page that hosts your copy of the Lab 01A repo. Again, for reference, mine is https://github.com/WUSTL-Biol4220/lab-01a-mlandis. You should now see your `more_output.txt` file listed in the repo contents.

Congratulations! You've just cloned a local copy of a remote repo, added a file to it, committed the changes, then pushed your changes back to the remote repo. This covers 99% of daily `git` usage. The remaining labs will exercise more difficult situations in repo management.

---

## 2. Configure Lab 01B directory as a GitHub repo

In this lab, we'll learn more about how to move between different commits within a single repo branch.

Similar to what you did in Part 1 of this lab, we will clone your Lab 02A assignment repo from GitHub to the `~/labs` directory on your VM. The process of cloning a repo to your workstation will become familiar over time, but revisit the Part 1 instructions if you don't remember the exact procedure. The general procedure is to: navigate to the Lab 02A assignment on GitHub, click Code, select HTTPS, then copy the link to your clipboard (e.g. `https://github.com/WUSTL-Biol4220/lab-02a-mlandis.git`). Then, enter `~/labs` and call `git clone` while using the copied link as the argument.

```console
mlandis@biol4220-mlandis:~/labs$ git clone https://github.com/WUSTL-Biol4220/lab-02a-mlandis.git
Cloning into 'lab-02a-mlandis'...
Username for 'https://github.com': mlandis
Password for 'https://mlandis@github.com':
remote: Enumerating objects: 13, done.
remote: Counting objects: 100% (13/13), done.
remote: Compressing objects: 100% (6/6), done.
remote: Total 13 (delta 0), reused 0 (delta 0), pack-reused 0
Unpacking objects: 100% (13/13), 988 bytes | 98.00 KiB/s, done.
mlandis@biol4220-mlandis:~/labs/lab-02a-mlandis$ ls
data  README.md
mlandis@biol4220-mlandis:~/labs/lab-02a-mlandis$ cat README.md
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
mlandis@biol4220-mlandis:~/labs/lab-02a-mlandis$ git log
commit 5c48daca1e1cc668a041602637811586591933ed (HEAD -> master, origin/master, origin/HEAD)
Author: Michael Landis <mlandis@gmail.com>
Date:   Fri Sep 11 11:25:22 2020 -0500

    Initial commit
```

In my case, the commit id for my first commit begins with `5c48dac`. Let's modify a file, commit the changes, then view the commit history again.


```console
mlandis@biol4220-mlandis:~/labs/lab-02a-mlandis$ mv data/panthera/leo.fasta data/neofelis/
mlandis@biol4220-mlandis:~/labs/lab-02a-mlandis$ git status
On branch master
Your branch is up to date with 'origin/master'.

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
mlandis@biol4220-mlandis:~/labs/lab-02a-mlandis$ git add data
mlandis@biol4220-mlandis:~/labs/lab-02a-mlandis$ git commit -m 'move lion to clouded leopard genus'
[master b96cfb5] move lion to clouded leopard genus
 1 file changed, 0 insertions(+), 0 deletions(-)
 rename data/{panthera => neofelis}/leo.fasta (100%)
```

Now, move `data/panthera/tigris.fasta` into `data/neofelis`, and commit that change.


We now see these two commits as the most recent entries in `git log`

```console
mlandis@biol4220-mlandis:~/labs/lab-02a-mlandis$ git log
commit 10ee6fb7a13af2e5854b0e203a17e88958375a7f (HEAD -> master)
Author: Michael Landis <michael.landis@wustl.edu>
Date:   Fri Sep 11 12:06:26 2020 -0500

    move tiger into clouded leopard genus

commit b96cfb5bacf3e1c6de1bc546a60d2dfa4b769bc8
Author: Michael Landis <michael.landis@wustl.edu>
Date:   Fri Sep 11 12:02:38 2020 -0500

    move lion to clouded leopard genus

commit 5c48daca1e1cc668a041602637811586591933ed (origin/master, origin/HEAD)
Author: Michael Landis <mlandis@gmail.com>
Date:   Fri Sep 11 11:25:22 2020 -0500

    Initial commit
```

If we want to remember what commit `b96cfb5`, we can always read the associated message ("move lion to clouded leopard genus"). But what exactly changed in the filesystem? For this, we can use the command `git diff` to identify *differences* in the filesystem between the two commits.

```console
mlandis@biol4220-mlandis:~/labs/lab-02a-mlandis$ git diff b96cfb5 5c48dac
diff --git a/data/neofelis/leo.fasta b/data/panthera/leo.fasta
similarity index 100%
rename from data/neofelis/leo.fasta
rename to data/panthera/leo.fasta
```

Suppose we discover this change was in error. We can use `git revert` to *revert* any changes applied in a particular commit. 

```console
mlandis@biol4220-mlandis:~/labs/lab-02a-mlandis$ git revert b96cfb5

   ... provide a 

[master 8ec9fc0] Revert "move lion to clouded leopard genus"
 1 file changed, 0 insertions(+), 0 deletions(-)
 rename data/{neofelis => panthera}/leo.fasta (100%)
```

A reversion is itself a commit that is added to the repo history.

```console
mlandis@biol4220-mlandis:~/labs/lab-02a-mlandis$ git log -n1
commit 8ec9fc0e2935214238013f1b12f54bbfbd328818 (HEAD -> master)
Author: Michael Landis <michael.landis@wustl.edu>
Date:   Fri Sep 11 12:14:34 2020 -0500

    Revert "move lion to clouded leopard genus"

    This reverts commit b96cfb5bacf3e1c6de1bc546a60d2dfa4b769bc8.
```

Revert the other commit, which placed `tigris.fasta` in `data/neofelis`, then commit the reversion. After this, verify that `leo.fasta` and `tigris.fasta` are in `data/panthera` and not in `data/neofelis`. By calling `git status`, it will report that your repo is out-of-sync with GitHub: "`Your branch is ahead of 'origin/master' by 4 commits.`"). Use `git push` to synchronize your local repo with GitHub. Refer to the first part of Lab 02A if you are unsure of how to do this.

Now, if someone were to clone your repo from GitHub, they would have access to all of your changes, including the reversions. Validate this by visiting your Lab 02A repo on GitHub. Notice that your newest commit appears at the top of your repo's page.

<img src="https://github.com/WUSTL-Biol4220/home/raw/master/assets/lab_02A/view_02a.png" width="350"/>

Click on the "5 commits" (or however many commits your branch has) to view the commit history through the GitHub GUI.

<img src="https://github.com/WUSTL-Biol4220/home/raw/master/assets/lab_02A/commit_02a.png" width="350"/>

Suppose now that you wanted to view and interact with the filesystem as it existed before your two reversions. Return to your VM and checkout the commit prior to the commit in which you applied `git revert` (for me, it's `10ee6fb`).

```console
mlandis@biol4220-mlandis:~/labs/lab-02a-mlandis$ git checkout 10ee6fb
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
mlandis@biol4220-mlandis:~/labs/lab-02a-mlandis$ ls data/panthera/
onca.fasta  pardua.fasta  uncia.fasta
mlandis@biol4220-mlandis:~/labs/lab-02a-mlandis$ ls data/neofelis/
diardi.fasta  leo.fasta  nebulosa.fasta  tigris.fasta
```

The files `leo.fasta` and `tigris.fasta` have returned to the `data/neofelis` folder, as they were in commit `10ee6fb`. What we can't ignore is the long warning message, indicating that the branch is now in a `detatched HEAD` state. In essence, any commits you make in this state will not have any effect on the commit history *for your current branch*. All changes will be forgotten once you return to the most recent commit for the branch.

```console
mlandis@biol4220-mlandis:~/labs/lab-02a-mlandis$ rm -rf data
mlandis@biol4220-mlandis:~/labs/lab-02a-mlandis$ ls data
ls: cannot access 'data': No such file or directory
mlandis@biol4220-mlandis:~/labs/lab-02a-mlandis$ git checkout master data
Updated 7 paths from ed02d3c
mlandis@biol4220-mlandis:~/labs/lab-02a-mlandis$ git checkout master
Switched to branch 'master'
Your branch is up to date with 'origin/master'.
mlandis@biol4220-mlandis:~/labs/lab-02a-mlandis$ git status
On branch master
Your branch is up to date with 'origin/master'.

nothing to commit, working tree clean
```

Your local VM and GitHub repos should now be viewing the same commit -- i.e. the most recent commit in the repo's history.

---

## 3. Commit and push Lab 02A to VM using `git`

In this final section, we'll learn how to work with multiple `git` branches, including how to create new branches, how to merge branches, and resolve merge conflicts. Each `git` branch manages its own commit history. This allows the user to freely modify different versions of the git repo's filesystem, with options to reconcile differences between branch histories should that be useful in some way. Becoming comfortable with branch management is key to unlocking the full potential of `git`.

To begin, we can use the `git branch` command to observe what branches are locally available, and which branch we are currently modifying.

```console
mlandis@biol4220-mlandis:~/labs/lab-02a-mlandis$ git branch
* master
```

We are using (`*`) the default branch (`master`), which is the only branch, currently. Suppose you wanted to add the new file `data/puma/concolor.fasta` to the repo filesystem, but you wanted to introduce those changes in a way that wouldn't interfere with the contents of `master`. We will create a new branch called `add_puma`, then switch into it.

```console
mlandis@biol4220-mlandis:~/labs/lab-02a-mlandis$ git branch add_puma
mlandis@biol4220-mlandis:~/labs/lab-02a-mlandis$ git branch
  add_puma
* master
mlandis@biol4220-mlandis:~/labs/lab-02a-mlandis$ git checkout add_puma
Switched to branch 'add_puma'
mlandis@biol4220-mlandis:~/labs/lab-02a-mlandis$ git branch
* add_puma
  master
```

Now, create a new directory called `data/puma` and the file `data/puma/concolor.fasta` with the contents
```console
> Puma_concolor
ACGTTATTACAT
```

Next, add that file to be monitored by the repo, then commit the changes to the branch's history. Once those changes are committed, try to push the commit history to GitHub.

```console
mlandis@biol4220-mlandis:~/labs/lab-02a-mlandis$ git push
fatal: The current branch add_puma has no upstream branch.
To push the current branch and set the remote as upstream, use

    git push --set-upstream origin add_puma
```

When you create a new branch in `git` through your local machine, you will need to inform GitHub (`origin`) that 
```console
mlandis@biol4220-mlandis:~/labs/lab-02a-mlandis$ git push --set-upstream origin add_puma
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
remote:      https://github.com/WUSTL-Biol4220/lab-02a-mlandis/pull/new/add_puma
remote:
To https://github.com/WUSTL-Biol4220/lab-02a-mlandis.git
 * [new branch]      add_puma -> add_puma
Branch 'add_puma' set up to track remote branch 'add_puma' from 'origin'.
```

Now go to GitHub. Notice that the GitHub repo now lists two branches: `master` and `add_puma`.

<img src="https://github.com/WUSTL-Biol4220/home/raw/master/assets/lab_02A/new_branch_02a.png" width="350"/>

Unfortunately, we forgot to update the `README.md` file to reflect the new contents of `data` in the `add_puma` branch. Use the GitHub editor to correct the text of `README.md`. This edit will appear as a new commit in the branch history.

<img src="https://github.com/WUSTL-Biol4220/home/raw/master/assets/lab_02A/view_02a.png" width="350"/>

To apply the new GitHub branch commits to your local copy of the branch, you will need *pull* them from GitHub (`origin`), like so

```console
mlandis@biol4220-mlandis:~/labs/lab-02a-mlandis$ git pull
Username for 'https://github.com': mlandis
Password for 'https://mlandis@github.com':
remote: Enumerating objects: 5, done.
remote: Counting objects: 100% (5/5), done.
remote: Compressing objects: 100% (3/3), done.
remote: Total 3 (delta 1), reused 0 (delta 0), pack-reused 0
Unpacking objects: 100% (3/3), 754 bytes | 754.00 KiB/s, done.
From https://github.com/WUSTL-Biol4220/lab-02a-mlandis
   dd7156a..d443871  add_puma   -> origin/add_puma
Updating dd7156a..d443871
Fast-forward
 README.md | 3 ++-
 1 file changed, 2 insertions(+), 1 deletion(-)
mlandis@biol4220-mlandis:~/labs/lab-02a-mlandis$ cat README.md
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

Let's now return to the `master` branch on our VM using the `git checkout` command. Once in `master`, create a new file (and directories) for `data/acinonyx/jubatus.fasta`. That file will contain the text
```console
> Aciononyx_jubatus
CCGTTCTTACAT
```
Be sure to also update `README.md` to reflect the changes in our `data` directory. Commit your changes and push them to GitHub.

The two branches, `master` and `add_puma`, contain new data additions that we would somehow like to reunify into a single branch. This can be done using the `git merge` command. To *merge* in `git`, you will merge another branch into the branch you are currently using. In our case, we will merge `add_puma` into `master`.

```console
mlandis@biol4220-mlandis:~/labs/lab-02a-mlandis$ git branch
  add_puma
* master
mlandis@biol4220-mlandis:~/labs/lab-02a-mlandis$ git merge add_puma
Auto-merging README.md
CONFLICT (content): Merge conflict in README.md
Automatic merge failed; fix conflicts and then commit the result.
```

The merge had no problem copying the separate `data/acinonyx/jubatus.fasta` and `data/puma/concolor.fasta` files

```console
mlandis@biol4220-mlandis:~/labs/lab-02a-mlandis$ ls data
acinonyx  neofelis  panthera  puma
```

But our merge reported a *merge conflict* in `README.md` that needs to be resolved. Of course! Both `master` and `add_puma` modified the contents of `README.md`. To *resolve* the merge conflict, open `README.md` in `nano`. You will see text similar to this

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
mlandis@biol4220-mlandis:~/labs/lab-02a-mlandis$ git status
On branch master
Your branch is ahead of 'origin/master' by 1 commit.
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
mlandis@biol4220-mlandis:~/labs/lab-02a-mlandis$ git add README.md
mlandis@biol4220-mlandis:~/labs/lab-02a-mlandis$ git commit -am 'merge with add_puma; resolve README.md conflict'
[master b34d17b] merge with add_puma; resolve README.md conflict
mlandis@biol4220-mlandis:~/labs/lab-02a-mlandis$ git push
Username for 'https://github.com': mlandis
Password for 'https://mlandis@github.com':
Enumerating objects: 16, done.
Counting objects: 100% (16/16), done.
Delta compression using up to 2 threads
Compressing objects: 100% (8/8), done.
Writing objects: 100% (10/10), 979 bytes | 326.00 KiB/s, done.
Total 10 (delta 3), reused 0 (delta 0)
remote: Resolving deltas: 100% (3/3), completed with 1 local object.
To https://github.com/WUSTL-Biol4220/lab-02a-mlandis.git
   0004f47..b34d17b  master -> master
```

Return to the Lab 02A repo on GitHub. The `README.md` should show your merged changes.



<img src="https://github.com/WUSTL-Biol4220/home/raw/master/assets/lab_02A/commit_02a.png" width="350"/>
