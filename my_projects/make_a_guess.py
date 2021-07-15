# -*- coding: utf-8 -*-
"""
Created on Thu Jun 17 22:23:36 2021

@author: admin
"""
import random

print("\tWelcome to GuessMyNumber game\n")
print("I will make a guess in every try a number between 2 and 8\n")
print("And i will also say to you is it lower or higher\n")
print("You have 5 attempts\n")
print("****Lets start****")

guess = int(input("make a guess"))

real = random.randint(2,5)
attempt  = 1
if guess<2 and guess>8:
    print("make a guess between 2 and 8")
    guess = int(input("make a guess"))
while real != guess:
    if real < guess:
        print("lower")
    else:
        print("lower")
    guess = int(input("make a new guess"))
    attempt += 1
    if attempt == 9:
        print("sory: you losed")
        break
if guess == real:
   print("concracilations\n")
   print(real," is correct and you have made ",attempt," attempt")     
    
    


