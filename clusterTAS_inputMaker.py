'''
clusterTAS input maker
Given a .fof you want to do things to, this will walk you through the generation of clusterTAS input script file.

Date: December 9, 2012
@author: sbrown
'''

## Import Libraries
import sys
import argparse
import os

DEBUG = False
VERB = False


if __name__ == "__main__":

    ## Get command line arguments
    parser = argparse.ArgumentParser(description = "clusterTAS input maker")
    parser.add_argument("fof_file", help = "The 'file of files' you want to perform computation on.", type = str)
    parser.add_argument("output_file", help = "The file you want to write your script to.", type = str)
    parser.add_argument("-d", "--debug", action = "store_true", dest = "DEBUG", help = "Flag for setting debug/test state.")
    parser.add_argument("-v", "--verbose", action = "store_true", dest = "VERB", help = "Flag for setting verbose output.")
    args = parser.parse_args()

    ## Set Global Vars
    DEBUG = args.DEBUG
    VERB = args.VERB

    ## open the output file for writing to (which will occur in the loop below)
    outputFileHandle = open(args.output_file, "w")


    lineNumber = 0
    ## Read fof_file, and prepare sh script for each line (job)
    for line in open(args.fof_file, "r"):
        lineNumber += 1     ## increment lineNumber by 1

        ## `line` will contain one line of the fof_file, going through each line for each loop of the for loop.
        file = line.rstrip().split("\t")    ## if multiple files, these should be separated by tabs.
                                            ## `file` is now a list, access first entry by: file[0].
                                            ## if multiple files in a line, will be file[0], file[1], file[2], ...

        ## Generate a unique jobname for this job
        ## It can be a number, a sample name, etc.
        ## But should be valid as a directory name (no slashes, special characters. - or _ is fine)
        ## Here I have set the jobname to the line number.
        jobname = "job{}".format(lineNumber)


        ## Create the script
        script = ""     ## initialize an empty script.
        ## EDIT HERE:
        script += "FILL THIS IN WITH THE SCRIPT OF INTEREST;"
        script += "MAKE SURE TO FINISH EVERY COMMAND WITH A SEMICOLON;"
        script += "AN EXAMPLE OF REFERENCING THE CURRENT FILE FOLLOWS;"
        script += "UNTAR THE FILE {};".format(file[0])
        script += "THE CURLY BRACKETS TELL WHERE TO INSERT THE VARIABLE PRESENT IN `format`;"
        #script += "IF THERE ARE MULTIPLE FILES YOU CAN DO THINGS TO FILE 1: {} AND FILE 2: {};".format(file[0], file[1])
        ## /END EDIT HERE
        script += "\n"  ## adds newline character to the end

        ## Write the script for this line/job to the script file.

        outputFileHandle.write("{}\t{}\n".format(jobname, script))

    ## The args.fof_file automatically closes once the for loop completes.

    ## Just need to close the output file.
    outputFileHandle.close()

    ## And we're done.
    print("Usage: clusterTAS [options] {} {} genesis_directory analysis_directory".format(args.fof_file, args.output_file))
    print("Complete.")
