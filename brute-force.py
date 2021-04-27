#!/usr/bin/python3

# Script Name: Automated Brute Force Wordlist Attack Tool Part 1 of 3
# Class Name: Ops 401
# Author Name: Carsten Rossen
# Date of Latest Revision: 4/26/21 
# Purpose: Print every word from a text file consecutively or
# Purpose: search a text file for an inputed string


# Import libraries

import time


# Declare functions

# Menu system
def menu():
    print("Which mode would you like to enter?")
    print("   1. Offensive; Dictionary Iterator")
    print("   2. Defensive; Password Recognized")
    choice = input("(1/2) >>> ")
    return choice

# Prints all the words in a text file
def offensive():
    # get the file path
    wordlist = input("\nPlease give the word list's full file path: ")
    
    # open the file in read mode
    with open(wordlist, 'r') as file:

        # put all of the file's words into a list
        words = list(file.read().split())

        # print all the words with a .1 second delay in between
        for word in words:
            print(word)
            time.sleep(.1)

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

# get user input from menu system
choice = menu()
if choice == "1":
    offensive()
elif choice == "2":
    defensive()
else:
    # end the program if the user does not input a proper option
    print("Error: Only enter 1 or 2. TERMINATING PROGRAM.")


# End