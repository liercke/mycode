#!/usr/bin/env python3

import netifaces

print(netifaces.interfaces())

interface_name = input("Which interface do you want to look at?").lower()
macorip = input("What do you want to display? (mac or ip): ").lower()

for i in netifaces.interfaces():    
    if i == interface_name:
        print("\n**********DETAILS OF INTERFACE - " + i + " **********")
        try:
            if macorip == "mac":
                print("MAC: ", end="")
                print((netifaces.ifaddresses(i)[netifaces.AF_LINK])[0]["addr"])
            elif macorip == "ip":
                print("IP Address: ", end="") 
                print((netifaces.ifaddresses(i)[netifaces.AF_INET])[0]["addr"])
            else:
                print("You selected an invalid parameter")
        except:
            print("failed")
