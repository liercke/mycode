#!/usr/bin/env python3

message = "The movie is about to begin, we recommend "

connection = float(input("What is your connection speed in Mbps?"))

if connection >= 25:
    message = message + "setting video to 4k."
elif connection >= 5:
    message = message + "setting video to 1080p."
elif connection >= 2:
    message = message + "setting video to 720p."
else:
    message = message + "finding another access network."

print(message)
