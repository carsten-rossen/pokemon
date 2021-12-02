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


# Up and down
def up_down(number):
    return(number - 1, number + 1)


# Consecutive zeros
def consecutive_zeros(string):
    count = 0
    new_count = 0
    for char in string:
        if char == '1':
            new_count = 0
        else: 
            new_count += 1
            if new_count > count:
                count = new_count
    return count


# All equal
def all_equal(lst):
    for element in lst:
        if element != lst[0]:
            return False
    return True


# Boolean and
def triple_and(x, y, z):
    if x != True or y != True or z != True:
        return False
    return 1 and True


# Writing Short Code
def convert(numbers):
    return [str(num) for num in numbers]


# List xor
def list_xor(n, list1, list2):
    if n in list1 and n in list2:
        return False
    elif n not in list1 and n not in list2:
        return False
    else:
        return True


# Counting parameters
def param_count(*args):
    return len(args)


# Thousands separator
def format_number(num):
    snum = ''
    while num // 1000 > 0:
        if num % 1000 == 0:
            nextval = "000"
        else:
            nextval = str(num % 1000)
        snum  = "," + nextval + snum
        num = num // 1000
    snum = str(num) + snum
    return snum 

# Main (for testing purposes)
print(convert([1,2,3]))
