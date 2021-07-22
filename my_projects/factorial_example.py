# -*- coding: utf-8 -*-
"""
Created on Thu Jul 22 13:45:06 2021

@author: admin
"""

num = int(input("Give me a number: "))
 
def factorial(num):
    result = 1
    if num == 0:
        return 1
    for i in range(1,num + 1):
        result = result * i
    return result
print(f"The factorial of {num} is equal to {factorial(num)}.") 