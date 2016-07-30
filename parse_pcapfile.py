#!/usr/bin/env python

import struct
from queue import Queue
from packet import Packet

'''
struct pcap_file_header {
        bpf_u_int32 magic;
        u_short version_major;
        u_short version_minor;
        bpf_int32 thiszone;     /* gmt to local correction */
        bpf_u_int32 sigfigs;    /* accuracy of timestamps */
        bpf_u_int32 snaplen;    /* max length saved portion of each pkt */
        bpf_u_int32 linktype;   /* data link type (LINKTYPE_*) */
};

struct pcap_pkthdr {
        struct timeval ts;      /* time stamp */
        bpf_u_int32 caplen;     /* length of portion present */
        bpf_u_int32 len;        /* length this packet (off wire) */
};
struct timeval {
        long            tv_sec;         /* seconds (XXX should be time_t) */
        suseconds_t     tv_usec;        /* and microseconds */
};

'''

def parse_pcapfile(fname,packet_queue):
    f = open(fname,"rb")
    pcap_header = f.read(24)
    if len(pcap_header) != 24:
        print("read file header error")
    while True:
        pkthdr = f.read(16)
        if len(pkthdr) != 16:
            print("read pkt header error")
            break
        tv_sec,tv_usec,caplen,pktlen = struct.unpack("4I",pkthdr)
        print(caplen)
        packet_data = f.read(caplen)
        if len(packet_data) != caplen:
            print("read packet error")
            break
        pkt = Packet(packet_data)
        if pkt.drop != 1:
            print(pkt.tuple())
            #packet_queue.put(pkt)

def test():
    parse_pcapfile(sys.argv[1],None)
    return



if __name__ == "__main__":
    import sys
    test()
