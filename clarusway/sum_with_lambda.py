# -*- coding: utf-8 -*-
"""
Created on Thu Aug  5 21:58:47 2021

@author: admin
"""
#Given two integer values, return their sum. 
#If the two values are the same, then return double their sum.
def sum(a,b):
    if a == b:
        return (a+b)*2
    else:
        return a+b
    
print(sum(5,4))
#------solution with function lambda----------------
x = lambda a,b : (a+b)*2 if a == b else a+b
print(x(8,5))

       
 