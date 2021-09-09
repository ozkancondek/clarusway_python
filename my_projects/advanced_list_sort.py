# -*- coding: utf-8 -*-
"""
Created on Thu Sep  9 19:36:32 2021

@author: admin
"""

#Create a function that takes a list of numbers or strings and returns a list with the items from the original list stored into sublists. 
#Items of the same value should be in the same sublist.



def advanced_sort(ls):
    ls1 = []
    end_ls = []
    for i in ls:
        x = ls.count(i)
        ls1=[i for j in range(x)]
        end_ls.append(ls1)
        ls1 = []
    for y in end_ls:
        if end_ls.count(y) != 1:
            for n in range( end_ls.count(y)-1):
                end_ls.remove(y)
    return end_ls     
           
        
        
            
        
        

print(advanced_sort(["b", "a", "b", "a", "c"]))