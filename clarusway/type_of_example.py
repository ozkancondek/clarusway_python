# -*- coding: utf-8 -*-
"""
Created on Mon Jul 12 19:37:52 2021

@author: admin
"""
sample_list = [{"section":5, "topic":2}, 'clarusway', [1, 4], 2020, 3.14, 1+618j, False, (10, 20)]

for i in range (len(sample_list)):
    t = type(sample_list[i])
    print (f"The type of {sample_list[i]} is {t}")
    i+=1 
    
    
 
  
    
    