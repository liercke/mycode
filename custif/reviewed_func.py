#!/usr/bin/env python3
import crayons
from subprocess import call
from time import sleep
 
def bandwidth(): #Define the function name
    openfile = open("test.csv", "r") #Open the file, "r" to read
    outfile = open("output.txt", "a") #Define a file to output the results to, "a" to append
    filesplit = openfile.readlines() #Read the file
    for x in filesplit: #Loop through each row
        x = x.split(',')
        speed = x[0]
        carrier = x[1]
        message = "The movie is about to begin..." #Define the inital user message
        mess = resolution(message, speed, carrier)
        outfile.write(mess)
    #Clean things up by closing the input and outfile files
    openfile.close()
    outfile.close()



def resolution(message, speed, carrier):
    if int(speed) >= 25:
        message = f"{message} since your bandwidth is {speed}, and your carrier is {carrier}, we recommend setting video to 4k." 
        #Display the specific message in GREEN
        print(crayons.green(message, bold=True))
    elif int(speed) >= 5:
        message = f"{message} since your bandwidth is {speed}, and your carrier is {carrier}, we recommend setting video to 1080p." 
        #Display the specific message in YELLOW
        print(crayons.yellow(message, bold=True))
    elif int(speed) >= 2:
        message = f"{message} since your bandwidth is {speed}, and your carrier is {carrier}, we recommend setting video to 720p." 
        #Display the specific message in RED
        print(crayons.red(message, bold=True))
    else:
        message = f"{message} Since your bandwidth is {speed}, and your carrier is {carrier}, we recommend finding another provider." 
        #Display the specific message in MAGENTA
        print(crayons.magenta(message, bold=True))
    return message


def look_at_file():
    print("\nAll of the above results have been saved to a file named output.txt")
    #Display a message that shows we are now opening the file
    print("\n\n\nWe are now opening the file, please wait...")
    #Wait for 5 seconds
    sleep(3)
    #Now display the file that was generated from running the script
    call(["cat", "output.txt"])
    #Show the file exists in this directory
    print(crayons.green("\nWe are now showing the file exists in this directory."))
    call(["ls", "output.txt"])
    sleep(3)
    #Now lets delete the file that was created
    print(crayons.green("\nWe are now deleting the file"))
    call(["rm", "output.txt"])
    #Show that the file no longer exists
    call(["ls", "output.txt"])
    sleep(3)
    print(crayons.green("\nYou can now see the file no longer exists!"))


def main():
    bandwidth() #Run the function
    look_at_file()


main()
