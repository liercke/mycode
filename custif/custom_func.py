#!/usr/bin/env python3

def bandwidth(): #Define the function name
    import crayons
    openfile = open("test.csv", "r") #Open the file
    readfile = openfile.read() #Read the file
    filesplit = readfile.splitlines() #Separate each row

    for x in filesplit: #Loop through each row
        message = "The movie is about to begin..." #Define the inital user message
        if int(x) >= 25:
            message = f"{message} since your bandwidth is {x}, we recommend setting video to 4k." 
            #Display the specific message in GREEN
            print(crayons.green(message, bold=True))
        elif int(x) >= 5:
            message = f"{message} since your bandwidth is {x}, we recommend setting video to 1080p." 
            #Display the specific message in YELLOW
            print(crayons.yellow(message, bold=True))
        elif int(x) >= 2:
            message = f"{message} since your bandwidth is {x}, we recommend  setting video to 720p." 
            #Display the specific message in RED
            print(crayons.red(message, bold=True))
        else:
            message = f"{message} Since your bandwidth is {x}, we recommend finding another provider." 
            #Display the specificmessage in MAGENTA
            print(crayons.magenta(message, bold=True))        
       
bandwidth() #Run the function
