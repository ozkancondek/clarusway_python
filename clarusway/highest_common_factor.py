# -*- coding: utf-8 -*-
"""
Created on Thu Sep  2 19:38:11 2021

@author: admin
"""

# Highest common factor
def hcm(a,b):
    ls = []
    for i in range(1,max(a,b)):
        if a%i == 0 and b%i == 0:
            ls.append(i)
    return max(ls)
        
print(hcm(13,7))
 