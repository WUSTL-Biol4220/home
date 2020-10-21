# Lab 06B

*Lab 06B GitHub Classroom link:* https://classroom.github.com/g/P1iPDoj3

In this lab, we will learn how git enables researchers to modify the same set of files in real time. We will work with a one shared repository to complete the lab exercises. 

Exercises
1. Sharing simple edits
2. Resolving merge conflicts
3. Managing multiple branches
4. GitHub features

For the below exercises, replace instances of `mlandis` with your username. For example, if your username is `beyonce` and you are asked to create the file `data_mlandis.txt`, instead create the file `data_beyonce.txt`.

You do not need to turn in any individual assignments as part of this lab, but your commits must appear in the shared repository's commit history.

---

## Sharing simple edits


Begin by cloning the Lab 06B assignment repo to your VM.

```console
$ cd ~/labs
$ git clone https://github.com/WUSTL-Biol4220/lab-06b-entire-class.git
$ cd lab-06b-entire-class
```

Create a new local branch (we will use this later) named `mlandis_edit` (remember, substitute your username where you see `mlandis`):
```console
$ git branch mlandis_edit
$ git branch
* main
  mlandis_edit
```

Our first group exercise will be to create an empty file named `data_mlandis.txt`. Commit that file to your current branch (`main`) in your local repository, then push your changes to the remote repo on GitHub. After everyone has pushed their changes, pull changes from the remote repo. You should now have a local copy of each student's empty file. 

Now, add your username and a message to your file. Commit and push the changes, while pulling any changes from your collaborators. Repeat this three times. At this time, no one should modify any file but their own, meaning `git` should report any issues as everyone pushes and pulls their changes.

---

## Resolving merge conflicts

Now, we will try modifying another users file. Insert your username (`mlandis was here`) to one other `data_username.txt` file, then commit and push that change to the remote repository. If another user has pushed their changes to the remote repo before you, then you will need to pull their changes into your local repo. It may also be the case that other users have edited the same file that you decided to edit! In that case, you will need to handle the merge conflict, commit your conflict resolution, then push your changes. When resolving a merge conflict, you may decide to retain either your name, your classmate's name, or both names.

Merge conflicts have the general structure
```
mlandis: git out of my file
<<<<<<< HEAD
mlandis: I have nothing to share but bad puns
=======
beyonce: it's spelled get, dude
>>>>>>> new_branch_to_merge_later
```
To resolve a merge conflict by hand, open the conflicted file in `nano`, then search for lines beginning with `<<<` with the search tool (`^W`). In the above example, deleting everything by `beyonce: it's spelled get, dude` would resolve the conflict. (Not to mention combat the rising threat of punnery.)

We'll repeat this three times as a class to become familiar with the process. If a merge ever becomes too overwhelming, you can generally abort the procedure with the command `git merge --abort` or by using `git reset COMMIT_ID` to restore the filesystem and commit history to the state related to `COMMIT_ID`.

At the end of the exercise, call `git blame data_mlandis.txt` to view who made the most recent edits to each line of the file.

---

## Managing multiple branches

In this part, we will return to the local branch we created in Part 1.

```console
$ git checkout mlandis_edit
```

This branch is an older version of `main`, before all us applied ourt edits. First, merge the `main` branch into `mlandis_edit`

```console
$ git merge main
```

Next, we will all search-and-replace text patterns found in *Origin of Species* (`oos.txt`). Everyone choose a *different* word to replace (and suggested replacements) from the list of words below:
```
pigeon -> flying rat
fancier -> bird-wonk
fossils -> extinct taxa
extinction -> death
divergence -> displacement
selection -> culling                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           
```

Once you've made your changes, commit the edits to your local branch. Keep in mind, however, that your local branch has not yet been synchronized with the remote repository. Calling `git push` returns this error
```console
$ git push
fatal: The current branch mlandis_edit has no upstream branch.
To push the current branch and set the remote as upstream, use

    git push --set-upstream origin mlandis_edit
    
```

which means that the remote repository in GitHub (`origin`) has no local copy of `mlandis_edit`. Execute the command printed in the error message to create a new branch on the remote repo.

```console
$ git push --set-upstream origin mlandis_edit
Total 0 (delta 0), reused 0 (delta 0)
remote:
remote: Create a pull request for 'mlandis_edit' on GitHub by visiting:
remote:      https://github.com/WUSTL-Biol4220/lab-06b-entire-class/pull/new/mlandis_edit
remote:
To https://github.com/WUSTL-Biol4220/lab-06b-entire-class.git
 * [new branch]      mlandis_edit -> mlandis_edit
Branch 'mlandis_edit' set up to track remote branch 'mlandis_edit' from 'origin'.
```

Wait until everyone has pushed their local branches to GitHub. Now, call `git pull` to retrieve fresh copies of all branches recognized by GitHub. If you call `git branch`, only branches that you have previously checked out will be listed.

```console
$ git branch
  master
* mlandis_edit
```

Executing `git branch -r` will list all branches that may load into your filesystem. Once a branch has been checked out, it will appear under the shortened list for `git branch`.

Everyone checkout one other student's branch. Then, merge your branch into their branch. This will likely result in merge conflicts. Resolve those conflicts, commit the resolution. Then push the changes back to GitHub.

Wait until everyone is done, then we will try to merge each of our branches into `main`, from the instructor's computer. It's certain the merge will flag many conflicts, in which case we can either resolve each conflict by hand, on a case-by-case basis. Alternatively, we can instruct `git` to always prefer one repo's changes over another's. Cancel the conflicted merge request using `git merge --abort`. Then call `git pull -X theirs` to resolve all merge conflicts in favor of the *incoming branch* or use `git pull -X ours` to resolve all conflicts in favor of the *current branch*.

Once we have merged all existing branches into `main`, we can view how the branches have split and merged using the command
```console
$ git log --oneline --decorate --all --graph
```

After discussing the structure of the commit history graph, all students will create a second local branch. Create a file with the command e.g. `history > history_mlandis.txt`, then store the new file to your new local branch's commit history. Finally, each student will merge their new local branch into `main`, and push their changes to GitHub.

---

Be sure that your history file appears in the `main` branch on GitHub.
