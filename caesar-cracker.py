#!/usr/bin/python3

# Script Name: Caesar Cracker
# Author Name: Carsten Rossen
# Date of Latest Revision: 7/19/21
# Purpose: Cracks a phrase that has been encrypted using a caesar cipher.


# Import libraries

# Note: To use this library you must first install it using 'pip install english-words'
from english_words import english_words_set
import string


# Define functions

# Transpose message up or down and look for words are in the english dictionary
# This program will only work with messages that contain only words in the english_words_set library
def change_cipher(phrase, count, diff):
    new_phrase = ""
    fin = False
    count+=1
    # Keeps the program from failing because of too many iterations
    if count == 995:
        return 0
    else:
        # Transpose each letter in the encrypted message
        for letter in phrase:
            # do not transpose spaces
            if letter != ' ':
                letter = chr(ord(letter) + diff)
            new_phrase += letter
            # Keeps the program from failing if the message cannot be transposed further
            if letter == 'a':
                fin = True
        if fin:
            return 0
        # Test each word of the message against the english_words_set library
        for word in new_phrase.split():
            if word not in english_words_set:
                # If not every word from the message matches a word from the english_words_set library,
                # this starts a recursive process to keep transposing the message
                new_phrase = change_cipher(new_phrase, count, diff)
                break
        return new_phrase
    

# Main

# Ask the user for the encrypted message
phrase = input("Please input the encrypted phrase: ")
new_phrase = change_cipher(phrase, 0, 1)
# A zero indicates that the message could not be decrypted using words in the english_words_set library
if new_phrase == 0:
    # Try transposing backwards to see if the message can be decrypted this way
    new_phrase = change_cipher(phrase, 0, -1)
if new_phrase == 0:
    # Prepare results of the program
    new_phrase = "Your message could not be decrypted using this Caesar Cipher decryption tool."
else: new_phrase = "Your decrypted message is: " + new_phrase
# Print results
print(new_phrase)


# End
