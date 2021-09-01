# -*- coding: utf-8 -*-
"""
Created on Wed Sep  1 15:57:51 2021

@author: admin
"""
"""
A left-truncatable prime is a prime number that contains no 0 digits and, when the first digit is successively removed, the result is always prime.
If the integer is only a left-truncatable prime, return "left".
If the integer is only a right-truncatable prime, return "right".
If the integer is both, return "both".
Otherwise, return False.
"""
from prime_function import prime

num = int(input("Enter a number: "))

def trucatable(num):
    x = prime(num)
    if x == None:
        return "Number is not Prime!!!"
    elif "0" in str(x):
        return False
    elif x in [2,3,5,7]:
        return "both"
    else:
        if (  prime(int(str(x).replace(str(x)[0], ""))) != None) and ( prime(int(str(x).replace(str(x)[len(str(x))-1], ""))) != None):
            return "Both"
        elif prime(int(str(x).replace(str(x)[len(str(x))-1], ""))) != None:
            return "Right"
        elif  prime(int(str(x).replace(str(x)[0], ""))) != None:
            return "Left"
        else:
            return False
        
print(trucatable(num))
        
            