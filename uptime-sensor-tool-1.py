#!/usr/bin/python3

# Script Name: Uptime Sensor Tool Part 1 of 2
# Class Name: Ops 401
# Author Name: Carsten Rossen
# Date of Latest Revision: 4/6/21
# Purpose: Continually test the local system is able to ping a host on the LAN

# import libraries

import os
import datetime
import time


# declaration of variables

now = datetime.datetime.now()
ip = "192.168.1.100"

# main
while True:
    pingreq = os.system("ping -c 1 192.168.1.100")
    if str(pingreq).find("0 received"):
        status = 'Inactive'
    else:
        status = 'Active'
    print("\n\n" + str(now) + " Network " + status + " to " + ip + "\n\n")
    time.sleep(2)


# end