# -*- coding: utf-8 -*-
"""
Created on Sat Aug 14 23:55:58 2021

@author: admin
"""

#Python Modules
#Consider a module to be the same as a code library.
#A file containing a set of functions you want to include in your application.

#Save this code in a file named mymodule.py
def greeting(name):
  print("Hello, " + name)
  #Import the module named mymodule, and call the greeting function:
#New pyhton page--------
import mymodule
mymodule.greeting("Jonathan")

#-------------
person1 = {
  "name": "John",
  "age": 36,
  "country": "Norway"
}
# Save a file an open new one
import mymodule as mx #Create an alias for mymodule called mx:

a = mx.person1["age"]
print(a)

#Built-in Modules
#There are several built-in modules in Python, which you can import whenever you like.
import platform

x = platform.system()
print(x)
#Using the dir() Function
#There is a built-in function to list all the function names (or variable names) in a module. The dir() function:
import platform

x = dir(platform)
print(x)
#Import From Module
#You can choose to import only parts from a module, by using the from keyword.
#The module named mymodule has one function and one dictionary:
def greeting(name):
  print("Hello, " + name)

person1 = {
  "name": "John",
  "age": 36,
  "country": "Norway"
}
#Import only the person1 dictionary from the module:
from mymodule import person1

print (person1["age"])
#Note: When importing using the from keyword, do not use the module name when referring to elements in the module.
# Example: person1["age"], not mymodule.person1["age"]