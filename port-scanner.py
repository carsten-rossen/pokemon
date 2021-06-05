#!/usr/bin/python3

# Script Name: Port Scanner
# Class Name: Ops 401
# Author Name: Carsten Rossen
# Date of Latest Revision: 6/4/21 
# Purpose: The purpose of this script is to determine if a target port is open or closed, using strictly Python 3 commands. 
# To do so, we'll be importing the socket module, a low-level networking interface for Python.


# import libraries
import socket


# declare variables
sockmod = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
timeout = 5
sockmod.settimeout(timeout)

# get target IP address and port number
hostip = input("Host IP address: ")
portno = int(input("Port number: "))


# declare functions
def portScanner(portno):
    # try to connect with port as a way to test whether or not it is open
    if sockmod.connect_ex((hostip, portno)):
        print("Port closed")
    else:
        print("Port open")

# main
portScanner(portno)
