#!/usr/bin/python3

# Script Name: Uptime Sensor Tool Part 2 of 2
# Class Name: Ops 401
# Author Name: Carsten Rossen
# Date of Latest Revision: 4/7/21
# Purpose: Continually test the local system is able to ping a host on the LAN
# Purpose: and send an email to a specified address if there is a change in status

# import libraries

import os
import datetime
import time
import smtplib

# declaration of variables

ip = "192.168.1.100"
previous_status = 'Inactive'
server = smtplib.SMTP("smtp.gmail.com", "587")


# main

server.ehlo()
server.starttls()

# login to email account
server.login("john.smith.flyhomes@gmail.com", "flyhomes123")

while True:

    # obtain timestamp
    now = datetime.datetime.now()
    
    # obtain ping request status
    pingreq = os.system("ping -c 1 " + ip)

    # set host status
    if pingreq != 0:
        status = 'Inactive'
    else:
        status = 'Active'

    # determine if host status changed
    if status != previous_status:

        # create a message of the status change information
        msg = "\n\n" + str(now) + " Network changed from " + previous_status + " to " + status + " on " + ip + "\n\n"
        
        # save the status to test against the next ping request status
        previous_status = status
        
        # send an email with the status change message
        try:
            server.sendmail("john.smith.flyhomes@gmail.com", "randy.perkins.flyhomes@gmail.com", msg)
        except:
            print("Email failed to send.")

    time.sleep(2)

server.quit()

# end