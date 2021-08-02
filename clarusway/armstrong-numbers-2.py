# -*- coding: utf-8 -*-
"""
Created on Mon Aug  2 19:11:53 2021

@author: admin
"""
#armstrong number example. Invalid Value pert is different
while True:
    number = input("Enter a positive integer number: ")
    digit = len(number)
    result = 0
    
    if not number.isdigit():
        print(number, " is invalid entry. Enter valid input:")
    elif int(number) >= 0:
        for i in range(digit):
            result = result +  int(number[i])**digit
        if result == int(number):
            print(number, " is an Armstrong number")
            break
        else:
            print("its not an Armstrong number.") 
            break