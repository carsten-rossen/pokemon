#!/usr/bin/python3

# Script Name: Password Creator
# Class Name: Ops 401
# Author Name: Carsten Rossen
# Date of Latest Revision: 7/8/21
# Purpose: Creates a complex password of a user-specified length.


# import libraries
import string
import random


# define functions

# count how many characters of a certain string are in the password
def counter(phrase, lst):
    element_count = 0
    for i in phrase:
        element_count += lst.count(i)
    return element_count

# generate a new password of a specified length
def generate(lst):
    for i in range(len(lst)):
        lst[i] = random.choice(string.printable)
    return lst

# get the desired password length from the user
def get_length():
    length = input("What length would you like you password? ")
    # recall function if user does not input a positive digit
    if not str.isdigit(length):
        print("Please only input a positive digit")
        length = get_length()
    # recall function if the specified length is less than 4
    elif int(length) < 4:
        print("Please select a longer password")
        length = get_length()
    return int(length)


# Main

length = get_length()
pass_lst = [''] * length
pass_lst = generate(pass_lst)

# generate new passwords until the password is complex
lower_count, upper_count, char_count = 0,0,0
while lower_count == 0 or upper_count == 0 or char_count == 0:
    pass_lst = generate(pass_lst)
    lower_count = counter(string.ascii_lowercase, pass_lst)
    upper_count = counter(string.ascii_uppercase, pass_lst)
    char_count = counter(string.punctuation, pass_lst)

# print the generated password to the terminal
pass_str = ''.join(pass_lst)
print("\nGenerated Password:")
print(pass_str)

# End
