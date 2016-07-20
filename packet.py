#!/usr/bin/env python

import struct


''''
struct ip_hdr{
    
}


sruct tcp_hdr{

}
''''

class Packet(object):
    def __init__(self,buff):
        self.orig_data = buff
        self._l3_proto = 0
        self._l4_proto = 0
        self._l3_offset = 0
        self._l4_offset = 0
        self._l7_offset = 0
        self._drop = 0
        self._tunple = (,)
        return
    def __parse_l3(self):
       self._tunple[0] = 
       self._tunple[1] = 
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



def test():
    return 0


if __name__ == "__main__":
    test()