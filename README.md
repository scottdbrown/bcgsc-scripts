General Use Scripts
===================

Scott Brown
-----------
Canada's Michael Smith Genome Sciences Centre  
BC Cancer Research Centre  
Genome Science + Technology Graduate Program  
University of British Columbia  
Vancouver, BC, Canada  
[http://www.holtlab.ca](http://www.holtlab.ca)  
[http://www.scottderekbrown.com](http://www.scottderekbrown.com)  
sbrown@bcgsc.ca  
scottderekbrown@gmail.com  

[mqsub_throttled](mqsub_throttled)
-----------------

March 29, 2016

Variation on mqsub command available on GSC clusters.
Allows you to limit the number of jobs to be in the queue at once.
```
Usage: mqsub_throttled [-h] --file batchfile [--chdir directory]
                       [--name jobname] [--nosubmit] [--maxJobs num_jobs]
                       [--mkdir] [--qsub "qsub args"] [--refresh num_minutes]
                       [--debug] [-v]
```
`mqsub_throttled -h` for more information.


[clusterTAS](clusterTAS)
------------

June 21, 2016

Analysis management script designed for use on GSC clusters.
Use case: You have X files that you want to do analysis on using Genesis, and need to transfer
          files to Genesis scratch space (default using Apollo), and want to manage jobs.
          Designed for situation where your Genesis scratch space is not large enough to hold
          all the files you want to analyze. This script will track and limit submissions
          depending on user criteria provided through command line arguments.
```
usage: clusterTAS [-h] [--genMem N] [--genQsub "qsub args"] [--maxJobs N]
                  [--maxSpace N] [--noApollo] [--noDate] [--refresh N]
                  [--spaceInflationFactor N] [--startAtLine N] [-c] [-L] [-t]
                  [-d] [-v]
                  filesToTransfer scriptsToRun genesisWorkingDir
                  localWorkingDir
```
`clusterTAS -h` for more information.

Pressing `Ctrl-c` while clusterTAS is running may set the program into a PAUSE state. This allows submission of jobs to be suspended, and modification of some variables (max number of jobs, refresh time, DEBUG and VERB). Caution should be taken, if PAUSE state is entered in the middle of processing, jobs may be lost. There is a 1 second safe window where the PAUSE state can be entered each iteration, identified by "Holding 1 second for safe time to pause..." appearing on the screen. Alternatively, it can be entered during any Wait period.

Should the program be ended unexpectedly, clusterTAS will attempt to write output files containing completed and running job names, and will print which line to resume processing at.

Logfile of all output created. Additionally, tracks environment information:
```
    clusterTAS Genesis Analysis Management Script
    Python version: 3.4.3 (default, May 29 2015, 15:56:30)
    [GCC 4.1.2 20080704 (Red Hat 4.1.2-54)]
    Server: gphost02
    Current directory: /projects/sbrown_prj/scripts/test
    Command: ../clusterTAS --genMem 1 --refresh 2 --maxSpace 5000000000 --spaceInflation 2 -c testFile.tsv testScriptFile.txt /genesis/extscratch/sbrown/test /projects/sbrown_prj/scripts/test/gphost02
    Time: 2016/06/21 11:13:14
```

[clusterTAS_inputMaker.py](clusterTAS_inputMaker.py)
--------------------------

December 9, 2016

(Optional) Example script to generate the shell script required as input for clusterTAS.

```
usage: python3 clusterTAS_inputMaker.py fof_file output_sh_file
```
`python3 clusterTAS_inputMaker.py -h` for more information

Requires a fof_file as input. Each line of this file will become a single job on the cluster. If there are multiple files per job, they should be tab separated.

[fastaToFastq.py](fastaToFastq.py)
-----------------

September 19, 2016

Simple script to convert a file in fasta format into "pseudo-fastq" format by giving arbitrary "H" quality scores.

```
usage: fastaToFastq.py [-h] [-d] [-v] fastaFile fastqFile
```
`fastaToFastq.py -h` for more information.

Created for converting capillary sequencing data files into fastq format for running in MiTCR, with -quality 0 flag used.
(MiTCR requires files to be in fastq format even if quality information is not used).

[sstat.py](sstat.py)
----------

October 20, 2017

Utility to check the load on the gphosts.
Note, you must be able to ssh into each server without entering your password (have SSH keys set up).

```
usage: python3 sstat.py [-h] [-d] [-v] gscServersToCheck.csv
```

Example output:
```
gphost01:  MEM [|                   ] 3.4%      CPU [|||                 ] 13%
gphost02:  MEM [|                   ] 1.8%      CPU [|                   ] 1%
gphost03:  MEM [|                   ] 3.7%      CPU [|||                 ] 15%
gphost04:  MEM [||||||||||          ] 45.7%     CPU [||                  ] 6%
gphost05:  MEM [|                   ] 2.3%      CPU [||||                ] 20%
gphost06:  MEM [|                   ] 0.6%      CPU [                    ] 0%
gphost07:  MEM [|                   ] 0.6%      CPU [                    ] 0%
gphost08:  MEM [|                   ] 0.6%      CPU [                    ] 0%
gphost09:  MEM [|                   ] 0.6%      CPU [                    ] 0%
gphost10:  MEM [|                   ] 0.6%      CPU [                    ] 0%
gphost11:  MEM [|                   ] 0.6%      CPU [                    ] 0%
gphost12:  MEM [|                   ] 0.6%      CPU [                    ] 0%
```
