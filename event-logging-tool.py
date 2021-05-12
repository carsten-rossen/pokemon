#!/usr/bin/python3

# Script Name: Event Loggin Tool 2/3
# Class Name: Ops 401
# Author Name: Carsten Rossen
# Date of Latest Revision: 5/11/21 
""" Purpose: Creates a log file with logs related to the Uptime Sensor Tool (1/2) and
rotates logs once the original file exceeds a certain size.
"""

# import libraries
import os
import datetime
import time
import logging
from logging.handlers import RotatingFileHandler


# declare variables

# get current date and time
now = datetime.datetime.now()


# Main

# create rotating log
logger = logging.getLogger("Rotating Log")
logger.setLevel(logging.INFO)

# add rotating handler
handler = RotatingFileHandler('test.log', maxBytes=50, backupCount=5)
logger.addHandler(handler)

# set file to send logs
#logging.basicConfig(filename='./example.log', level=logging.DEBUG, format='%(asctime)s:%(levelname)s:%(message)s')


while True:

    # ping system
    pingreq = os.system("ping -c 1 192.168.1.100")
    
    # determine if ping is received
    if str(pingreq).find("0 received"):
        status = 'Inactive'
    else:
        status = 'Active'

    # send log to file    
    #logging.debug("\n\n" + str(now) + " Network " + status + " to 192.168.1.100")
    logger.info("\n\n" + str(now) + " Network " + status + " to 192.168.1.100")
    time.sleep(2)

# End