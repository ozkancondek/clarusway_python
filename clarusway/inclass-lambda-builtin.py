# -*- coding: utf-8 -*-
"""
Created on Wed Aug 18 19:04:54 2021

@author: admin
"""

#inclass--Lambda within User-Defined Functions
def func(n):
    return lambda x:x**n

power_2 = func(2) # power_2 is works like a new function 
power_3 = func(3)
power_4 = func(4)

print(power_2(2))
print(power_3(2))
print(power_4(2))

#----------------string repeater--------------------
def repeater(n):
    return lambda x :x*n

mult_3 = repeater(3)
mult_4 = repeater(4)
mult_5 = repeater(5)

print(mult_3("*"))
print(mult_4("*"))
print(mult_5("*"))
 
#----------emoji an message----------
def functioner(n):
    return lambda x:print(x,n)

smile = functioner(":)")
sad = functioner(":(")
neutral = functioner(":|")


smile(1)
sad(2)
neutral("*")

#----------------------
c =  lambda a : a + ":)"
print(c("hello "))
