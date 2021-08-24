#!/usr/bin/python3

# Script Name: Currency Converter
# Author Name: Carsten Rossen
# Date of Latest Revision: 8/19/21 
# Purpose: This program will convert between currencies using the a GUI interface. 
# I will achieve this with the Tkinter library. (Learning from this video: https://www.youtube.com/watch?v=YXPyB4XeYLA)

# Import libraries
from tkinter import *


# Declare variables
root = Tk()
main_label = Label(root, text="Currency Converter")


# Main
main_label.pack()
root.mainloop()