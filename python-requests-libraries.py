#!/usr/bin/python3

# Script Name: Python Requests Libraries (Challenge 13)
# Class Name: Ops 301
# Author Name: Carsten Rossen
# Date of Latest Revision: 3/17/21
# Purpose: 

# Import libraries
import requests as req 

# Declaration of variables
options = ['GET', 'POST', 'PUT', 'DELETE', 'HEAD', 'PATCH', 'OPTIONS']


# Main
def pick_request():
    url = input('What is the destination URL? ')
    print('\nHTTP Method options:')
    i = 1
    for method in options:
        print(f'  {i}) {method}')
        i += 1

    while True:
        choice = input('\nPlease enter a number corresponding to an option above: ')

        if choice.isdigit() and int(choice) >= 1 and int(choice) <= 7:
            break
    
    answers = [options[int(choice)-1], url]

    print(f'\nYou are about to send a(n) {answers[0]} request to {answers[1]}.')
    
    while True:
        proceed = input('\nWould you like to proceed? (y/n): ')
        if proceed == 'y':
            break
        elif proceed == 'n':
            answers = pick_request()
            break
        else:
            print("Please enter 'y' to proceed or 'n' to start over.")

    return answers
    
answers = pick_request()

response = getattr(req, answers[0].lower())(answers[1])
print(response)


    




# print(req.get(url))