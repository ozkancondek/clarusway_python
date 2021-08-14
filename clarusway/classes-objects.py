# -*- coding: utf-8 -*-
"""
Created on Sat Aug 14 23:47:19 2021

@author: admin
"""

#Python Objects
#Objects can also contain methods. Methods in objects are functions that belong to the object.
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self): #The self parameter is a reference to the current instance of the class, and is used to access variables that belong to the class.
    print("Hello my name is " + self.name)

p1 = Person("John", 36)
p1.myfunc()

class ozkan:
    def __init__(first,name,age):
        first.name = name
        first.age = age
        
    def func(abc):
        print("hello, my name is ", abc.name)
        
x = ozkan("ozkan",24)
x.age = 40 #Modify Object Properties
#del x.age  #Delete Object Properties
#del p1  #Delete Objects
x.func()
print(x.age)
        