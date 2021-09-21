#!/usr/bin/python3

# Script Name: Currency Converter
# Author Name: Carsten Rossen
# Date of Latest Revision: 8/19/21 
# Purpose: This program will convert between currencies using the a GUI interface. 
# I will achieve this with the Tkinter library. (Learning from this video: https://www.youtube.com/watch?v=YXPyB4XeYLA) 38.51

# Import libraries
from tkinter import *


# Declare variables
root = Tk()
main_label = Label(root, text="Currency Converter")
description = Label(root, text="This program will converter currencies to other currencies.")


# Declare functions
def choose_currency():
    choose_label = Label(root, text="Starting currency")
    choose_label.grid(row=0, column=0)
    choose_description = Label(root, text="Choose a currency from the ones listed below.")
    choose_description.grid(row=1, column=0)


# Main
main_label.grid(row=0, column=0)
description.grid(row=1, column=0)
nextbutton = Button(root, text="Next", command=choose_currency)
nextbutton.grid(row=3)


root.mainloop()


