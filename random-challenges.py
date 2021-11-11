#!/usr/bin/python3

# Script Name: Random Challenges
# Author Name: Carsten Rossen
# Date of Latest Revision: 11/10/21 
# Purpose: All of the Python3 challenges in this script can be found here https://pythonprinciples.com/challenges/
# Each function represents a solution to a challenge found on this website.


# Challenge solutions (functions)

# Tic Tac Toe Input
import string
def get_row_col(location):
    x = string.ascii_uppercase.index(location[0])
    y = int(location[1]) - 1
    return (x,y)

# Palindrome
def palindrome(string):
    for i in range(len(string)):
        if string[i] != string[len(string) - 1 - i]:
            return False
    return True

# Main (for testing purposes)
print(palindrome("abcd"))