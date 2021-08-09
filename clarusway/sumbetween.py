# -*- coding: utf-8 -*-
"""
Created on Mon Aug  9 13:30:59 2021

@author: admin
"""
#get two number from the user and write a function that sums all numbers
#betwwen two input. Those two number will not included to sum.

first = int(input("Give me the first number: "))
second = int(input("Give me the second number: "))
 
def between_sum(first,second):
    summe = 0
    if first <= second :
       for i in range(first+1,second):
           summe = summe + i 
    else:
        for i in range(second+1,first):
           summe = summe + i 
    return summe       
         
print(f"Sum of numbers between {first} and {second} is: {between_sum(first,second)}.")
 
    