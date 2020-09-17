#!/usr/bin/env python3

from subprocess import call
import netifaces

runfirstcode = input("Would you like to run the first code? (y or n): ")

if runfirstcode == "y":

    call(["ip", "link", "show", "up"])

    print("This program will check your interface")

    interface = input("Enter an interface, like, ens3: ")

    call (["ip", "addr", "show", "dev", interface])

    call (["ip", "route", "show", "dev", interface])
else:
    print("\n")

askwireshark = input("Would you like to run wireshark?\n").lower()
if askwireshark == "y":
    print("Below is a list of Interfaces: \n")
    print(netifaces.interfaces())
    interfacename = input("Enter an interface name: \n")
    call (["wireshark", "-i", interface])
else:
    print("You did not want to run wireshark!")


command = ""

print("What details do you want to see?\n")
print("1 - Verify routing table")
print("2 - Interface Details")

command = input("Please select an option above:\n")
if command == "1":
    call(["netstat", "-rn"])
else:
    call(["ifconfig"])            
