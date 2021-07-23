#!/usr/bin/python3

# Script Name: Caesar Cipher
# Author Name: Carsten Rossen
# Date of Latest Revision: 7/21/21
# Purpose: Encrypt and decrypt a message using a Caesar Cipher technique.


# Import Libraries
import string

# Define functions
def prompt():
    print("Welcome to the Caesar Cipher program. Would you like to...")
    print("   1. Encrypt")
    print("   2. Decrypt")
    while(True):
        choice = input("Please only input 1 or 2")
        if choice == "1" or choice == "2":
            return choice


def key_prompt():
    key = input("Key (integer): ")
    try:
        int(key)
    except ValueError:
        print("Please only input an integer.")
        key = key_prompt()
    return int(key)


def encrypt_decrypt(msg, key, choice):
    new_msg = ""
    if choice == "1":
        msg = input("Message to encrypt: ")
        key = key_prompt
    else:
        msg = input("Message to decrypt: ")
        key = 0 - key_prompt
    msg = msg.upper()
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

choice = prompt()
key = key_prompt()
msg = encrypt_decrypt(msg, key)
print("Your encrypted message is: " + msg)

# End