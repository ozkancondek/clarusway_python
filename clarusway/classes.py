# -*- coding: utf-8 -*-
"""
Created on Sat Aug 14 23:37:44 2021

@author: admin
"""

#Python Classes 
class myclass():
    x = 5
a = myclass()
print(a.x)
 
#All classes have a function called __init__(), which is always executed when the class is being initiated.
class Person:
  def __init__(self, name, second_name, age):
    self.name = name
    self.second_name = second_name
    self.age = age

p1 = Person("John","Diheart", 36)

print(p1.name)
print(p1.second_name)
print(p1.age)


#class definitions cannot be empty, but if you for some reason
# have a class definition with no content, put in the pass statement
# to avoid getting an error.
class Person_1:
  pass