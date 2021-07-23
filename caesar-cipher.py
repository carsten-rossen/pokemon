#!/usr/bin/python3

# Script Name: Caesar Cipher
# Author Name: Carsten Rossen
# Date of Latest Revision: 7/21/21
# Purpose: Encrypt and decrypt a message using a Caesar Cipher technique.


# Import Libraries
import string

# Define functions

def key_prompt():
    key = input("Key (integer): ")
    try:
        int(key)
    except ValueError:
        print("Please only input an integer.")
        key = key_prompt()
    return int(key)

def encrypt(msg, key):
    new_msg = ""
    for i in range(len(msg)):
        if msg[i] not in string.whitespace:
            location = char_list.index(msg[i])
            new_char = char_list[(location + key) % len(char_list)]
            new_msg = new_msg + new_char
        else:
            new_msg = new_msg + msg[i]
    return new_msg


# Main

char_list = []
for i in range(len(string.ascii_uppercase)):
    char_list.append(string.ascii_uppercase[i])
for i in range(len(string.digits)):
    char_list.append(string.digits[i])
for i in range(len(string.punctuation)):
    char_list.append(string.punctuation[i])

msg = input("Message to encrypt: ")
msg = msg.upper()
key = key_prompt()
msg = encrypt(msg, key)
print("Your encrypted message is: " + msg)

# End