# "How To" guide

This document serves as a quick reference for "how to" do basic tasks:
- Virtual private network (VPN)
- Secure shell (SSH)
- Lab virtual machines (VM)
- Connect to the WUSTL cluster
- Create a GitHub Classroom account
- Accept your lab assignment on GitHub Classroom
- Submit your assignment on GitHub Classroom

Technical details for how to use VPNs, VMs, `ssh`, `git`, etc. are provided in the [lecture and lab notes](schedule.md).

---

## Virtual private network (VPN)

VPN allows remote users with proper credentials to access private network resources, even when off-campus.

To use VPN, you'll will need to download and install the Cisco AnyConnect VPN client software. Follow the WUSTL IT instructions [here](https://insideartsci.wustl.edu/connect-network-through-vpn).
- Mac users running the Catalina OS (10.15) will install [this](https://wustl.box.com/s/89aq55v287hfnryfigdxig1j6k1v7fyl).
- All other Windows and Mac users will install by following this [link](https://vpn.wustl.edu/artsci).

Once the software is installed, to connect to the WUSTL VPN
- Open the Cisco AnyConnect VPN Client software
- Enter `vpn.wustl.edu/artsci` as the "VPN Service..." and click Connect
- When prompted, enter your WUSTL id for the Username and your WUSTL password for the Password.
- Click OK to connect to the WUSTL VPN

<img src="https://github.com/WUSTL-Biol4220/how_to/raw/master/assets/vpn_connect.png" width="250"/>

Please refer to the WUSTL [Connect](https://it.wustl.edu/items/connect/) resources if you have problems connecting. If your problem persists, please let the instructor know.

---

## Secure shell (SSH) 

SSH is an encrypted protocol for securely communicating with devices on the network. We will connect to several key computational resources, such as our lab virtual machines and the WUSTL cluster, using VPN and SSH in combination.

Users with Unix-based operating systems, such as Linux and Mac OS X, will use the pre-installed `ssh` program to establish SSH connections through terminal.

Windows users will need to install an SSH client to use various resources that are essential to completing the labs. Labs will generally assume that Windows users are connecting with [PuTTy](https://www.putty.org/).

--- 

## Lab virtual machines (VM)

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

Lab VMs are preinstalled with (hopefully) all of the necessary software to complete the lab exercises. For various reasons, you will not have full admin access over your Lab VMs. If you find your Lab VM is no longer in a fully operational state, please let the instructor know so we can either fix your issue or provide you with a new VM.

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

## Accept a lab assignment

Lab assignments will be posted to the Biol 4220 [GitHub Classroom]() near the start of each class. When a new assignment is posted, students will receive an email with an invitation link to begin their assignment.

You must accept the assignment in order to complete and submit it properly! At first, this procedure might feel burdensome, but it will become easier as the course proceeds.

Accepting the assignment will tell GitHub Classroom to create a personal copy of the lab assignment for you as a new GitHub workspace, called a *repository*.

When you first click on the invite link, you will need to "Authorize GitHub Classroom App" to have permission to interact with your primary GitHub account:

<img src="https://github.com/WUSTL-Biol4220/how_to/raw/master/assets/github_class_authorize.png" width="150"/>

Next, you'll select your name from the course roster, and confirm that you are this person:

<img src="https://github.com/WUSTL-Biol4220/how_to/raw/master/assets/github_class_confirm_name.png" width="150"/>

You'll then be asked to accept the assignment:

<img src="https://github.com/WUSTL-Biol4220/how_to/raw/master/assets/github_class_accept_assignment.png" width="150"/>

Once you accept, GitHub Classroom will create a personal repository for your work for the lab exercise:

<img src="https://github.com/WUSTL-Biol4220/how_to/raw/master/assets/github_class_create_repo.png" width="150"/>

Upon completion, GitHub Classroom will provide a link to your new GitHub repository for the lab assignment:

<img src="https://github.com/WUSTL-Biol4220/how_to/raw/master/assets/github_class_assignment_accepted.png" width="150"/>

Clicking the second link will take you to the GitHub repository for your lab assignment:

<img src="https://github.com/WUSTL-Biol4220/how_to/raw/master/assets/github_class_assignment_repo.png" width="150"/>

---

## Complete your lab assignment on your VM

After you have accepted a lab assignment, you will need to
1. copy the GitHub repository for the lab assignment to your VM
2. complete the lab instructions
3. save any completed work to the repository for the lab assignment
4. submit your repository for grading on GitHub Classroom

Assignments must be submitted within 7 calendar-days (168 hours) from the start of a given class to receive full credit.

If your GitHub username is `mlandis` and the lab your completing is `lab-1a`, then the 

1. SSH into your VM and log in
2. Enter to your project directory: `cd ~/projects`
3. Clone a copy of your repository for the lab assignment: `git clone git@github.com:WUSTL-Biol4220/lab-1a-mlandis.git`
4. Enter your new lab assignment directory: `cd lab-1a-mlandis`
5. Carefully read the `README.md` file and follow the instructions: `nano README.md`
6. Complete your laboratory assignment!

While completing your assignment, you can save your work using the commands `git add <filename>` and `git commit`. For more details on how to use `git` to save your work, see the Lab XX.

When you're ready to submit your lab assignment
1. Make sure all of your files are are saved and committed
2. Update your GitHub repository with your changes: `git push`
3. Visit the GitHub Classroom to see if your lab is correct: https://classroom.github.com/classrooms/69019055-practical-bioinformatics-f2020/assignments/example-lab
  a. If your 

