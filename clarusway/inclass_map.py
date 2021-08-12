# -*- coding: utf-8 -*-
"""
Created on Thu Aug 12 20:15:13 2021

@author: admin
"""

#map  object
#map(function,*iterable) applies this function for every elements of iterable.You can also send an iterable more than one.
iterable = [1,2,3,4,5,6]

result = map(lambda x:x**2,iterable)
print(result)
print(list(result))

#---def and map

def a(x):
    return x**2
iterable = [1,2,3,4,5,6]
a = map(a,iterable)
print(list(a))
#----------
#first of all x for iterable1
#than y for iterable 
#than z for iterable3
letter1 = ['o', 's', 't', 't']
letter2 = ['n', 'i', 'e', 'w']
letter3 = ['e', 'x', 'n', 'o']
numbers = map(lambda x, y, z: x+y+z, letter1, letter2, letter3)
print(list(numbers))
#--------avarage of two list
num1 = [1,2,3,4]
num2 = [11,22,33,44]
a = map(lambda x,y : (x+y)/2, num1,num2)
print(list(a))
#--------
 
  





















