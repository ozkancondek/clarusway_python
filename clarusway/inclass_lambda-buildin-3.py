# -*- coding: utf-8 -*-
"""
Created on Wed Aug 18 20:19:11 2021

@author: admin
"""

 
def function_generator(n):
    return lambda x: n(x)


myPrint =  function_generator(print)
myMax = function_generator(max)
myBool = function_generator(bool)
mySorted = function_generator(sorted)
print(myBool(1))
print(myMax([5,1,7,8])) 


 