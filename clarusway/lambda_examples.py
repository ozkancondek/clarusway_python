# -*- coding: utf-8 -*-
"""
Created on Thu Jul 29 00:44:20 2021

@author: admin
"""

  
#lambda examples
x = lambda a : a + 10
print(x(5))

x = lambda a, b : a * b #Equal to def func(a,b): -->  return a*b 
print(x(5, 6))

x = lambda a, b, c : a + b + c
print(x(5, 6, 2))

def myfunc(n):
  return lambda a : a * n  #a paramater is belong to lambda function and n is to myfunc()

mydoubler = myfunc(2)
mytripler = myfunc(3)

print(mydoubler(11))
print(mytripler(11))