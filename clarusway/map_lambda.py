# -*- coding: utf-8 -*-
"""
Created on Thu Jul 29 15:08:10 2021

@author: admin
"""
#map(function, iterable)
iterable = [1, 2, 3, 4, 5]
map(lambda x:x**2, iterable)
result = map(lambda x:x**2, iterable)
print(type(result))  # it's a map type

print(list(result))  # we've converted it to list type to print

print(list(map(lambda x:x**2, iterable)))  # you can print directly
#Equal outputs---------------------------------------------------------
def square(n):   # at least two additional lines of code
    return n**2  
  
iterable = [1, 2, 3, 4, 5]
result = map(square, iterable) #map(function, iterable)
print(list(result))


#map(function, iterable)
letter1 = ['o', 's', 't', 't']
letter2 = ['n', 'i', 'e', 'w']
letter3 = ['e', 'x', 'n', 'o']
numbers = map(lambda x, y, z: x+y+z, letter1, letter2, letter3)

print(list(numbers))