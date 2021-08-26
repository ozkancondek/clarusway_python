# -*- coding: utf-8 -*-
"""
Created on Thu Aug 26 22:35:01 2021

@author: admin
"""

num1 = int(input("Enter a number: "))
num2 = int(input("Enter a number: "))
dic = {}
def square(num1,num2): 
    for i in range(num1,num2+1):
        if i % 2 != 0:
            dic[i] = i**2
    return dic
 
print(square(num1, num2))
        
        
 