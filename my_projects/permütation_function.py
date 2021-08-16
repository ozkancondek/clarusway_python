# -*- coding: utf-8 -*-
"""
Created on Sun Aug 15 01:25:36 2021

@author: admin
"""


def permütation(a,b):
    n_fact = 1
    s_fact = 1
     
    for i in range(1,a+1):
        n_fact=n_fact*i
    for j in range((a-b),0,-1):
        s_fact=s_fact*j
    return n_fact / s_fact

print(int(permütation(89, 5)))
    
     