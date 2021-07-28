# -*- coding: utf-8 -*-
"""
Created on Wed Jul 28 23:57:28 2021

@author: admin
"""
#"It is called Recursion when a function calls itself."
a = int(input("Give me a number: "))
def summe(num):
    # Base Case 
    if num == 1:
          
        return 1
    # Recursive Case 
    else:
        return num + summe(num - 1)
print("Sum of numbers up to {} is equal to {}".format(a,summe(a)))
