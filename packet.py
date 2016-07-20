#!/usr/bin/env python3

import struct
import socket

''''
struct iphdr{
    unsigned int ihl:4;
    unsigned int version:4;
    u_int8_t tos;
    u_int16_t tot_len;
    u_int16_t id;
    u_int16_t frag_off;
    u_int8_t ttl;
    u_int8_t protocol;
    u_int16_t check;
    u_int32_t saddr;
    u_int32_t daddr;
    /*The options start here. */
};


struct tcphdr{
    u_int16_t source;
    u_int16_t dest;
    u_int32_t seq;
    u_int32_t ack_seq;
    u_int16_t res1:4;
    u_int16_t doff:4;
    u_int16_t fin:1;
    u_int16_t syn:1;
    u_int16_t rst:1;
    u_int16_t psh:1;
    u_int16_t ack:1;
    u_int16_t urg:1;
    u_int16_t res2:2;
    u_int16_t window;
    u_int16_t check;
    u_int16_t urg_ptr;
    /*The options start here. */
};

''''

class Packet(object):
    def __init__(self,buff):
        self.orig_data = buff
        self._drop = 0
        self._l2_offset = 14
        self._l3_offset = 0
        self._l4_offset = 0
        self._l7_offset = 0
        self._l3_proto = 0
        self._l4_proto = 0
        self._tunp4 = (,)
        return

    @property
    def drop(self):
        return self._drop
    @property
    def l3_proto(self):
        return self._l3_proto
    @property
    def l4_proto(self):
        return self._l4_proto
    @property
    def tunple(self):
        return self._tunple

    def __parse(self):
        self.__parse_l3(self)
        self.__parse_l4(self)

    def __parse_l3(self):
        if self.drop:
            return
        l3data = self.orig_data[self._l2_offset:]
        first,*_,l4_proto,check,saddr,daddr = struct.unpack("!IB3H2BH2I",l3data)
        iphdr_len = (first&0XFFFFFFFF)>>28 * 4
        self._l3_offset = iphdr_len + 14
        self._l4_proto = l4_proto
        if self._l4_proto != 0x06:
            self._drop = 1
            return
        self._tunp4[0] = saddr
        self._tunp4[1] = daddr
       return 

    def __parse_l4(self):
        if self.drop:
            return
        l4data = self.orig_data[self._l3_offset:]
        sport,dport = struct.unpack("!xxxx",l4data)
        self._tunp4[2] = sport
        self._tunp4[3] = dport
        return

if __name__ == "__main__":
    test()