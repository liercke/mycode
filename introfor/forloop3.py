#!/usr/bin/env python3

farms = [{"name": "NE Farm", "agriculture": ["sheep", "cows", "pigs", "chickens", "llamas", "cats"]}, {"name": "W Farm", "agriculture": ["pigs", "chickens", "llamas"]}, {"name": "SE Farm", "agriculture": ["chickens", "carrots", "celery"]}]

farm_list = ["NE Farm", "cows", "sheep"]

for farm in farms:
    print("\nThe Farm is: " + farm['name'], end="") 
    if farm['name'] not in farm_list:
        print(" - and is NOT MY FARM!")
    else: 
        print("\nThis is my Farm and we deal with the follow:")
        for animal in farm["agriculture"]:
            print(animal)
print("\nOur Loop has ended")
