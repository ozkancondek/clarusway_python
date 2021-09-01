# -*- coding: utf-8 -*-
"""
Created on Wed Sep  1 15:57:51 2021

@author: admin
"""

 

def prime(num):
     for i in range(2,num):
         if (num % i )== 0:
             return None
             break
     else:
        return num
             
        
 