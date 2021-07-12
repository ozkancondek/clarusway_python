# -*- coding: utf-8 -*-
"""
Created on Tue Jun 22 13:13:48 2021

@author: admin
"""
print("Please answer the questions to know corona risk.\n")
print(" Press direct to ENTER key if say no. Otherwise write somethink to say yes\n")
age = bool (input("Are you a cigarette addict older than 75 years old? "))
chronic = bool (input("Do you have a severe chronic disease? "))
immune =  bool (input("Is your immune system too weak?"))
risk =  age and (chronic or immune)
if risk == True:
    print("You are in Danger.")
else:
    print("There is no Danger")
    
