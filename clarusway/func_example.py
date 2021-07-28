# -*- coding: utf-8 -*-
"""
Created on Mon Jul 26 18:37:31 2021

@author: admin
"""
def func(x, y):  #  args
    print(x, "Its from Generation X")
    print(y, "Its from Generation Y")
 
dict_1 = {'y' : "Marry", 'x' : "Fred"}
func(**dict_1)  # we call the function by a single argument(variable)

def func_1(x='Solomon', y='David'):  # defined by kwargs (default values assigned to x and y)
    print(x, "belongs to Generation X")
    print(y, "belongs to Generation Y")
 
dict_2 = {'y' : "Marry", 'x' : "Fred"}
func_1(**dict_2)  