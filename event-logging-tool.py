#!/usr/bin/python3

# Script Name: Event Loggin Tool 3/3
# Class Name: Ops 401
# Author Name: Carsten Rossen
# Date of Latest Revision: 5/12/21 
""" Purpose: Creates a log file with logs related to the Uptime Sensor Tool (1/2) and
rotates logs once the original file exceeds a certain size. Outputs error logs to a seperate
file from the debug logs.
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

# create handlers
c_handler = logging.StreamHandler()
f_handler = logging.FileHandler('file.log')
c_handler.setLevel(logging.WARNING)
f_handler.setLevel(logging.ERROR)

# Create formatters and add it to handlers
c_format = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
f_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
c_handler.setFormatter(c_format)
f_handler.setFormatter(f_format)

# add handlers to the logger
logger.addHandler(c_handler)
logger.addHandler(f_handler)


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
    logger.warning('This is a warning')
    logger.error('This is an error')
    time.sleep(2)

# End