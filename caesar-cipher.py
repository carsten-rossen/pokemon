#!/usr/bin/python3

# Script Name: Caesar Cipher
# Author Name: Carsten Rossen
# Date of Latest Revision: 7/23/21
# Purpose: Encrypt and decrypt a message using a Caesar Cipher technique.


# Import Libraries

import string


# Define functions

# Build a list of characters in which messages can be encrypted and decrypted with
def char_list_maker():
    char_list = []

    # Uppercase letters
    for i in range(len(string.ascii_uppercase)):
        char_list.append(string.ascii_uppercase[i])

    # Numbers
    for i in range(len(string.digits)):
        char_list.append(string.digits[i])

    # Punctuation
    for i in range(len(string.punctuation)):
        char_list.append(string.punctuation[i])

    return char_list


# Ask if user wants to encrypt or decrypt
def prompt():
    print("Welcome to the Caesar Cipher program. Would you like to...")
    print("   1. Encrypt")
    print("   2. Decrypt")

    # Redisplay prompt if user inputs an incorrect value
    while(True):
        choice = input("Please only input 1 or 2: ")
        if choice == "1" or choice == "2":
            return choice


# Prompt the user for a value to transpose the message by (key)
def key_prompt():
    key = input("Key (integer): ")
    
    # Only accept an integer
    try:
        int(key)
    except ValueError:
        print("Please only input an integer.")
        key = key_prompt()
    return int(key)


# Encrypt or decrypt the message using the key
def encrypt_decrypt(char_list, choice):
    if choice == "1":
        msg = input("Message to encrypt: ")
        key = key_prompt()
        new_msg = "Your encrypted message is: "
    else:
        msg = input("Message to decrypt: ")
        key = 0 - key_prompt()
        new_msg = "Your decrypted message is: "

    # All letters will be encrypted or decrypted in an uppercase format
    msg = msg.upper()

    # Transpose characters
    for i in range(len(msg)):
        if msg[i] not in string.whitespace:
            location = char_list.index(msg[i])
            new_char = char_list[(location + key) % len(char_list)]
            new_msg = new_msg + new_char
        else:
            new_msg = new_msg + msg[i]
    return new_msg


# Main

# Make list of acceptable characters
char_list = char_list_maker()
choice = prompt()
msg = encrypt_decrypt(char_list, choice)
print(msg)


# End