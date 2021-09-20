# -*- coding: utf-8 -*-
"""
Created on Mon Sep 20 22:54:35 2021

@author: admin
"""

#Sort list in ascendeing number by the second element


ls = [('b', 1), ('c', 2), ('x', 3), ('x', 4), ('z', 0)]
 
 
result = sorted(ls, key = lambda x:x[1])
print(result)