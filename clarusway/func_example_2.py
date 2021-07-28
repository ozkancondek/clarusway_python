# -*- coding: utf-8 -*-
"""
Created on Wed Jul 28 23:57:20 2021

@author: admin
"""

def func(name = "ozkan"):
    print("my name is ", name)
    
func("Jane")
func()
func("Jonah")
#2
def func_1(numbers): 
    ls_1 =[]
    for i in numbers:
      ls_1.append(i)
    print(ls_1)
ls = [1,2,3,4,5,6,7,8,9]
func_1(ls)