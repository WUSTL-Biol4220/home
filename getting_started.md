# How to...

This document explains how to:
- Install the WUSTL virtual private network (VPN) software
- Install the secure shell (SSH) client (for Windows users)
- Connect to the WUSTL VPN
- Connect to your Biol 4220 virtual machine (VM)
- Connect to the WUSTL cluster
- Create a GitHub Classroom account
- Accept your lab assignment on GitHub Classroom
- Complete your lab assignment on your VM
- Submit your assignment on GitHub Classroom

Technical details for how to use VPNs, VMs, `ssh`, `git`, etc. are provided in the [lecture and lab notes](schedule.md).

---

## Install the WUSTL virtual private network (VPN) software

You will need to download and install the Cisco AnyConnect VPN client software. Follow the WUSTL IT instructions [here](https://insideartsci.wustl.edu/connect-network-through-vpn).

---

## Install the secure shell (SSH) client (for Windows users)

Windows users will need to install an SSH client to use various resources that are essential to completing the labs.

- [PuTTy](https://www.putty.org/)


Users with Unix-based operating systems, such as Linux and Mac OS X, will use the pre-installed `ssh` program to establish SSH connections.

---

## Connect to the WUSTL VPN

VPN allows remote users with proper credentials to access private network resources, even when off-campus.

Connecting to the WUSTL VPN requires three steps.

Once the software is installed, you'll then initiate your VPN connection. To connect to the WUSTL VPN
- Open the Cisco AnyConnect VPN Client software
- Enter `vpn.wustl.edu/artsci` as the "VPN Service..." and click Connect
- When prompted, enter your WUSTL id for the Username and your WUSTL password for the Password.
- Click OK to connect to the WUSTL VPN

<img src="https://github.com/WUSTL-Biol4220/how_to/raw/master/assets/vpn_connect.png" width="250"/>

Please refer to the WUSTL [Connect](https://it.wustl.edu/items/connect/) resources if you have problems connecting. If your problem persists, please let the instructor know.

--- 

## Connect to your Biol 4220 virtual machine (VM)

Our class will use VMs to complete laboratory exercises. Each VM is preinstalled with Ubuntu (version XX) and the various packages (XXX) that are necessary to complete the lab assignments throughout the course.

Every student will be given their own personal VM to use. Students will connect to their VM principally using the *secure shell* network protocol (or ssh). You can read more about ssh [here](https://en.wikipedia.org/wiki/Secure_Shell).

To log in, you'll need to supply three key pieces of information
1. `ip_address` -- the unique IP address assigned to your VM; format is `172.21.xxx.xxx`
2. `username` -- your VM username, which is identical to your WUSTL id
3. `password` -- your VM password, which you'll set upon first login

If you are off-campus, you will need to first connect to the WUSTL VPN.

### SSH for Linux and Mac users
1. Open terminal
2. Type `ssh username@ip_address` into the command prompt and press enter

### SSH for Windows users
1. Open PuTTY
2. Enter `address` into the "Host Name or IP address" field
3. Enter `22` into the "Port" field
4. Click "Open"

Once you connect, you should see the following prompt

```
michael.landis@host:~
```

---

## Connect to the WUSTL cluster

Many bioinformatics analyses are designed to be run using teams of computational servers, called clusters. Research Infrastructure Services, or [RIS](ris.wustl.edu), provides WUSTL with access to clusters and other high performance computing (HPC) services. We'll use the RIS HPC to learn more about processing bioinformatics tasks with clusters as part of our lecture and lab exercises.

To use RIS HPC, you will need to
1. Create a RIS HPC account
2. SSH to RIS HPC
3. Submit and process jobs

Details for how run analyses with RIS HPC are covered in [Lab X]().

---

## Create a GitHub account

Programmers and researchers use a tool called `git` to save and share their work. (We'll learn how to use `git` during the course itself.) Our course will use GitHub, a service that hosts `git` projects for free. If you do not currently have a GitHub account, you'll need to create one.

Visit https://github.com, then supply a username, your email address, and a password to create a GitHub account. If you provide your `@wustl.edu` email address, then you may qualify for special account perks through [GitHub Education](https://education.github.com/).

Here is what the account creation prompt looks like:

<img src="https://github.com/WUSTL-Biol4220/how_to/raw/master/assets/github_new_account.png" width="250"/>


---

## Load your assignment on to your VM

Lab assignments will be posted to the Biol 4220 [GitHub Classroom]() near the start of each class. When a new assignment is posted, students will receive an email with an invitation link to begin their assignment.

When you first click on the invite link, you will need to "Authorize GitHub Classroom App" to have permission to interact with your primary GitHub account:
- <img src="https://github.com/WUSTL-Biol4220/how_to/raw/master/assets/github_class_authorize.png" width="150"/>

Next, you'll select your name from the course roster, and confirm that you are this person:
- <img src="https://github.com/WUSTL-Biol4220/how_to/raw/master/assets/github_class_confirm_name.png" width="150"/>

You'll then be asked to accept the assignment:
- <img src="https://github.com/WUSTL-Biol4220/how_to/raw/master/assets/github_class_accept_assignment.png" width="150"/>

Once you accept, GitHub Classroom will create a personal repository for your work for the lab exercise:
- <img src="https://github.com/WUSTL-Biol4220/how_to/raw/master/assets/github_class_create_repo.png" width="150"/>

Upon completion, GitHub Classroom will provide a link to your new workspace on `github.com`:
- <img src="https://github.com/WUSTL-Biol4220/how_to/raw/master/assets/github_class_assignment_accepted.png" width="150"/>

Clicking the second link will take you to your lab workspace:
- <img src="https://github.com/WUSTL-Biol4220/how_to/raw/master/assets/github_class_assignment_repo.png" width="150"/>




---

## Complete your lab assignment on your VM

To complete your lab assignment, you will need to
- clone a copy of your repository to your VM
- follow the lab instructions
- commit any changes to your repository as you go along


---

## Submit your lab assignment to GitHub Classroom

Assignments must be submitted within 7 calendar-days (168 hours) from the start of a given class to receive full credit.

There are two important steps to submitting lab
