'''
Server Status
Check the status of the servers

Date: October 19, 2017
@author: sbrown
'''

## Import Libraries
import sys
import argparse
import os
import time
import subprocess
import math
import getpass

DEBUG = False
VERB = False

ALLOWED_SUBPROCESS_ERRORS = ["","Warning: No xauth data; using fake authentication data for X11 forwarding.\r\n"]
BAR_WIDTH = 20
USER = getpass.getuser()

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    ENDC = '\033[0m'

def log_print(type, msg):
    print("{} [{}]: {}".format(type, time.strftime("%Y/%m/%d %T"), msg))


def printChart(prc, len):
    numToPrint = math.ceil((prc/100)*len)
    res = "{}{}{}{}".format(bcolors.OKGREEN,"|"*numToPrint," "*(len-numToPrint), bcolors.ENDC)
    if prc > 25:
        res = "{}{}{}{}".format(bcolors.OKBLUE,"|"*numToPrint," "*(len-numToPrint), bcolors.ENDC)
    if prc > 50:
        res = "{}{}{}{}".format(bcolors.WARNING,"|"*numToPrint," "*(len-numToPrint), bcolors.ENDC)
    if prc > 75:
        res = "{}{}{}{}".format(bcolors.FAIL,"|"*numToPrint," "*(len-numToPrint), bcolors.ENDC)
    return res



if __name__ == "__main__":

    ## Deal with command line arguments
    parser = argparse.ArgumentParser(description = "Server Status")
    ## add_argument("name", "(names)", metavar="exampleOfValue - best for optional", type=int, nargs="+", choices=[allowed,values], dest="nameOfVariableInArgsToSaveAs")
    parser.add_argument("serverList", help = "csv of server names and addresses, one per line")
    parser.add_argument("-d", "--debug", action = "store_true", dest = "DEBUG", help = "Flag for setting debug/test state.")
    parser.add_argument("-v", "--verbose", action = "store_true", dest = "VERB", help = "Flag for setting verbose output.")
    args = parser.parse_args()

    ## Set Global Vars
    DEBUG = args.DEBUG
    VERB = args.VERB

    if VERB:
        print("=======================================================")
        print("Python version: {}".format(sys.version))
        print("Server: {}".format(os.uname()[1]))
        print("Current directory: {}".format(os.getcwd()))
        print("Command: {}".format(" ".join(sys.argv)))
        print("Time: {}".format(time.strftime("%Y/%m/%d %T")))
        print("=======================================================\n")


    servers = []
    ips = {}

    for line in open(args.serverList, "r"):
        line = line.rstrip().split(",")
        servers.append(line[0])
        ips[line[0]] = line[1]

    
    ## Submit queries
    memcalls = []
    cpucalls = []
    for serv in servers:
        ## mem call
        cmd = "ssh {}@{} 'free;'".format(USER,ips[serv])
        memcalls.append(subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True))
        time.sleep(0.2) ## slight pause so no exactly concurrent requests
        ## cpu call
        cmd = "ssh {}@{} 'vmstat 1 2 | tail -1;'".format(USER,ips[serv])
        cpucalls.append(subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True))
        time.sleep(0.2) ## slight pause so no exactly concurrent requests

    ## Get results
    for i in range(0, len(servers)):
        out = "{}:  ".format(servers[i])
        ## MEM
        (res, err) = memcalls[i].communicate()
        if err.decode('ascii') in ALLOWED_SUBPROCESS_ERRORS:
            ##success
            res = res.decode("ascii")
            res = res.split("\n")
            memline1 = res[1]
            memline1 = memline1.split()
            #print(memline)
            memtot = int(memline1[1])
            memline2 = res[2]
            memline2 = memline2.split()
            memusd = int(memline2[2])
            memprc = 100*(memusd/memtot)
            out += "MEM [{}] {:1.1f}% \t".format(printChart(memprc,BAR_WIDTH),memprc)
        else:
            if DEBUG: print(err.decode("ascii"))
            out += "MEM [{}] --.-% \t".format("-"*BAR_WIDTH)

        ## CPU
        (res, err) = cpucalls[i].communicate()
        if err.decode('ascii') in ALLOWED_SUBPROCESS_ERRORS:
            ##success
            res = res.decode("ascii")
            #print(res)
            res = res.split("\n")
            #print(res)
            res = res[0]
            res = res.split()
            cpuprc = int(res[12])
            out += "CPU [{}] {}%".format(printChart(cpuprc,20),cpuprc)
        else:
            if DEBUG: print(err.decode("ascii"))
            out += "CPU [{}] -% \t".format("-"*BAR_WIDTH)

        print(out)