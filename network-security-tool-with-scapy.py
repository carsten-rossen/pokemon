#!/usr/bin/python3

# Script Name: Network Security Tool with Scapy
# Class Name: Ops 401
# Author Name: Carsten Rossen
# Date of Latest Revision: 4/19/21
# Purpose: Scans specified ports on a specified host.

# Import libraries

import sys
from scapy.all import ICMP, IP, sr1, TCP
import random


# Main

# input host
ip = input("Please specify host IP address: ")

# generate source port
src_port = random.randint(2, 200)
dst_ports = []

# input destination ports
while True:
    dst_ports.append(input("Please specify port to scan: "))
    answer = input("Would you like to specify another port? (y/n): ")
    if answer != 'y':
        break

# scan specified ports
for port in dst_ports:
    response = sr1(IP(dst=ip)/TCP(sport=src_port,dport=port,flags="S"),timeout=1,verbose=0)

    print(response)

# End