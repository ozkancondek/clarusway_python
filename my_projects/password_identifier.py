# -*- coding: utf-8 -*-
"""
Created on Mon Aug 23 15:32:21 2021

@author: admin
"""
import random
a = chr(random.randint(65,90)) # chr(x) gets an character from ascii table. 65-90 upper_cases
 
uppers  =[chr(random.randint(65,90)) for i in range(3)]
x = "".join(uppers)   # "-"-->K-L-M
lowers = [chr(random.randint(97,122)) for i in range(3)]
y = "".join(lowers)
numbers = [chr(random.randint(48,57)) for i in range(3)]
z = "".join(numbers)
chars = [chr(random.randint(33,47)) for i in range(3)]
t = "".join(chars)
password = x+y+z+t

print(password)
 
 
def shf(password):
    ls= list(password)
    random.shuffle(ls) # shufles iterable
    return "".join(ls)

print(shf(password))
 

 
    