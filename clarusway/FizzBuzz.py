# -*- coding: utf-8 -*-
"""
Created on Thu Aug 12 17:35:09 2021

@author: admin
"""
ls = []
for i in range(1,101):
    if i%3 == 0 and i%5 == 0:
        i = "FizzBuzz"
        ls.append(i)
    elif i%5 == 0:
        i = "Buzz"
        ls.append(i)
    elif i%3 == 0:
        i = "Fizz"
        ls.append(i)
    else:
        ls.append(i)
        
print(ls)
 