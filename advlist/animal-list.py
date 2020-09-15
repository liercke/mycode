#!/usr/bin/env python3

animal_list = ["Fly", "Fly", "Ant", "Bee", "Cod", "Cat", "Dog", "Yak", "Fly", "Hen", "Koi", "Hog", "Jay", "Fly"]

print(animal_list)


counter = animal_list.count("Fly")

print(counter)

print(animal_list.count("Fly"))

pets = ["fido", "spot", "fluffy"]

input1 = input("Input First Pet Name: ")
input2 = input("Input Second Pet Name: ")
input3 = input("Input Third Pet Name: ")

input_pets = [input1, input2, input3]

pets.append(input1)
pets.insert(1, input2)
pets.insert(1, input3)

print(pets)

index0 = str(pets.index(pets[0]))
index1 = str(pets.index(pets[1]))
index2 = str(pets.index(pets[2]))
index3 = str(pets.index(pets[3]))
index4 = str(pets.index(pets[4]))
index5 = str(pets.index(pets[5]))


counter = 0

for pet in pets:
    print(counter, pet)
    counter +=1

