
# Lab 1A

*Lab 1A GitHub Classroom link:* https://classroom.github.com/a/p86i6vXW

In this lab, we'll familiarize ourselves with various computational resources and procedures that we'll use throughout the course.

This lab has seven parts

1. [Explore the course home page](https://github.com/WUSTL-Biol4220/lab_1A#1-explore-the-course-home-page)
2. [Connect to the virtual private network (VPN)](https://github.com/WUSTL-Biol4220/lab_1A#2-connect-to-the-virtual-private-network-vpn)
3. [Install the secure shell client (SSH)](https://github.com/WUSTL-Biol4220/lab_1A#3-connect-to-the-secure-shell-client-ssh)
4. [Connect to your virtual machine (VM)](https://github.com/WUSTL-Biol4220/lab_1A#4-connecting-to-your-lab-computer-your-virtual-machine)
5. [Create a GitHub account](https://github.com/WUSTL-Biol4220/lab_1A#5-create-a-github-account)
6. [Accept a GitHub Classroom assignment](https://github.com/WUSTL-Biol4220/lab_1A#6-accept-your-first-github-classroom-assignment)
7. [Submit a GitHub Classroom assignment](https://github.com/WUSTL-Biol4220/lab_1A#7-complete-your-first-github-classroom-assignment)

Parts of this lab assignment may be particularly difficult for students who are new to computing. Some of the concepts and commands we're using here have not yet been introduced, and may seem unfamiliar or intimidating. This feeling is common in computing! Do the best that you can do for now, and rest assured that we'll spend more time learning about these new concepts soon enough! Please ask the instructor for help if needed.


---
## 1. Explore the course home page

Part 1 of Lab 1A will simply be to locate a few key resources for Biol 4220.

The main course webpage is located at: [https://github.com/WUSTL-Biol4220/home](https://github.com/WUSTL-Biol4220/home). 

All of the course materials are centralized in this page, including the Zoom meeting link, the course schedule, instructor contact information, and various course resources. The course resources are especially important, because they provide specific answers to various questions you might have. When in doubt, check the course resources!

The course resources include:
* [Syllabus](https://docs.google.com/document/d/1TYE10600VUhCyq51_h_9flVUhkCF-IQCE9SnQKRGRGo/edit?usp=sharing)
* [Lecture & Lab schedule](https://github.com/WUSTL-Biol4220/home/blob/master/course_schedule.md)
* ["How To" guide](https://github.com/WUSTL-Biol4220/home/blob/master/how_to_guide.md)
* [Course Project](https://github.com/WUSTL-Biol4220/home/blob/master/course_project.md)
* [GitHub Classroom](https://classroom.github.com/classrooms/69019055-practical-bioinformatics-f2020)
* [Canvas](https://wustl.instructure.com/courses/54531)

(Throughout the remaining tasks in Lab 1A, we'll repeatedly refer to the "How To" guide.)

Notice that this website is hosted at the web addresss [http://github.com](http://github.com). GitHub is a website used by programmers, artists, and researchers to save and share digital projects. Biol 4220 will make heavy use of GitHub in various ways. Not only will we use it to host organizational materials for the course. We'll also use GitHub to submit our lab exercises and to develop our analysis pipeline projects.

---

## 2. Connect to the virtual private network (VPN)

A *virtual private network* (VPN) is an extension of a private network that can be accessed through the internet. To control access to the VPN, a network administrator can design a server, called the *VPN host*, that only allows authorized users to connect to the VPN. Authorized users identify and authenticate themselves against the VPN host using a special piece of software, called the *VPN client*. Connecting to a VPN generally requires the user to provide (1) the IP address for the VPN host, (2) the login credentials for a user who is authorized to access the VPN, and sometimes (3) two-factor authentication (or 2FA) to ensure that the user who is logging into the VPN is indeed who they claim to be -- e.g. by sending a push notification to the user's registered smartphone. These VPN client-host relationships allow private networks to control what network resources are accessible to the outside world, and to whom.

For Part 2 of Lab 1A, we'll install the VPN client software on to your home computer, then verify that we can connect to the WUSTL VPN.

Complete the steps in the [VPN](https://github.com/WUSTL-Biol4220/home/blob/master/how_to_guide.md#virtual-private-network-vpn) section in the "How To" guide.

In general, your home computer will need to be connected to the VPN to connect to your lab virtual machine (e.g. Part 3 of Lab 1A) and other WUSTL network resources. 

Now you can access approved WUSTL network resources from anywhere in the world, even your home.

---

## 3. Connect to the secure shell client (SSH)

Two computers that are on the same network can connect and communicate with one another in various ways. One mode of communication -- through the secure shell (SSH) protocol -- is remarkably simple, fast, versatile, and secure. Once you have established an SSH connection with a remote computer, you will largely be free to interact with that computer as though you were physically sitting in front of it, at the keyboard, logged in through your user account. Most bioinformatics work carried out on remote computers is facilitated by SSH.

The easiest way to connect to a remote computer through the SSH protocol is to install an SSH client.

Complete the steps in the [SSH](https://github.com/WUSTL-Biol4220/home/blob/master/how_to_guide.md#secure-shell-ssh) section in the "How To" guide.

Now your home computer has a way to remotely interact with other computers on the network.

---

## 4. Connecting to your lab computer (your virtual machine)

In Biol 4220, each student will have access to their own personal computer, located on the WUSTL private network. All student computers are configured in the exact same way: they are all running the Linux operating system, [Ubunutu 20.04 LTS](https://releases.ubuntu.com/20.04/), and they are all pre-configured with the software required to complete the Biol 4420 lab exercises.

One thing to know is that these lab computers are not *physical computers*, but *virtual machines* or (VMs). As the name suggests, a VM is a computer hardware system that is emulated using software. This emulation is called *virtualization*. VMs are typically hosted by a VM server that specializes in virtualization, and is responsible for managing shared *physical* hardware resources -- such as processor time, memory, disk storage -- across the VMs that it is hosting, as well as backing up VMs, rebooting VMs, copying VMs, etc. Virtualization is an extremely useful technology, because it allows you to safely control and replicate your software environment, making certain software configurations extremely portable across diverse computing infrastructures. (For wet lab folks, imagine if you could "clone" your bench setup and mail it to a collaborating lab!)

Complete the steps in the [VM section](https://github.com/WUSTL-Biol4220/home/blob/master/how_to_guide.md#lab-virtual-machines-vm) in the "How To" guide.

Now you know how to connect to your VM.

Take a moment to reflect on what you've done so far. First, you connected to the WUSTL network, either by being on the WUSTL campus or by connecting to the WUSTL VPN. Second, you initiated an SSH connection to your VM through your SSH client. Third, you authenticated yourself against the VM's operating system (Ubuntu) using your username and password. This demonstrates elemental tasks and technologies can be combined into incredibly useful workflows. This will be a recurring theme in the course.


---

## 5. Create a GitHub account

It was mentioned earlier that this course will use the [GitHub](https://github.com) website for various purposes. All students will need a GitHub account to accept and complete the lab exercises.

If you already have a GitHub account, make sure you know your account name and password.

Students who do not yet have a GitHub account should visit the [Create a GitHub account](https://github.com/WUSTL-Biol4220/home/blob/master/how_to_guide.md#create-a-github-account) section in the "How To" guide.

---

## 6. Accept your first GitHub Classroom assignment

Lab exercises (including this one!) will be assigned to students through the [Practical Bioinformatics (Fall 2020)](https://classroom.github.com/classrooms/69019055-practical-bioinformatics-f2020) website, hosted by [GitHub Classroom](https://classroom.github.com).

Each lab exercise will include an *invitation link* at the top of the lab instructions (i.e. the `README.md` file, like this one). The invitation link for Lab 1A is https://classroom.github.com/a/p86i6vXW.

By clicking that link, you will inform GitHub Classroom that you've accepted the assignment. GitHub Classroom will then prepare your lab workspace on the code-sharing website GitHub. After that workspace is prepared, all that's left is to complete your assignment (next section).

Visit the [Accept a GitHub Classroom assignment]() section in the "How To" guide.

Accept the Lab 1A assignment and verify that you can access your lab repository through [GitHub](https://github.com). For example, my GitHub username is mlandis, so my Lab 1A repository was created at https://github.com/WUSTL-Biol4220/lab_1A-mlandis.

---

## 7. Complete your first GitHub Classroom assignment

We are finally in a position to complete your first lab exercise. The task itself for Lab 1A is extremely simple. We will create a file called `output.txt` that contains the text `Hello, world!` in our lab assignment repository on our VM. Then, we will submit lab repository to GitHub Classroom for grading.

First review the [Complete a GitHub Classroom assignment](https://github.com/WUSTL-Biol4220/home/blob/master/how_to_guide.md#complete-your-github-classroom-lab-assignment) section in the "How To" guide. The same general workflow will be used to complete all lab assignments.

To complete the lab, you'll need to SSH into your VM. Revisit the earlier sections of this lab if you don't remember exactly how to do so. 

Once you have SSH'd into your VM, you will see the following prompt
```
mlandis@biol4220-mlandis:~$
```
This prompt informs you of your user account (`mlandis`), what computer you've logged in to (`biol4220-mlandis`), and where in the filesystem you're currently located (your home directory `/home/mlandis` abbreviated as `~`).

You will now make a directory called `projects` with the `mkdir` command
```
mlandis@biol4220-mlandis:~$ mkdir projects
```
then enter the new folder with the change directory (`cd`) command
```
mlandis@biol4220-mlandis:~$ cd projects
mlandis@biol4220-mlandis:~/projects$
```
Notice that the prompt now informs us that we are in the directory `~/projects`, a subdirectory of the home directory, `~`.

Now, you will instruct your VM to copy your lab assignment repository from GitHub into the `~/projects` directory using the `git clone` command
```
mlandis@biol4220-mlandis:~/projects$ git clone https://github.com/WUSTL-Biol4220/lab_1A-mlandis
Cloning into 'lab_1A-mlandis'...
Username for 'https://github.com': mlandis
Password for 'https://mlandis@github.com':
remote: Enumerating objects: 43, done.
remote: Counting objects: 100% (43/43), done.
remote: Compressing objects: 100% (21/21), done.
remote: Total 43 (delta 7), reused 33 (delta 7), pack-reused 0
Unpacking objects: 100% (43/43), 10.90 KiB | 413.00 KiB/s, done.
mlandis@biol4220-mlandis:~/projects$
```

Now we have a local copy of the lab assignment repository in our `~/projects` folder. Use `cd` to enter the new repository directory.

```
mlandis@biol4220-mlandis:~/projects$ cd lab_1A-mlandis/
mlandis@biol4220-mlandis:~/projects/lab_1A-mlandis$
```

Next, we will create a file called `output.txt` that contains the text `Hello, world!`

```
mlandis@biol4220-mlandis:~/projects/lab_1A-mlandis$ echo Hello, world! > output.txt
```

To verify that `output.txt` contains the desired text, we can print the file contents to screen with the `cat` command
```
mlandis@biol4220-mlandis:~/projects/lab_1A-mlandis$ cat output.txt
Hello, world!
```

Why, hello to you, too, computer! The file contents have been validated, thus completing the computational task for Lab 1A!

We still, however, need to submit our results to GitHub Classroom.

```
mlandis@biol4220-mlandis:~/projects/lab_1A-mlandis$ git config --global user.email "michael.landis@wustl.edu"
mlandis@biol4220-mlandis:~/projects/lab_1A-mlandis$ git config --global user.name "Michael Landis"
```

We will need to tell the computer that we'd like to associate our new `output.txt` file with the repository
```
mlandis@biol4220-mlandis:~/projects/lab_1A-mlandis$ git add output.txt
```

then save our changes with the `git commit` command

```
mlandis@biol4220-mlandis:~/projects/lab_1A-mlandis$ git commit -am 'add output.txt'
[master a181324] add output.txt
 1 file changed, 1 insertion(+)
 create mode 100644 output.txt
```

finally, we send our saved changes back to GitHub to be graded by GitHub Classroom
```
mlandis@biol4220-mlandis:~/projects/lab_1A-mlandis$ git push
Username for 'https://github.com': mlandis
Password for 'https://mlandis@github.com':
Enumerating objects: 4, done.
Counting objects: 100% (4/4), done.
Delta compression using up to 2 threads
Compressing objects: 100% (2/2), done.
Writing objects: 100% (3/3), 332 bytes | 332.00 KiB/s, done.
Total 3 (delta 0), reused 0 (delta 0)
To https://github.com/WUSTL-Biol4220/lab_1A-mlandis
   bc5ac54..a181324  master -> master
mlandis@biol4220-mlandis:~/projects/lab_1A-mlandis$
```

You have now submitted your assignment! You can exit the SSH session on your VM. 

```
mlandis@biol4220-mlandis:~/projects/lab_1A-mlandis$ exit
logout
Connection to 128.252.89.47 closed.
```

When you visit your Lab 1A assignment repository on GitHub, you should see a green checkmark towards the top of the screen.

<img src="https://raw.githubusercontent.com/WUSTL-Biol4220/home/master/assets/lab_1A_git_class_success.png" width="350"/>

If you do not see a green checkmark, or if you see a red 'X', you will want to make sure that your GitHub repository contains the file `output.txt` and that the file only contains the text `Hello, world!`.

This concludes your first lab exercise.
