#!/usr/bin/env python3

round = 0

answer = " "

while round < 3 and answer != "brian":
    round +=1
    answer = input('Finish the movie title, "Monty Python\'s The Life of _____":')
    if answer.lower() == "brian":
        print("Correct")
        break
    elif answer.upper() == "BRIAN":
        print("Correct")
        break
    elif answer == "shrubbery":
        print("You gave the super secret answer!")
        break
    elif round ==3:
        print("Sorry, the answer was Brian")
        break
    else:
        print("Sorry Try Again!")

