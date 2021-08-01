# -*- coding: utf-8 -*-
"""
Created on Thu Jul 29 14:19:30 2021

@author: admin
"""
#These two functions are same
#1
def square(x):
    return x**2
#2 
lambda x: x**2
 
#conditional syntax
a = lambda x: 'odd' if x % 2 != 0 else 'even'
 
#---------------------
(lambda x: x**2)(3)
#same call methods
a = lambda x: x**2
a(3)
#--------------------
#------------------------------------
average = lambda x, y: (x+y)/2
print(average(3, 5) )
#Also those are equal
average = (lambda x, y: (x+y)/2)(3, 5) 
print(average)
#-----------------------------------

