#!/usr/bin/env python


import os
import sys
import getopt
import struct
import StringIO

def usage():
    print ("./http_decoder.py -r <input_file>")

def main():
    opts,args = getopt.getopt(sys.argv[1:],"r:")
    input_file = ""
    if len(sys.argv) != 2:
        usage()
        exit()
    for op,value in opts:
        if op == "-r":
            input_file = value
            print input_file
        else:
            usage()
            exit()
    return 0


if __name__ == "__main__":
    main()