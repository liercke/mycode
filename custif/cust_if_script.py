#!/usr/bin/env python3

message = "The grade you should expect is "

grade = float(input("What is the numeric grade? "))

if grade >= 90:
    message = message + "A"
elif grade >= 80:
    message = message + "B"
elif grade >= 70:
    message = message + "C"
elif grade >= 60:
    message = message + "D"
else:
    message = "YOU HAVE FAILED THE CLASS!!! RECONSIDER YOUR OPTIONS!!! IT'S AN F!!!"

print(message)
