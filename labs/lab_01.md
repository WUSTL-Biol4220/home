
# Lab 01

*Lab 01 GitHub Classroom link:* [https://classroom.github.com/a/Sn9nM1tN](https://classroom.github.com/a/Sn9nM1tN)

In this lab, we'll familiarize ourselves with various computational resources and procedures that we'll use throughout the course.

This lab has seven short parts

1. [Explore the course home page](https://github.com/WUSTL-Biol4220/home/blob/main/labs/lab_01.md#1-explore-the-course-home-page)
2. [Virtual private network (VPN)](https://github.com/WUSTL-Biol4220/home/blob/main/labs/lab_01.md#2-virtual-private-network-vpn)
3. [Secure shell client (SSH)](https://github.com/WUSTL-Biol4220/home/blob/main/labs/lab_01.md#3-secure-shell-client-ssh)
4. [Connect to your virtual machine (VM)](https://github.com/WUSTL-Biol4220/home/blob/main/labs/lab_01.md#4-connecting-to-your-lab-computer-your-virtual-machine)
5. [Create a GitHub account](https://github.com/WUSTL-Biol4220/home/blob/main/labs/lab_01.md#5-create-a-github-account)
6. [Accept a GitHub Classroom assignment](https://github.com/WUSTL-Biol4220/home/blob/main/labs/lab_01.md#6-accept-your-first-github-classroom-assignment)
7. [Submit a GitHub Classroom assignment](https://github.com/WUSTL-Biol4220/home/blob/main/labs/lab_01.md#7-complete-your-first-github-classroom-assignment)

Parts of this lab assignment may be particularly difficult for students who are new to computing. Some of the concepts and commands we're using here have not yet been introduced, and may seem unfamiliar or intimidating. This feeling is common in computing! Do the best that you can do for now, and rest assured that we'll spend more time learning about these new concepts soon enough. Please ask the instructors for help if needed.


---
## 1. Explore the course home page

Part 1 of Lab 01 will simply be to locate a few key resources for Biol 4220.

The main course webpage is located at: [https://github.com/WUSTL-Biol4220/home](https://github.com/WUSTL-Biol4220/home). 

All of the course materials are centralized in this page, including the Zoom meeting link, the course schedule, instructor contact information, and various course resources. The course resources are especially important, because they provide specific answers to various questions you might have. When in doubt, check the course resources!

The course resources include:
* [Syllabus](https://docs.google.com/document/d/1dKYfde0X5M6hDkAPgRK1TTpCjtQEg6Zwvj-gFFvMp_A)
* [Lecture & Lab schedule](https://github.com/WUSTL-Biol4220/home/blob/main/course_schedule.md)
* ["How To" guide](https://github.com/WUSTL-Biol4220/home/blob/main/how_to_guide.md)
* [Course Project](https://github.com/WUSTL-Biol4220/home/blob/main/course_project.md)
* [GitHub Classroom](https://classroom.github.com/classrooms/69019055-practical-bioinformatics-2024)
* [Canvas](https://wustl.instructure.com/courses/54531)

(We'll repeatedly refer to the "How To" guide for the tasks assigned in Lab 01.)

Notice that this website is hosted at the web addresss [http://github.com](http://github.com). GitHub is a website used by programmers, artists, and researchers to save and share digital projects. Biol 4220 will make heavy use of GitHub in various ways. Not only will we use it to host organizational materials for the course, we'll also use GitHub to submit our lab exercises and to develop our analysis pipeline projects.

---

## 2. Virtual private network (VPN)

*(NOTE: Connecting to the VPN is only needed to access campus resources when **off-campus**.)*

A *virtual private network* (VPN) is an extension of a private network that can be accessed through the internet. To control access to the VPN, a network administrator can design a server, called the *VPN host*, that only allows authorized users to connect. Authorized users identify and authenticate themselves against the VPN host using a special piece of software, called the *VPN client*. Connecting to a VPN generally requires the user to provide:

1. the IP address for the VPN host
2. the login credentials for a user who is authorized to access the VPN
3. (sometimes) two-factor authentication, or 2FA, to ensure that the user who is logging into the VPN is indeed who they claim to be -- e.g. by sending a push notification to the user's registered smartphone.

These VPN client-host relationships allow private networks to control what network resources are accessible to the outside world, and to whom.

For Part 2 of Lab 01, we'll install the VPN client software on to your home computer, then verify that we can connect to the WUSTL VPN.

Complete the steps in the [VPN](https://github.com/WUSTL-Biol4220/home/blob/main/how_to_guide.md#virtual-private-network-vpn) section in the "How To" guide.

When you are off-campus, your home computer will need to be connected to the VPN to connect to your lab virtual machine (Part 3 of Lab 01) and other WUSTL network resources. 

---

## 3. Secure shell client (SSH)

Two computers that are on the same network can connect and communicate with one another in various ways. Secure shell (SSH) protocol is the most common command line interfacet for interacting with remote computers. It is simple, fast, versatile, secure, and available on every Unix-based computer by default. Once you have established an SSH connection with a remote computer, you will largely be free to interact with that computer as though you were physically sitting in front of it, at the keyboard, logged in through your user account. Most bioinformatics work carried out on remote computers is facilitated by SSH.

The easiest way to connect to a remote computer through the SSH protocol is to install an SSH client.

Complete the steps in the [SSH](https://github.com/WUSTL-Biol4220/home/blob/main/how_to_guide.md#secure-shell-ssh) section in the "How To" guide.

Now your home computer has a way to remotely interact with other computers on the network.

---

## 4. Connecting to your lab computer (your virtual machine)

In Biol 4220, each student will have access to their own personal computer, located on the WUSTL private network. All student computers are configured in the exact same way: they are all running the Linux operating system, [Ubunutu 24.04 LTS](https://releases.ubuntu.com/24.04/), and they are all pre-configured with the software required to complete the Biol 4220 lab exercises.

One thing to know is that these lab computers are not *physical computers*, but *virtual machines* or (VMs). As the name suggests, a VM is a computer hardware system that is emulated using software. This emulation is called *virtualization*. VMs are typically hosted by a VM server that specializes in virtualization, and is responsible for managing shared *physical* hardware resources -- such as processor time, memory, disk storage -- across the VMs that it is hosting, as well as backing up VMs, rebooting VMs, copying VMs, etc. Virtualization is an extremely useful technology, because it allows you to safely control and replicate your software environment, making certain software configurations extremely portable across diverse computing infrastructures. (For wet lab folks, imagine if you could "clone" your bench setup and mail it to a collaborating lab!)

Complete the steps in the [VM section](https://github.com/WUSTL-Biol4220/home/blob/main/how_to_guide.md#lab-virtual-machines-vm) in the "How To" guide.

Now you know how to connect to your VM.

Take a moment to reflect on what you've done so far. First, you connected to the WUSTL network, either by being on the WUSTL campus or by connecting to the WUSTL VPN. Second, you initiated an SSH connection to your VM through your SSH client. Third, you authenticated yourself against the VM's operating system (Ubuntu) using your username and password. This demonstrates elemental tasks and technologies can be combined into incredibly useful workflows. This will be a recurring theme in the course.


---

## 5. Create a GitHub account

It was mentioned earlier that this course will use the [GitHub](https://github.com) website for various purposes. All students will need a GitHub account to accept and complete the lab exercises.

If you already have a GitHub account, make sure you know your account name and password.

Students who do not yet have a GitHub account should visit the [Create a GitHub account](https://github.com/WUSTL-Biol4220/home/blob/main/how_to_guide.md#create-a-github-account) section in the "How To" guide.

---

## 6. Accept your first GitHub Classroom assignment

Lab exercises (including this one!) will be assigned to students through the [Practical Bioinformatics (Fall 2024)](https://classroom.github.com/classrooms/69019055-practical-bioinformatics-2024) website, hosted by [GitHub Classroom](https://classroom.github.com).

Each lab exercise will include an *invitation link* at the top of the lab instructions (i.e. the `README.md` file, like this one). The invitation link for Lab 01 is [https://classroom.github.com/a/zIH-8t3B](https://classroom.github.com/a/Sn9nM1tN).

By clicking that link, you will inform GitHub Classroom that you've accepted the assignment. GitHub Classroom will then prepare your lab workspace on the code-sharing website GitHub. That workspace will be a *git repository* (or *repo* for short). Future labs will explore how to use the version control software, git. For now, we can essentially view a repo as a "smart folder" that can recall the entire history for how its contents have changed.

Visit the [Accept a GitHub Classroom assignment](https://github.com/WUSTL-Biol4220/home/blob/main/how_to_guide.md#accept-your-github-classroom-lab-assignment) section in the "How To" guide. *Note:* You will complete and submit your lab assignment through the GitHub website (see below). You do not need to use the command line for this part of the lab.

Accept the Lab 01 assignment and verify that you can access the *git repository* for your lab assignment through [GitHub](https://github.com). 
My GitHub username is mlandis, so my Lab 01 repo was created at https://github.com/WUSTL-Biol4220/lab-01-mlandis. After that workspace is prepared, all that's left is to complete your assignment (next section).


---

## 7. Complete your first GitHub Classroom assignment

We are finally in a position to complete your first lab exercise. The task itself for Lab 01 is extremely simple. We will create a file called `output.txt` that contains the text `Hello, world!` in our lab assignment repository. Then, we will submit lab repository to GitHub Classroom for grading.

Visit your Lab 01 assignment repository.

Click the 'Add file' button, then select the 'Create new file' option

<img src="https://raw.githubusercontent.com/WUSTL-Biol4220/home/main/assets/lab_01/git_class_create_file.png" width="350"/>

Name the file `output.txt` by entering that name about the 'Edit file' panel. In the 'Edit file' panel, enter the text: `Hello, world!`

<img src="https://raw.githubusercontent.com/WUSTL-Biol4220/home/main/assets/lab_01/git_class_wrong_text.png" width="350"/>

Scroll to the bottom of the window, enter a message, and click 'Commit change'

<img src="https://raw.githubusercontent.com/WUSTL-Biol4220/home/main/assets/lab_01/git_class_wrong_commit.png" width="350"/>

Done! Now your new file is saved to the repository for grading. Future labs will be submitted and graded in a similar way.
