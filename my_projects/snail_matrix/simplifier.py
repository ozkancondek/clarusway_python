# -*- coding: utf-8 -*-
"""
Created on Fri Sep  3 17:21:00 2021

@author: admin
"""
 
ls = [1, 2, 3, 3, 6, 9,1]

def simplifier(ls):  
     for i in ls:
       a = ls.count(i)
       if a != 1:
           ls.reverse()
           ls.remove(i)
           ls.reverse()
       
       
            
     return ls

 
 