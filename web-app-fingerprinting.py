#!/usr/bin/python3

# Script Name: Web Application Fingerprinting Part 1 of 3
# Class Name: Ops 401
# Author Name: Carsten Rossen
# Date of Latest Revision: 5/24/21 
# Purpose: Performs banner grab using netcat, telnet, and Nmap


# import libraries
import os


# main

# get URL or IP address and port number
address = input("URL or IP address: ")
port = input("Type port number: ")

# netcat banner grab
print("\nBanner grabbing using netcat:\n")
os.system(f"nc {address} {port}")

# telnet banner grab
print("\n\nBanner grabbing using telnet:\n")
os.system(f"telnet {address} {port}")

# Nmap banner grab on well-known ports
print("\n\nBanner grabbing using Nmap:\n")
os.system(f"nmap -Pn -p 1-1023 -sV --script=banner {address}")


# End
