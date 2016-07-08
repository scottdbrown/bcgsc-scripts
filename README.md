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
          files to Genesis scratch space using Apollo, and want to manage jobs.
          Designed for situation where your Genesis scratch space is not large enough to hold
          all the files you want to analyze. This script will track and limit submissions
          depending on user criteria provided through command line arguments.
```
Usage: clusterTAS [-h] [--genMem N] [--genQsub "qsub args"] [--maxJobs N]
                  [--maxSpace N] [--noDate] [--refresh N]
                  [--spaceInflationFactor N] [--startAtLine N] [-c] [-L] [-t]
                  [-d] [-v]
                  filesToTransfer scriptsToRun genesisWorkingDir
                  localWorkingDir
```
`clusterTAS -h` for more information.

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


