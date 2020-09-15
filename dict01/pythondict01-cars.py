#!/usr/bin/env python3

cars = [{'type': 'challenger', 'year': '2001', 'color': 'red'}, {'type': 'charger', 'year': '2005', 'color': 'white'}]

print(cars)

#print(cars[1]['year'])

for car in cars:
    print(f"I want a {car['color']} {car['type']} from {car['year']}.")
