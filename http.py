#!/usr/bin/env python


import struct
import os
from tcp import TcpFlow



def http_identify(flow):
    if not isinstance(flow,TcpFlow):
        print("error")
        exit(0)
    dport = flow.tunp4[3]
    if dport == 80:
        return True
    return False