#!/usr/bin/python3

# Script Name: Currency Converter
# Author Name: Carsten Rossen
# Date of Latest Revision: 8/19/21 
# Purpose: This program will convert between currencies using the a GUI interface. 
# I will achieve this with the Tkinter library. (Learning from this video: https://www.youtube.com/watch?v=YXPyB4XeYLA) 29:31

# Import libraries
from tkinter import *


# Declare variables
root = Tk()
main_label = Label(root, text="Currency Converter")
description = Label(root, text="This program will converter currencies to other currencies.")


# Main
main_label.grid(row=0, column=0)
description.grid(row=1, column=0)
root.mainloop()