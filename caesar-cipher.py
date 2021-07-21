#!/usr/bin/python3

# Script Name: Caesar Cipher
# Author Name: Carsten Rossen
# Date of Latest Revision: 7/21/21
# Purpose: Encrypt and decrypt a message using a Caesar Cipher technique.


# Import Libraries
import string


# Define functions
def encrypt(msg, transpose_value):
    new_msg = ""
    transpose_value = int(transpose_value) % 100
    for i in range(len(msg)):
        if msg[i] not in string.whitespace:
            location = string.printable.index(msg[i])
            new_char = string.printable[location + transpose_value]
            new_msg = new_msg + new_char
        else:
            new_msg = new_msg + msg[i]
    return new_msg


# Main
msg = input("Message to encrypt: ")
msg = msg.upper()
transpose_value = input("Transpose by (positive or negative integer): ")
msg = encrypt(msg, transpose_value)

print("Your encrypted message is: " + msg)

# End