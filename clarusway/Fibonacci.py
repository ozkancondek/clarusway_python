# -*- coding: utf-8 -*-
"""
Created on Tue Jul 20 19:15:49 2021

@author: admin
"""


fibonacci = [0,1]

 
for i in range(20): 
    a = fibonacci[i] + fibonacci[i+1]
    fibonacci.append(a)
    i += 1
    if a > 50:
        break
       
print (fibonacci) 
 
