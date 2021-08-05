# -*- coding: utf-8 -*-
"""
Created on Thu Aug  5 16:54:00 2021

@author: admin
"""


def perfect(limit):
    """ This function will give to user the list of perfect numbers from 0 to entered limit."""
    k = []
    b = 0
    for x in range(2,limit):
       a = [i for i in range(1,x) if x%i == 0]
       for y in a:
           b = b + y
       if b == x:
           k.append(x)
       b = 0
    print(k) 
perfect(500)