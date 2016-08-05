#!/usr/bin/env python


import os
import sys
import getopt
import struct
import StringIO

import threading
from queue import Queue

from tcp import TcpTable
from tcp import l4stream
from parse_pcapfile import parse_pcapfile
from packet import Packet


global tcptable
global queue = Queue()


def global_init():
    tcptable = TcpTable()


def usage():
    print ("./http_decoder.py -r <input_file>")


def l4stream():
    return


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

    l4_thread = threading.Thread(target=l4stream,args=(packet_queue))
    l4_thread.start()
    parse_pcap_file(input_file,packet_queue)    
    for pkt_data in parse_pcapfile(input_file):
        pkt = Packet(pkt_data)
        if pkt.drop != 1:
            packet_queue.put(pkt)
        else:
            continue

if __name__ == "__main__":
    main()