# -*- coding: utf-8 -*-
"""
Created on Fri Aug 13 18:44:33 2021

@author: admin
"""

ls = [5, 7, 11, 35, 55, 77]

def common_multiple(ls):
    result = 1
    
    for i in ls:
        result = result * i
        for j in ls:
            if result % j != 0:
                result = result*j
        break
    print(result)
    
common_multiple(ls)
        
            
     
    
        
 
    