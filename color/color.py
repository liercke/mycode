#!/usr/bin/env python3

"""
This script prompts users for their name and asks what colors to present them in

"""

import crayons

firstname = input("Input your First Name: ")
lastname = input("Input your Last Name: ")

def color_chooser(color, name):
    """
    Chooses a color
    """
    if color.lower() == "red":
        print(crayons.red(name, bold=True))
    elif color.lower() == "green":
        print(crayons.green(name, bold=True))
    elif color.lower() == "blue":
        print(crayons.blue(name, bold=True))
    else:
        print(crayons.magenta(name, bold=True))

print("These are the available colors:")
print(crayons.red("Red"))
print(crayons.green("Green"))

fname_color = input("What color would you like your First Name to be?")
lname_color = input("What color would you like your Last Name to be?")

color_chooser(fname_color, firstname)
color_chooser(lname_color, lastname)
