'''
Fasta to Fastq
Convert file in fasta format to pseudo-fastq format (fake quality score)

Date: September 19, 2016
@author: sbrown
'''

## Import Libraries
import sys
import argparse

DEBUG = False
VERB = False


if __name__ == "__main__":

    ## Deal with command line arguments
    parser = argparse.ArgumentParser(description = "Fasta to Fastq")
    ## add_argument("name", "(names)", metavar="exampleOfValue - best for optional", type=int, nargs="+", choices=[allowed,values], dest="nameOfVariableInArgsToSaveAs")
    parser.add_argument("fastaFile", help = "Fasta file to convert", type = str)
    parser.add_argument("fastqFile", help = "Fastq file to write to", type = str)
    parser.add_argument("-d", "--debug", action = "store_true", dest = "DEBUG", help = "Flag for setting debug/test state.")
    parser.add_argument("-v", "--verbose", action = "store_true", dest = "VERB", help = "Flag for setting verbose output.")
    args = parser.parse_args()

    ## Set Global Vars
    DEBUG = args.DEBUG
    VERB = args.VERB

    header = ""
    seq = ""

    out = open(args.fastqFile, "w")

    for line in open(args.fastaFile, "r"):
        if line.startswith(">"):
            ## write previous
            if len(header) > 0 and len(seq) > 0:
                out.write("@{}\n{}\n+\n{}\n".format(header, seq, "H"*len(seq)))
                header = ""
                seq = ""
            ## update header to new one.
            header = line.rstrip()[1:]
        else:
            seq += line.rstrip()
    ## write last entry
    out.write("@{}\n{}\n+\n{}\n".format(header, seq, "H"*len(seq)))

    out.close()

    print("done.")
