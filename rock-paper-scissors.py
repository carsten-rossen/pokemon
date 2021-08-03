#!/usr/bin/python3

# Script Name: Rock Paper Scissors
# Author Name: Carsten Rossen
# Date of Latest Revision: 8/02/21
# Purpose: 

# Import libraries
import random

# Define functions
def round():
    choice = input("Would you like to guess rock, paper, or scissors? (1/2/3): ")
    if not (choice == "1" or choice == "2" or choice == "3"):
        print("Please only input a 1, 2, or 3.")
        choice = round()
    return choice

def result(choice, computer_choice):
    if choice == computer_choice:
        print("This round was a tie.")
    else:
        if (choice == "1" and computer_choice == "2") or (choice == "2" and computer_choice == "3") or (choice == "3" and computer_choice == "1"):
            print("The computer has won this round!")
        else:
            print("You have won this round!")
        

def choice_is(choice):
    if choice == "1":
        return "rock"
    elif choice == "2":
        return "paper"
    else:
        return "scissors"


def play_again():
    result = input("Would you like to play another round? (y/n): ")
    if result == "y":
        return True
    elif result == "n":
        return False
    else:
        print("Please only input y/n.")
        new_result = play_again()
        return new_result

# Main
keep_playing = True
while keep_playing:
    choice = round()
    computer_choice = str(random.randint(1, 3))
    user_is = choice_is(choice)
    computer_is = choice_is(computer_choice)
    print(f"You have guessed {user_is} and the computer has guessed {computer_is}")
    result(choice, computer_choice)
    keep_playing = play_again()

# End
