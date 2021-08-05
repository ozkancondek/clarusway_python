# -*- coding: utf-8 -*-
"""
Created on Thu Aug  5 16:53:59 2021

@author: admin
"""

 
def perfect(num):
    result = 0
    
    a = [i for i in range(1,num) if num%i == 0]
    for j in a:
        result = result + j
     
    print( "Perfect number." if result == num else "It`s not a perfect number.")
perfect()