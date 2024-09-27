# Lab 11

*Lab 11 GitHub Classroom link:* https://classroom.github.com/a/Eku_G42u

In this short lab, we will learn about the WUSTL RIS cluster and how to interact with the cluster.

1. RIS cluster orientation
2. Scheduling jobs with LSF

Future labs and the course project may involve cluster usage.

---

## RIS cluster orientation

WUSTL Research Infrastructure Services (RIS) provides campus researchers with access to a compute platform and a storage platform. The two platforms interact, but we'll focus on how to use the [compute platform](https://ris.wustl.edu/services/compute/).

To improve the user experience with RIS compute services, RIS publishes a [user manual](https://confluence.ris.wustl.edu/display/RSUM/RIS+Services+User+Manual) and [knowledgebase articles](https://confluence.ris.wustl.edu/display/ITKB/RIS+IT+Knowledge+Base), and staffs a responsive [service desk](https://jira.ris.wustl.edu/servicedesk/customer/portal/1). RIS also offers several [workshops](https://confluence.ris.wustl.edu/display/ITKB/Workshops+and+Training) to orient new users to scientific computing through the cluster.

To use the cluster, we first need to connect to it. The cluster is on the WUSTL private network, just like your VMs, meaning you will need to connect to VPN, then SSH into the cluster.

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
domain users compute storage-home1-home-ro storage-bga-gmsroot-ro storage-bga-site-locks-rw storage-bga-shared-ro storage-mcallawa-shared-ro storage-ris-sas-ro storage-michael.landis compute-michael.landis
```
where our account's membership in `storage-michael.landis` and `compute-michael.landis` determines what resources we have access to, how our use of resources will be billed, etc.

The user `michael.landis` has access to three major storage directories. First, the user's `$HOME` directory, which has fast access times but is relatively small (10GB) in size. This is generally where you would store user configuration files, like `~/.profile`, and manage user binaries and libraries, e.g. `~/.local/bin` and `~/.local/lib`.

```console
[michael.landis@compute1-client-1 ~]$ echo $HOME
/home/michael.landis
```


Each user also has a scratch directory (e.g. `/scratch1/fs1/michael.landis`) which does not have strict size limits, but files are deleted sporadically by RIS administrators and policies. This is typically where you would write output for programs. Important output would be copied to permanent storage before it is automatically deleted by RIS.

```console
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

Finally, members of the `compute-michael.landis` group have shared access to `/storage1/fs1/michael.landis` directory, whose contents are persistent, but disk space is limited to 2.5TB. Large files or directories that you need to use on a regular basis are stored here, e.g. input datasets, source code for compiled binaries, GitHub projects, etc.

```console
[michael.landis@compute1-client-1 michael.landis]$ pwd
/storage1/fs1/michael.landis
[michael.landis@compute1-client-1 michael.landis]$ ls
Active  Archive  README.txt
```
where the `Active` directory is backed up with daily snapshots, where `Archive` data is read-only, used rarely, but regularly backed up to tape.

## Scheduling jobs with LSF

The RIS cluster uses IBM's Platform Load Sharing Facility software (LSF) to schedule jobs. IBM provides excellent documentation for LSF, including a basic [user's guide](https://www.ibm.com/support/knowledgecenter/SSWRJV_10.1.0/lsf_welcome/lsf_kc_foundations_user.html) and a list of [LSF commands](https://www.ibm.com/support/knowledgecenter/SSWRJV_10.1.0/lsf_welcome/lsf_kc_cmd_ref.html). For this lab, we'll only explore the small number of commands that are typically used to manage jobs through LSF.

To use the full power of the RIS cluster, users submit jobs to a queue. The scheduling software then prioritizes each job in each queue based on factors such as fair usage among users (e.g. based on past use), total system resources, resources requested per job, queue-level priorities, user-level priorities, and other similar factors. While the job is in the queue, it may have a variety of statuses, including running, pending, and suspended. Users may choose to cancel jobs that have not completed. Completed jobs will generate output, that can then be moved among directories known to the cluster, or copied off the cluster to a remote workstation (e.g. your laptop).

The central challenge in using a cluster efficiently is: how to define manageable units of work that can be submitted and managed as jobs?

To orient ourselves, first list all of the queues available for processing jobs
```
[michael.landis@compute1-client-1 ~]$ bqueues
QUEUE_NAME      PRIO STATUS          MAX JL/U JL/P JL/H NJOBS  PEND   RUN  SUSP
datatransfer     10  Open:Active       -    -    -    -     0     0     0     0
general          10  Open:Active       -    -    -    - 90936 90912    24     0
general-interac  10  Open:Active       -    -    -    -     5     0     5     0
workshop         10  Open:Active       -    2    -    -     0     0     0     0
workshop-intera  10  Open:Active       -    1    -    -     0     0     0     0
...
```
where the field `QUEUE_NAME` reports the queues you can see, `PRIO` reports the default priority of jobs in the queue, where (all else being equal) high priority jobs are processed before low priority jobs; `STATUS` reports whether each queue is fully functioning; `MAX` reports the maximum number of job slots that can be used to process jobs in the queue; `JL/U` and `JL/P` and `JL/H` give the max number of jobs per user, jobs per X , abd jobs per X. `NJOBS` gives the total number of job slots allowed in the queue; `PEND` gives the number of jobs waiting to be analyzed; `RUN` gives the number of jobs currently being processed; and `SUSP` gives the number of suspended jobs in the queue.


Next, list the compute nodes available for processing jobs scheduled across queues
```
[michael.landis@compute1-client-1 ~]$ bhosts
HOST_NAME          STATUS       JL/U    MAX  NJOBS    RUN  SSUSP  USUSP    RSV
compute1-exec-1.ri ok              -     16      0      0      0      0      0
compute1-exec-10.r ok              -     36      0      0      0      0      0
compute1-exec-100. ok              -     32      0      0      0      0      0
compute1-exec-101. ok              -     32      0      0      0      0      0
compute1-exec-102. ok              -     32      0      0      0      0      0
```
where `HOST_NAME` is the compute node's name, `STATUS` reports whether that node is functioning (`ok`) or not, `JL/U` reports the ma number of jobs per user, `MAX` is the job slots for the node, `NJOBS` is the number of jobs assigned to the node, `RUN` is the number of actively running jobs, `SSUSP` is the number of jobs suspended by the system (e.g. due to policy violation), `USUSP` is the number of jobs suspended by users (e.g. by an administrator), and `RSV` is the number of reserved slots in use.

Let's submit our first job to the LSF scheduler
```console
[michael.landis@compute1-client-1 ~]$ bsub -Is -q general-interactive -a 'docker(alpine)' 'echo -e "Hello, world!"'
Defaulting to LSF user group 'compute-michael.landis'
Job <93145> is submitted to queue <general-interactive>.
<<Waiting for dispatch ...>>
<<Starting on compute1-exec-52.ris.wustl.edu>>
Using default tag: latest
latest: Pulling from library/alpine
Digest: sha256:c0e9560cda118f9ec63ddefb4a173a2b2a0347082d7dff7dc14272e7841a5b5a
Status: Image is up to date for alpine:latest
docker.io/library/alpine:latest
Hello, world!
[michael.landis@compute1-client-1 ~]$
```

This job runs almost instantaneously, and prints `Hello, world!` before completing. The job runs so quickly, that it can't be used to demonstrate how to monitor (`bjobs`) and cancel (`bkill`) jobs. This time, will run a job that runs the command `sleep 1000` submitted as a non-interactive job, which tells the compute to do nothing for 1000 seconds.

```console
[michael.landis@compute1-client-1 ~]$ bsub -q general -a 'docker(alpine)' 'echo Waiting; sleep 10; echo ...done!'
Defaulting to LSF user group 'compute-michael.landis'
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
[michael.landis@compute1-client-1 ~]$ bsub -q general -a 'docker(alpine)' -o job.log "echo -e \'Hello, world\!\' > output.txt"
Defaulting to LSF user group 'compute-michael.landis'
Job <93159> is submitted to queue <general>.
[michael.landis@compute1-client-1 ~]$ tail -n25  job.log

Your job looked like:

------------------------------------------------------------
# LSBATCH: User input
echo -e \'Hello, world\!\' > output.txt
------------------------------------------------------------

Successfully completed.

Resource usage summary:

    CPU time :                                   0.24 sec.
    Max Memory :                                 8 MB
    Average Memory :                             6.67 MB
    Total Requested Memory :                     4096.00 MB
    Delta Memory :                               4088.00 MB
    Max Swap :                                   -
    Max Processes :                              5
    Max Threads :                                19
    Run time :                                   9 sec.
    Turnaround time :                            11 sec.

The output (if any) is above this job summary.
```

After generating output, there are multiple ways to share those files on the cluster with other computers.

One way would be to transfer files using secure copy (`scp`). If your virtual machine username is `mlandis` and your virtual machine IP is `128.252.89.47`, then you can copy your files by typing 
```
$ scp output.txt mlandis@128.252.89.47:/home/mlandis
$ scp job.log mlandis@128.252.89.47:/home/mlandis
```
Now your files are downloaded to `/home/mlandis` on your virtual machine.


Another way would be use GitHub to synchronize files with a remote repository
```console
$ mkdir -p projects
$ git clone https://github.com/WUSTL-Biol4220/lab-07a-mlandis.git projects/lab-07a-mlandis
$ mv output.txt projects/lab-07a-mlandis
$ mv job.log projects/lab-07a-mlandis
$ cd ~/projects/lab-07a-mlandis
$ git add job.log
$ git add output.txt
$ git commit -am 'add log/txt'
$ git push
```
Now the files you produced on the cluster are now synchronized with the remote repository online. To synchronize the files with your Virtual Machine, you'll need to clone and pull changes from the GitHub repository to your Virual Machine.

```console
$ ssh mlandis@128.252.89.47
$ git clone https://github.com/WUSTL-Biol4220/lab-07a-mlandis.git projects/lab-07a-mlandis
$ cd projets/lab-07a-mlandis
$ git pull
```

That's all we'll cover in this tutorial

---

Clone the Lab 12 repo to the cluster, then commit and push `history > history.txt` to the cloned repo to complete the assignment.
