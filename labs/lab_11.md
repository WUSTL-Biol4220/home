# Lab 11

*Lab 11 GitHub Classroom link:* https://classroom.github.com/a/-0i1prbi

In this short lab, we will learn about the WUSTL RIS cluster and how to interact with the cluster.

1. RIS cluster orientation
2. Scheduling jobs with LSF

Future labs and the course project may involve cluster usage.

---

## RIS cluster orientation

WUSTL Research Infrastructure Services (RIS) provides campus researchers with access to a compute platform and a storage platform. The two platforms interact, but we'll focus on how to use the [compute platform](https://ris.wustl.edu/services/compute/).

To improve the user experience with RIS compute services, RIS publishes a [user manual](https://confluence.ris.wustl.edu/display/RSUM/RIS+Services+User+Manual) and [knowledgebase articles](https://confluence.ris.wustl.edu/display/ITKB/RIS+IT+Knowledge+Base), and staffs a responsive [service desk](https://jira.ris.wustl.edu/servicedesk/customer/portal/1). RIS also offers several [workshops](https://confluence.ris.wustl.edu/display/ITKB/Workshops+and+Training) to orient new users to scientific computing through the cluster.

To use the cluster, we first need to connect to it. The cluster is on the WUSTL private network, just like your VM.  meaning you will need to connect to VPN, then SSH into the cluster.

Recall that HPC environments are composed of many nodes that provide different services to users, including *head nodes* that host SSH sessions for remote users and schedule jobs, and including *compute nodes* that process jobs assigned by the scheduler.

On the WUSTL HPC, there are four head nodes called `compute1-client-1.ris.wustl.edu`, `compute1-client-2.ris.wustl.edu`, `compute3-client-1.ris.wustl.edu`, and `compute4-client-1.ris.wustl.edu`. These head nodes interface with the HPCs only current compute cluster `compute1`.


To access the head node, you will SSH using your WUSTL key. For example, my email address is `michael.landis@wustl.edu`, so I can connect to a head node using the command
```console
$ ssh michael.landis@compute1-client-1.ris.wustl.edu
You are connecting to RIS Compute services.
Membership in a compute-* AD group is required.

Users are responsible for acting in accordance with
policies applicable to Washington University St. Louis.

https://confluence.ris.wustl.edu/display/RSUM/RIS+Compute+%3A+User+Agreement
michael.landis@compute1-client-1.ris.wustl.edu's password:
Last login: Sun Oct 25 11:59:00 2020 from 128.252.107.1
[michael.landis@compute1-client-1 ~]$
```

Our user account belongs to a number of user `groups`
```console
[michael.landis@compute1-client-1 ~]$ groups
domain users compute storage-home1-home-ro storage-bga-gmsroot-ro storage-bga-site-locks-rw storage-bga-shared-ro compute-workshop storage-mcallawa-shared-ro storage-ris-sas-ro storage-michael.landis compute-michael.landis compute-artsci storage-workshops-bio4220-rw
```
where our account's membership in `storage-workshops-bio4220-rw` and `compute-artsci` determines what resources we have access to, how our use of resources will be billed, etc.

### Home

The user `michael.landis` has access to three major storage directories. First, the user's `$HOME` directory, which has fast access times but is relatively small (10GB) in size. This is generally where you would store user configuration files, like `~/.profile`, and manage user binaries and libraries, e.g. `~/.local/bin` and `~/.local/lib`.

```console
[michael.landis@compute1-client-1 ~]$ echo $HOME
/home/michael.landis
```

### Scratch

On most clusters, each user also has a scratch directory (e.g. `/scratch1/fs1/michael.landis`) which does not have strict size limits, but files are deleted sporadically by RIS administrators and policies. This is typically where you would write output for programs. Important output would be copied to permanent storage before it is automatically deleted by RIS. *Note: most students will not have access to a scratch space unless they belong to the storage group associated with a research lab.*

```console
[michael.landis@compute1-client-1 ~]$ cd /scratch1/fs1/michael.landis
[michael.landis@compute1-client-1 michael.landis]$ pwd
/scratch1/fs1/michael.landis
[michael.landis@compute1-client-1 michael.landis]$ cat RIS_usage_report.txt
Generated on 2020-10-25
Space consumed by users:
root 4370 B
Space consumed by paths:
/scratch1/fs1/michael.landis/ 4096 B
/scratch1/fs1/michael.landis/RIS_usage_report.txt 274 B
/scratch1/fs1/michael.landis/.mmfind.found 0 B
/scratch1/fs1/michael.landis/.mmfind.policy 0 B
```

### Storage

Finally, members of the `storage-workshops-bio4220-rw` group have shared access to persistent storage in the `/storage1/fs1/workshops/Active/BIO4220` directory. Large files or directories that you need to use on a regular basis can be stored here, e.g. input datasets, source code for compiled binaries, GitHub projects, etc.

```console
[michael.landis@compute1-client-1 michael.landis]$ cd /storage1/fs1/workshops/Active/BIO4220
[michael.landis@compute1-client-1 BIO4220]$ pwd
/storage1/fs1/workshops/Active/BIO4220
[michael.landis@compute1-client-1 BIO4220]$ ls
dataset  users
```

Make a directory for your work:

```console
[michael.landis@compute1-client-1 BIO4220]$ mkdir -p users/${USER}
[michael.landis@compute1-client-1 BIO4220]$ cd users/${USER}
[michael.landis@compute1-client-1 BIO4220]$ pwd
/storage1/fs1/workshops/Active/BIO4220/users/michael.landis
```

If you are part of a research team here at WUSTL, you might also have membership to groups such as `storage-account.name` and `compute-account.name`, where `account.name` is the head of the research team. In that case, you would also have access to `/storage1/fs1/account.name`, which is a shared directory for your research group. This directory is backed up with daily snapshots, where `Archive` data is read-only, used rarely, but regularly backed up to tape. Most clusters impose a disk quota on storage directories, to prevent individual users from using all the shared disk space.

**Where should you store your files?**
- Use the *home directory for smaller personal files*. You should aim to store less than 1GB in your home directory.
- Use the *scratch directory for working or temporary files* that are generated as part of an analysis. For example, your code may need to generate and process 10GB of files to produce a small output file with analyzed results. Remember that you need to copy final versions of files to the stable storage directory.
- Use the *storage directory for large and important files* that should persist on the filesystem. For example, a large 5TB dataset unprocessed raw sequence data that is being analyzed by a team of researchers should be saved in shared storage.


## Scheduling jobs with LSF

The RIS cluster uses IBM's Platform Load Sharing Facility software (LSF) to schedule jobs. IBM provides excellent documentation for LSF, including a basic [user's guide](https://www.ibm.com/support/knowledgecenter/SSWRJV_10.1.0/lsf_welcome/lsf_kc_foundations_user.html) and a list of [LSF commands](https://www.ibm.com/support/knowledgecenter/SSWRJV_10.1.0/lsf_welcome/lsf_kc_cmd_ref.html). For this lab, we'll only explore the small number of commands that are typically used to manage jobs through LSF.

To use the full power of the RIS cluster, users submit jobs to a queue. The scheduling software then prioritizes each job in each queue based on factors such as fair usage among users (e.g. based on past use), total system resources, resources requested per job, queue-level priorities, user-level priorities, and other similar factors. While the job is in the queue, it may have a variety of statuses, including running, pending, and suspended. Users may choose to cancel jobs that have not completed. Completed jobs will generate output, that can then be moved among directories known to the cluster, or copied off the cluster to a remote workstation (e.g. your laptop).

The central challenge in using a cluster efficiently is: how to define manageable units of work that can be submitted and managed as jobs?

To orient ourselves, first list all of the queues available for processing jobs
```
[michael.landis@compute1-client-1 ~]$ bqueues | head -n5
QUEUE_NAME      PRIO STATUS          MAX JL/U JL/P JL/H NJOBS  PEND   RUN  SUSP
datatransfer     10  Open:Active       -    -    -    -     0     0     0     0
general-interac  10  Open:Active       -   64    -    -  3452  3277   175     0
dragen-2         10  Open:Active       -    -    -    -     0     0     0     0
dragen-2-intera  10  Open:Active       -    -    -    -     0     0     0     0
...
```
where the field `QUEUE_NAME` reports the queues you can see, `PRIO` reports the default priority of jobs in the queue, where (all else being equal) high priority jobs are processed before low priority jobs; `STATUS` reports whether each queue is fully functioning; `MAX` reports the maximum number of job slots that can be used to process jobs in the queue; `JL/U` and `JL/P` and `JL/H` give the max number of jobs per user, jobs per X , abd jobs per X. `NJOBS` gives the total number of job slots allowed in the queue; `PEND` gives the number of jobs waiting to be analyzed; `RUN` gives the number of jobs currently being processed; and `SUSP` gives the number of suspended jobs in the queue.


Next, list the compute nodes available for processing jobs scheduled across queues
```
[michael.landis@compute1-client-1 ~]$ bhosts | head -n5
HOST_NAME          STATUS       JL/U    MAX  NJOBS    RUN  SSUSP  USUSP    RSV
compute1-dragen-2. ok              -     24      0      0      0      0      0
compute1-dragen-3. ok              -     24     20     20      0      0      0
compute1-dragen-4. ok              -     32      0      0      0      0      0
compute1-dragen-5. closed          -     32     32     32      0      0      0
```
where `HOST_NAME` is the compute node's name, `STATUS` reports whether that node is functioning (`ok`) or not, `JL/U` reports the ma number of jobs per user, `MAX` is the job slots for the node, `NJOBS` is the number of jobs assigned to the node, `RUN` is the number of actively running jobs, `SSUSP` is the number of jobs suspended by the system (e.g. due to policy violation), `USUSP` is the number of jobs suspended by users (e.g. by an administrator), and `RSV` is the number of reserved slots in use.

Let's submit our first job to the LSF scheduler
```console
[michael.landis@compute1-client-1 ~]$ bsub -G compute-workshop \
                                           -Is -q general-interactive \
                                           -a 'docker(alpine)' \
                                           'echo -e "Hello, world!"'
Job <285964> is submitted to queue <general-interactive>.
<<Waiting for dispatch ...>>
<<Starting on compute1-exec-130.ris.wustl.edu>>
Using default tag: latest
latest: Pulling from library/alpine
Digest: sha256:beefdbd8a1da6d2915566fde36db9db0b524eb737fc57cd1367effd16dc0d06d
Status: Image is up to date for alpine:latest
docker.io/library/alpine:latest
Hello, world!
[michael.landis@compute1-client-1 ~]$
```

The anatomy of the command is as follows:
- `bsub` : submits a job to the LSF queue
- `-G compute-workshop` : determines which compute group to use for processor time
- `-Is` : run the job as an interactive session and create a pseudoterminal, meaning you can view the output directly
- `-q general-interactive` : run the job in the `general-interactive` queue, which allows interactive sessions (`-Is`)
- `-a 'docker(alpine)'` : run the job using a Docker container running Ubuntu-derived operating system, Alpine
- `'echo -e "Hello, world!"'` : the command string we want our job to execute, which should print `Hello, world!` to screen

This job runs almost instantaneously, and prints `Hello, world!` before completing. The job runs so quickly, that it can't be used to demonstrate how to monitor (`bjobs`) and cancel (`bkill`) jobs. This time, will run a job that runs the command `sleep 1000` submitted as a non-interactive job, which tells the compute to do nothing for 1000 seconds.

```console
[michael.landis@compute1-client-1 ~]$ bsub -G compute-workshop -q general -a 'docker(alpine)' 'echo Waiting; sleep 60; echo ...done!'
Defaulting to LSF user group 'compute-workshop'
Job <93149> is submitted to queue <general>.
[michael.landis@compute1-client-1 ~]$ bjobs
JOBID   USER    STAT  QUEUE      FROM_HOST   EXEC_HOST   JOB_NAME   SUBMIT_TIME
93149   michael PEND  general    compute1-cl             * ...done! Oct 25 16:02
[michael.landis@compute1-client-1 ~]$ bjobs
JOBID   USER    STAT  QUEUE      FROM_HOST   EXEC_HOST   JOB_NAME   SUBMIT_TIME
93149   michael RUN   general    compute1-cl compute1-ex * ...done! Oct 25 16:02
[michael.landis@compute1-client-1 ~]$ bkill 93149
Job <93149> is being terminated
[michael.landis@compute1-client-1 ~]$ bjobs
No unfinished job found
```

To record metadata regarding the processed job, such as run time and resource usage, we can provide the `-o` flag

```console
[michael.landis@compute1-client-1 ~]$ cat output.txt
'Hello, world!'
[michael.landis@compute1-client-1 ~]$ bsub -G compute-workshop -q general -a 'docker(alpine)' -o job.log "echo -e \'Hello, world\!\' > output.txt"
Defaulting to LSF user group 'compute-workshop'
Job <93159> is submitted to queue <general>.
[michael.landis@compute1-client-1 ~]$ tail -n25  job.log

Using default tag: latest
latest: Pulling from library/alpine
Digest: sha256:beefdbd8a1da6d2915566fde36db9db0b524eb737fc57cd1367effd16dc0d06d
Status: Image is up to date for alpine:latest
docker.io/library/alpine:latest

------------------------------------------------------------
Sender: LSF System <lsfadmin@compute1-exec-148.ris.wustl.edu>
Subject: Job 286134: <echo -e \'Hello, world\!\' > output.txt> in cluster <compute1-lsf> Done

Job <echo -e \'Hello, world\!\' > output.txt> was submitted from host <compute1-client-1.ris.wustl.edu> by user <michael.landis> in cluster <compute1-lsf> at Mon Sep 30 11:57:16 2024
Job was executed on host(s) <compute1-exec-148.ris.wustl.edu>, in queue <general>, as user <michael.landis> in cluster <compute1-lsf> at Mon Sep 30 11:57:17 2024
</home/michael.landis> was used as the home directory.
</home/michael.landis> was used as the working directory.
Started at Mon Sep 30 11:57:17 2024
Terminated at Mon Sep 30 11:57:37 2024
Results reported at Mon Sep 30 11:57:37 2024

Your job looked like:

------------------------------------------------------------
# LSBATCH: User input
echo -e \'Hello, world\!\' > output.txt
------------------------------------------------------------

Successfully completed.

Resource usage summary:

    CPU time :                                   10.16 sec.
    Max Memory :                                 33 MB
    Average Memory :                             16.75 MB
    Total Requested Memory :                     4096.00 MB
    Delta Memory :                               4063.00 MB
    Max Swap :                                   -
    Max Processes :                              5
    Max Threads :                                15
    Run time :                                   25 sec.
    Turnaround time :                            21 sec.

The output (if any) is above this job summary.
```

The output of `job.log` often contains valuable information, especially for debugging the cause of job to fail.

Transferring small files to and from RIS can be done using secure copy (`scp`). `scp` behaves similarly to standard `cp`, except you must also provide the network (IP) address and login credentials to complete the copy. Servers generally have a fixed IP address where the IP addresses of most user computers are randomly allocated. Because of this, we will assume the following commands are run from your workstation -- i.e., physical computer in front of you, not the virtual machine.

To copy a file called `input.txt` from your physical computer on to RIS, you would type
```console
$ echo "Hello, world!" > input.txt
$ scp input.txt michael.landis@compute1-client-1.ris.wustl.edu:/home/michael.landis/input.txt
You are connecting to RIS Compute services.
Membership in a compute-* AD group is required.

Users are responsible for acting in accordance with
policies applicable to Washington University St. Louis.

https://confluence.ris.wustl.edu/display/RSUM/RIS+Compute+%3A+User+Agreement
michael.landis@compute1-client-1.ris.wustl.edu's password:
input.txt                                    100%   14     3.4KB/s   00:00

```

Notice how the destination filepath string is constructed:
- `michael.landis` is the username to authenticate
- `@` indicates that the remaining text will locate the destination
- `compute1-client-1.ris.wustl.edu` is the destination server
- `:` indicates the next text is the path for the file on the destination server's filesystem
- `/home/michael.landis/test.txt` is where the file will be stored on the destination server

You will need to modify the remote username, address, and filepath depending on your authentication information, the server you're working with, and the location of your remote files.

Treating RIS as the source and your workstation as the destination allows you to transfer files into the local directory of your filesystem. 
```
$ scp michael.landis@compute1-client-1.ris.wustl.edu:/home/michael.landis/output.txt output.txt
$ scp michael.landis@compute1-client-1.ris.wustl.edu:/home/michael.landis/job.log job.log
```

**Note:** currently, network restrictions prevent us from copying files directly between our VMs and the RIS servers. We're working on a way to enable this functionality or an alternative method for file transfer.

Another way would be use GitHub to synchronize files on the server with a remote repository. Before using `git` to synchronize files, you'll need to create a new  security key for your RIS session, then share the public key with GitHub. We configured these keys on the first day for your laptops, following these instructions ([link](https://github.com/WUSTL-Biol4220/home/blob/main/how_to_guide.md#add-ssh-key-to-github-account)). Follow these instructions again, this time from within the home directory for an RIS session.

Afterwards, your RIS account should be able to use GitHub. Try running these commands:

```console
$ mkdir -p projects
$ git clone git@github.com:WUSTL-Biol4220/lab-11-mlandis.git
$ mv ./lab-11-mlandis ./projects/lab-11-mlandis
$ mv output.txt projects/lab-11-mlandis
$ mv job.log projects/lab-11-mlandis
$ cd ~/projects/lab-11-mlandis
$ git add job.log
$ git add output.txt
$ git commit -am 'add log/txt'
$ git push
```

Now the files you produced on the cluster are now synchronized with the remote repository online. To synchronize the files with your computer, you'll need to clone and pull changes from the GitHub repository:

```console
$ # navigate to the directory where you store lab repositories
$ git clone git@github.com:WUSTL-Biol4220/lab-11-mlandis.git
$ cd lab-11-mlandis
$ git pull
```

That's all we'll cover in this tutorial. Later labs may use RIS to assemble raw sequence data into genomes. You are certainly encouraged to use RIS or other server resources to complete your course project.

For more advanced tutorials on file transfer involving RIS, visit: https://docs.ris.wustl.edu/doc/storage/03_storage.html#moving-data-into-the-storage-service.

---

Clone the Lab 11 repo to the cluster, then commit and push `history > history.txt` to the cloned repo to complete the assignment.




