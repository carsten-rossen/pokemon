#!/usr/bin/python3

# Script Name: Rock Paper Scissors
# Author Name: Carsten Rossen
# Date of Latest Revision: 8/16/21
# Purpose: Play the computer in a game (or many games) of rock, paper, scissors!


# Import libraries
import random


# Define variables
COUNT_USER = 0
COUNT_ROUNDS = 0


# Define functions

# Prompt the user for a choice between rock, paper, and scissors
def round():
    choice = input("\nWould you like to guess rock, paper, or scissors? (1/2/3): ")
    print()
    # User must input only rock, paper, or scissors (no lizard or Spock)
    if not (choice == "1" or choice == "2" or choice == "3"):
        print("Please only input a 1, 2, or 3.")
        choice = round()
    return choice

# Print the result of the round
def result(choice, computer_choice, COUNT_ROUNDS, COUNT_USER):
    COUNT_ROUNDS += 1 
    if choice == computer_choice:
        print("This round was a tie.")
    else:
        if (choice == "1" and computer_choice == "2") or (choice == "2" and computer_choice == "3") or (choice == "3" and computer_choice == "1"):
            print("The computer has won this round!")
        else:
            print("You have won this round!")
            COUNT_USER += 1
    return COUNT_ROUNDS, COUNT_USER
        
# Convert number to a string of the corresponding choice
def choice_is(choice):
    if choice == "1":
        return "rock"
    elif choice == "2":
        return "paper"
    else:
        return "scissors"

# Prompt the user to play again
def play_again():
    result = input("\nWould you like to play another round? (y/n): ")
    if result == "y":
        return True
    elif result == "n":
        return False
    else: # Reprompt the user if they input a character that isn't y/n
        print("Please only input y/n.")
        new_result = play_again()
        return new_result

# Main
keep_playing = True

while keep_playing:
    choice = round() # Get user's choice
    computer_choice = str(random.randint(1, 3)) # Get computer's choice

    # Convert user and computer's choices to strings (i.e. converts 1 to "rock")
    user_is = choice_is(choice)
    computer_is = choice_is(computer_choice)

    print(f"You have guessed {user_is} and the computer has guessed {computer_is}")
    COUNT_ROUNDS,COUNT_USER = result(choice, computer_choice, COUNT_ROUNDS, COUNT_USER) # Print result of the round
    keep_playing = play_again() # Prompt the user to play again

print(f'\nYou have won {COUNT_USER/COUNT_ROUNDS}% of the rounds.') # Print statistics from all rounds

# End
