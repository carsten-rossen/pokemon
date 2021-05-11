#!/usr/bin/python3

# Script Name: Event Loggin Tool 1/3
# Class Name: Ops 401
# Author Name: Carsten Rossen
# Date of Latest Revision: 5/10/21 
# Purpose: Creates a log file with logs related to the Uptime Sensor Tool (1/2)

# import libraries
import os
import datetime
import time
import logging


# declare variables

# get current date and time
now = datetime.datetime.now()

# set IP
ip = "192.168.1.100"


# Main

# set file to send logs
logging.basicConfig(filename='example.log', encoding='utf-8', level=logging.DEBUG)


while True:

    # ping system
    pingreq = os.system("ping -c 1 192.168.1.100")
    
    # determine if ping is received
    if str(pingreq).find("0 received"):
        status = 'Inactive'
    else:
        status = 'Active'

    # send log to file    
    logging.debug("\n\n" + str(now) + " Network " + status + " to " + ip + "\n\n")
    time.sleep(2)

# End