#!/usr/bin/env python

import struct

def l4stream(packet_queue):
    global tcptable
    while True:
        pkt = packet_queue.get():
        flow = tcptable.find_flow(ptk.tuple4)
        if flow not None:
            flow.add_packet(ptk)
        else:
            pass



class TcpTable(dict):
    def __init__(self):
        return

    def add_flow():
        return
    def del_flow():
        return
    def find_flow(self,tuple):
        return 
    
    



class TcpFlow(object):
    def __init__(self):
        self.__finish = 0
        self.tunp4 = []
        return
    def add_packet():
        return
    def del_packet():
        return
    
    @property
    def is_finish(self):
        return self.__finish



def test():
    return

if __name__ == "__main__":
    test()