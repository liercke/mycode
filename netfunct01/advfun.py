#!/usr/bin/env python3

def func1(x):
    """
    Accepts the required positional argument x
    returns the value of x + 25
    """
    return x + 25


def func2(y, z=100):
    """
    Accepts the required positional argument y
    Accepts an optional keyword argment z
    Returns Value of y + z
    """

    return y + z


userinput = int(input("Enter a number: "))

print(func1(userinput))


def our_print(*txt):
    print(txt)

our_print("Hi Steve", "Hi Becky", "Hi Bob")


def print_name(fname, lname, mname=None):
    if mname:
        print(fname, mname, lname)
    else:
        print(fname, lname)

fname = input("Enter your First Name: " )
mname = input("Enter your Last Name: ")
lname = input("Enter your Middle Name: ")
print_name(fname, mname, lname)
