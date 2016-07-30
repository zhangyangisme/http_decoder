#!/usr/bin/env python3

'''
struct iphdr{
    u_int8_t ihl:4;
    u_int8_t version:4;
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
;

'''

import struct

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
        self._tunp4 = []
        self.__parse()
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
    def tunple(self):
        return self._tunp4
    @property
    def l7_data(self):
        return self.orig_data[self._l4_offset:]

    def __parse(self):
        self.__parse_l2()
        self.__parse_l3() 
        self.__parse_l4()

    def __parse_l2(self):
        link_type = self.orig_data[12:14]
        if link_type[0] == 0x08 and link_type[1] == 0x00:
            pass
        else:
            self._drop = 1
        return
    def __parse_l3(self):
        if self.drop:
            return
        l3data = self.orig_data[self._l2_offset:]
        first,*_,l4_proto,check,saddr,daddr = struct.unpack("!2B3H2BH2I",l3data[:20])
        iphdr_len = (first&0xF) * 4
        #print("iphdr_len:%d"%iphdr_len)
        self._l3_offset = iphdr_len + 14
        self._l4_proto = l4_proto
        if self._l4_proto != 0x06:
            self._drop = 1
            return
        self._tunp4.insert(0,saddr)
        self._tunp4.insert(1,daddr)
        return

    def __parse_l4(self):
        if self.drop:
            return
        l4data = self.orig_data[self._l3_offset:]
        sport,dport,seq,ack,doff_res = struct.unpack("!2H2IB",l4data[:13])
        hdr_len = (doff_res >> 4)*4
        print("hdr_len:%d"%hdr_len)
        self._l4_offset = self._l3_offset + hdr_len
        self._tunp4.insert(2,sport)
        self._tunp4.insert(3,dport)
        print(self._tunp4)
        return

class Tunple4():
    def __init__():
        return

def test():
    return 

if __name__ == "__main__":
    test()
