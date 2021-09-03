# -*- coding: utf-8 -*-
"""
Created on Fri Sep  3 17:21:00 2021

@author: admin
"""
 
ls = [1, 2, 3, 3, 6, 9]

def simplifier(ls):  
    for i in ls:
        c = ls.count(i)
        if c != 1:
            ls.remove(i)
            
    return ls

 