# -*- coding: utf-8 -*-
"""
Created on Mon Jul 12 20:39:12 2021

@author: admin
"""

num = int(input("Give me a number "))
if  num > 1:
    for i in range(2,num):
        if (num % i) == 0:
            print(f"{num} is not a prime number.")
            print(f"{i} time {num//i} is equal to {num}.")
            break
    else:
     print(f"{num} is a prime number.")
else:
    print(f"{num} is not a prime number.") 