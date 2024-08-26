# "How To" guide

This document serves as a quick reference for "how to" do basic tasks:
- [Virtual private network (VPN)](https://github.com/WUSTL-Biol4220/home/blob/main/how_to_guide.md#virtual-private-network-vpn)
- [Secure shell (SSH)](https://github.com/WUSTL-Biol4220/home/blob/main/how_to_guide.md#secure-shell-ssh)
- [Lab virtual machines (VM)](https://github.com/WUSTL-Biol4220/home/blob/main/how_to_guide.md#lab-virtual-machines-vm)
- [Create a GitHub account](https://github.com/WUSTL-Biol4220/home/blob/main/how_to_guide.md#create-a-github-account)
- [Add SSH Key to GitHub account](https://github.com/WUSTL-Biol4220/home/blob/main/how_to_guide.md#add-ssh-key-to-github-account)
- [Create a GitHub personal authentication token (PAT)](https://github.com/WUSTL-Biol4220/home/blob/main/how_to_guide.md#create-a-github-personal-authentication-token-pat)
- [Accept your GitHub Classroom lab assignment](https://github.com/WUSTL-Biol4220/home/blob/main/how_to_guide.md#accept-your-github-classroom-lab-assignment)
- [Submit your GitHub Classroom lab assignment](https://github.com/WUSTL-Biol4220/home/blob/main/how_to_guide.md#complete-your-github-classroom-lab-assignment)

Technical details for how to use VPNs, VMs, `ssh`, `git`, etc. are provided in the [course lecture & lab notes](course_schedule.md).

---

## Virtual private network (VPN)

VPN allows remote users with proper credentials to access private network resources, even when off-campus. To complete most lab assignments in this course, students will need to connect to resources on WUSTL's private network, such as the lab computers or the campus servers.

Note that VPN will only work properly if you are off-campus. You may receive an error or notice unusual access to network resources if you attempt to connect to the VPN while on-campus.

WUSTL undergraduates can install the necessary VPN software and connect to the VPN by following the directions listed here: https://computing.artsci.wustl.edu/connect-network-through-vpn

Once the software is installed, to connect to the WUSTL VPN
- Open the Cisco AnyConnect VPN Client software
- Enter `danforthvpn.wustl.edu` as the "VPN" and click Connect
- When prompted, enter your WUSTL id for the Username and enter the text `push`, `sms`, or `phone` (see guide for details) for the "Second password".
- Accept the security check through your device for 2FA (two factor authentication)
- Click OK to connect to the WUSTL VPN
- If the connection succeeds, the Cisco VPN client window will read `Connected to danforthvpn.wustl.edu` with a green checkmark.

<img src="assets/how_to/vpn_connect_success.png" width="250"/>

If your problem persists, please let the instructor know or contact the WUSTL [IT department](it.wustl.edu).

---

## Secure shell (SSH) 

SSH is an encrypted protocol for securely communicating with devices on the network. We will connect to several key computational resources, such as our lab virtual machines, using VPN and SSH in combination. You can read more about SSH [here](https://en.wikipedia.org/wiki/Secure_Shell).

* **Linux and Mac OS X.** Users with Unix-based operating systems, such as Linux and Mac OS X, will use the pre-installed `ssh` program to establish SSH connections through terminal. If you want to open an SSH connection to a particular IP address (e.g. `192.168.1.1`), you will open a terminal session, then type `ssh  192.168.1.1` and press enter. (**Note:** this is only an example command that you do not need to execute.) If you execute `ssh` without providing a target address, the computer will report different options for how you might use `ssh` (i.e. output reads `usage: ssh` followed by various flags). Please notify the instructor if your command prompt instead reports `command not found: ssh`.

* **Windows.** Windows users will need to install an SSH client to use various resources that are essential to completing the labs. Labs will generally assume that Windows users are connecting with [PuTTy](https://www.putty.org/). To open an SSH session with PuTTY, you will double-click the application, enter the appropriate address into the "Host Name or IP address" field, enter `22` into the "Port" field, then click "Open".

After initiating an SSH connection with a remote host, the users typically needs to provide credentials (a username and password) to authenticate and establish the SSH connection. Those details are covered elsewhere.

--- 

## Lab virtual machines (VM)

Our class will use virtual machines (or VMs) to complete laboratory exercises. Every student will be given their own personal VM to use. Each VM is preinstalled with Ubuntu (24.04 LTS) along with the software packages that are necessary to complete the course's lab assignments. For security purposes, your VM is only accessible through the WUSTL private network.

Students who are off-campus will need to first connect to the [VPN](https://github.com/WUSTL-Biol4220/home/blob/main/how_to_guide.md#virtual-private-network-vpn) before they can connect to their VM.
 
Students that are on-campus or connected through the VPN can access their VM is through [SSH](https://github.com/WUSTL-Biol4220/home/blob/main/how_to_guide.md#secure-shell-ssh).

To log in to your VM, you'll need to supply three key pieces of information:
1. `ip_address` -- the unique IP address assigned to your VM
2. `username` -- your VM username, which is identical to your WUSTL id
3. `password` -- your VM password, which you'll set upon first login

Each student will have their own `username`, `password`, and `ip_address`. In the below examples, let's pretend the student's username is `mlandis` and their IP address is `128.252.111.111`. *NOTE: These are example values; the instructor will provide you with your username, password, and IP address.*

### SSH for Linux and Mac users
1. Open the Terminal program
2. Type `ssh mlandis@128.252.111.111` into the command prompt and press enter

### SSH for Windows users
1. Open PuTTY
2. Enter `128.252.111.111` into the "Host Name or IP address" field
3. Enter `22` into the "Port" field
4. Click "Open"

At this point, you will have initiated your SSH connection,

you should be prompted to enter your password (your entered text will be invisible)
```
mlandis@128.252.111.111's password:
```
after correctly entering your password, you will see a welcome message similar to
```
Welcome to Ubuntu 24.04 LTS (GNU/Linux 6.8.0-1013-aws x86_64)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/pro

 System information as of Fri Aug 23 16:07:35 UTC 2024

  System load:  0.0                Temperature:           -273.1 C
  Usage of /:   53.8% of 37.70GB   Processes:             109
  Memory usage: 33%                Users logged in:       0
  Swap usage:   0%                 IPv4 address for ens5: 172.30.14.77

 * Ubuntu Pro delivers the most comprehensive open source security and
   compliance features.

   https://ubuntu.com/aws/pro

Expanded Security Maintenance for Applications is not enabled.

19 updates can be applied immediately.
6 of these updates are standard security updates.
To see these additional updates run: apt list --upgradable

Enable ESM Apps to receive additional future security updates.
See https://ubuntu.com/esm or run: sudo pro status


*** System restart required ***
Last login: Thu Aug 22 17:46:24 2024 from 128.252.25.9
mlandis@ip-172-30-14-77:~$
```

This last line (`mlandis@biol4220-mlandis:~$`) indicates that you have successfully SSH'd into your lab VM, and that the VM is ready to receive your commands!

To terminate your SSH session, type `exit` at the command prompt
```
mlandis@biol4220-mlandis:~$ exit
logout
Connection to 128.252.111.111 closed.
```

If you can't establish an SSH connection with your VM, please contact the instructor for help.

Lab VMs are preinstalled with all of the software needed to complete the lab exercises. For various reasons, you will not have full admin access over your Lab VMs. If you need additional software installed, or if you find your Lab VM is no longer in a fully operational state, please let the instructor know so we can either fix your issue or provide you with a new VM.

---

## Create a GitHub account

Programmers and researchers use a tool called `git` to save and share their work. (We'll learn how to use `git` during the course itself.) Our course will use GitHub, a service that hosts `git` projects for free. If you do not currently have a GitHub account, you'll need to create one.

Visit https://github.com, then supply a username, your email address, and a password to create a GitHub account. If you provide your `@wustl.edu` email address, then you may qualify for special account perks through [GitHub Education](https://education.github.com/).

Here is what the account creation prompt looks like:

<img src="assets/how_to/github_new_account.png" width="250"/>

---

## Add SSH key to GitHub account

You can simplify how you access GitHub from your virtual machine by first generating a unique SSH key on your virtual machine then registering that key with your GitHub account. Registering the SSH key allows you to bypass repeated and somewhat tedious username/password authentication.

To generate an SSH key, log into your virtual machine then type
```
$ mkdir -p ~/.ssh && cd ~/.ssh && ssh-keygen
```
When asked, use the default location to save the key then enter and re-enter your key's password (a blank password will be accepted but is not ideal).
```
Generating public/private rsa key pair.
Enter file in which to save the key (/home/mlandis/.ssh/id_rsa):
Enter passphrase (empty for no passphrase):
Enter same passphrase again:
Your identification has been saved in /home/mlandis/.ssh/id_rsa
Your public key has been saved in /home/mlandis/.ssh/id_rsa.pub
The key fingerprint is:
SHA256:fJFkgx52TrtiW0YBtNxszpExskQMmLUvhMI0Cy+J42k mlandis@bio4220testvm
The key's randomart image is:
+---[RSA 3072]----+
|. o  +o=*o*      |
|.= ..o ++O+*     |
|= * . oo+=Oo     |
|.o.. . =.++o     |
| E    . S.+.     |
|.      .o.+      |
|       . =       |
|        .        |
|                 |
+----[SHA256]-----+
```
Next, print and copy the contents of your new key file. **Important:** you must run this command on your virtual machine and copy the contents for your individual and unique `id_ed25519.pub` file. 
```
$ cat id_ed25519.pub
ssh-ed25519 xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx/xxxxxxxxxxxxx/xxxxxxxx mlandis@ip-172-30-14-77
```
**Important:** This key grants special access to your computer. Do not share it publicly. (The key printed above is a toy example and is invalid.)

The next step is to register your new key with your GitHub account.

- Click on your User Avatar in the upper right corner of the GitHub page
- Choose "Settings" from the dropdown menu
- Click "SSH and GPG keys" under "Access" on the menubar on the left
- Click the green "New SSH key" button in the upper right
- Enter the "Biol 4220 VM" as the Title, select "Authentication Key" (default) as the Key type, paste the copied contents of `id_rsa.pub` into the Key field, then click "Add SSH key".

<img src="assets/how_to/github_ssh_key.png" width="450"/>

That's it! Your SSH key is now registered with GitHub. This will make it easier for you to interact with GitHub from your virtual machine.

---

## Create a GitHub Personal Authentication Token (PAT)

*WARNING: you will not be able to register a PAT on your VM until after you have completed the `git` lab (Lab 03)*

GitHub uses Personal Authentication Tokens (or PATs) to control access to different GitHub resources (e.g. repositories) for each GitHub users. PATs function very similarly to passwords, except each PAT may (1) grant access to different resources and (2) have a different expiration date.

In general, you will need to create a PAT and register it on your VM to use GitHub through your VM. (You are free to configure your VM to authenticate with GitHub in an alternative manner if you prefer.)

To create a PAT for GitHub
1. Log in to GitHub
2. Click on your Account Manager (your account avatar in the upper right corner)
3. Click `Settings` from the dropdown menu
4. Click `Developer settings` from the left menu bar
5. Click `Personal access token` from the left menu bar
6. Click `Generate a personal access token` from the main text
7. Enter your GitHub credentials, if asked
8. You should now be at the website: https://github.com/settings/tokens/new

<img src="assets/how_to/github_pat_create.png" width="450"/>

9. For `Note` enter `Token for Biol 4220`
10. For `Expiration` set the custom date of 01/01/2022 (or longer if you prefer)
11. For `Select scopes` check off the `repo` and `workflow` fields
12. Click the green `Generate Token` button at the bottom of the page
13. Copy the text that reads `ghp_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx` to your clipboard

<img src="assets/how_to/github_pat_copy.png" width="450"/>

**NOTE:** The exact text of the PAT cannot be seen again after you leave the token-creation webpage. You do not need it again after registering the PAT into the VM (below). However, you may choose to copy the PAT to a local file on your computer if you are worried about losing it. Alternatively, you can always create and register a new PAT if the original copy is needed again for some reason.

To register the PAT on your VM
1. SSH on to your VM
2. Enter the command `git config --global credential.helper store`
3. When you next interact with GitHub that requires your credentials (e.g. using `git push` or `git pull`)
    - Enter your GitHub username in the username field
    - Enter the **PAT that you saved to your clipboard** into the password field
4. This will save your credentials as plain text in the file `~/.git-credentials` as `https://username:ghp_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx@github.com`. The command `cat ~/.git-credentials` will print this file to screen, if you want to take a peek.

Please see an instructor if you have difficulties configuring the PAT on your VM, if your credentials no longer work, or if you reset your PAT.


---

## Accept your GitHub Classroom lab assignment

Lab assignments will be posted to the Biol 4220 [GitHub Classroom]() near the start of each class. When a new assignment is posted, students will receive an email with an invitation link to begin their assignment.

You must accept the assignment in order to complete and submit it properly! At first, this procedure might feel burdensome, but it will become easier as the course proceeds.

Accepting the assignment will tell GitHub Classroom to create a personal copy of the lab assignment for you as a new GitHub workspace, called a *repository*.

When you first click on the invite link, you will need to "Authorize GitHub Classroom App" to have permission to interact with your primary GitHub account:

<img src="assets/how_to/github_class_authorize.png" width="150"/>

Next, you'll select your name from the course roster, and confirm that you are this person:

<img src="assets/how_to/github_class_confirm_name.png" width="150"/>

You'll then be asked to accept the assignment:

<img src="assets/how_to/github_class_accept_assignment.png" width="150"/>

Once you accept, GitHub Classroom will create a personal repository for your work for the lab exercise:

<img src="assets/how_to/github_class_create_repo.png" width="150"/>

Upon completion, GitHub Classroom will provide a link to your new GitHub repository for the lab assignment:

<img src="assets/how_to/github_class_assignment_accepted.png" width="150"/>

Clicking the second link will take you to the GitHub repository for your lab assignment:

<img src="assets/how_to/github_class_assignment_repo.png" width="150"/>

---

## Complete your GitHub Classroom lab assignment

After you have accepted a lab assignment, you will need to
1. copy the GitHub repository for the lab assignment to your VM
2. complete the lab instructions
3. save any completed work to the repository for the lab assignment
4. submit your repository for grading on GitHub Classroom

Assignments must be submitted within 7 calendar-days (168 hours) from the start of a given class to receive full credit.

If your GitHub username is `mlandis` and the lab your completing is `example-lab`, then the 

1. SSH into your VM and log in
2. Enter to your project directory: `cd ~/projects`
3. Clone a copy of your repository for the lab assignment: `git clone git@github.com:WUSTL-Biol4220/example-lab-mlandis.git`
4. Enter your new lab assignment directory: `cd example-lab-mlandis`
5. Carefully read the `README.md` file and follow the instructions: `nano README.md`
6. Complete your laboratory assignment!

While completing your assignment, you can save your work using the commands `git add <filename>` and `git commit`. For more details on how to use `git` to save your work, see Lab 03.

When you're ready to submit your lab assignment
1. Make sure all of your files are are saved and committed
2. Update your GitHub repository with your changes: `git push`
3. Visit your repository: https://github.com/WUSTL-Biol4220/example-lab-mlandis
  - If see a red 'X' by your newest commit, click the 'X'<br>
  <img src="assets/how_to/github_commit_fail.png" width="200"/>
  
  - Expand the 'autograding' step to identify the problem<br>
  <img src="assets/how_to/github_test_fail.png" width="200"/>
  
  - The test expects `output.txt` to contain `Hello, world!` not `Jello, warld!`
  - If you see a green checkmark next to the newest commit, click the checkmark<br>
  <img src="assets/how_to/github_commit_succeed.png" width="200"/>
    
  - Expand the 'autograding' step, and enjoy the celebratory fireworks<br>
  <img src="assets/how_to/github_test_succeed.png" width="200"/>

