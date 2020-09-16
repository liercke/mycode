#!/usr/bin/env python3

calc1 = 0.0
calc2 = 0.0

operation = ""

while calc1 != "q":
    print("\nWhat is the first Operator? Or, enter q to quit: ")
    calc1 = input()
    if calc1 == "q":
        break
    calc1 = float(calc1)
    print("\nWhat is the second Operator? Or, enter q to quit: ")
    calc2 = input()
    if calc2 == "q":
        break
    calc2 = float(calc2)
    print("Enter an operation to perfrom on the two operators (+ or -):")
    operation = input()
    #print(type(calc1))
    #print(type(calc2))
    if operation == "+":
        #print('\n' + str(calc1) + " + " + str(calc2) + " = " + str(calc1 + calc2))
        print(f"\n {calc1} + {calc2} = {calc1 + calc2}")
    elif operation == "-":
        #print('\n' + str(calc1) + " + " + str(calc2) + " = " + str(calc1 - calc2))
        print(f"\n {calc1} - {calc2} = {calc1 - calc2}") 
    else:
        print("Not a valid etnry. Restarting...")
