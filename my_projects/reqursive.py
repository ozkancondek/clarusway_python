# -*- coding: utf-8 -*-
"""
Created on Wed Jul 28 23:59:58 2021

@author: admin
"""
a = int(input("Give me a number: "))
def factoriel(x):
    if x == 0:
        return 1
    else:
        return x * factoriel(x-1)
    
print("The factorial of the {} is equal to {}.".format(a,factoriel(a)))
  
