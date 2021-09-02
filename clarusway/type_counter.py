# -*- coding: utf-8 -*-
"""
Created on Thu Sep  2 19:09:25 2021

@author: admin
"""
# Type counter
data = ["a", "b", True, (False, 1), {"1" : 2}, [1,2], {"2" : "two"}, {2, "3"}, "c", 23, 0]

types = ["int","str","bool","list","tuple","dict","set"] 
summ = {}.fromkeys(types,0)   # list to dict directly
 

for i in range(len(data)):
    if type(data[i]) == int: summ["int"] += 1
    elif type(data[i]) == str: summ["str"] += 1
    elif type(data[i]) == bool: summ["bool"] += 1
    elif type(data[i]) == list: summ["list"] += 1
    elif type(data[i]) == tuple: summ["tuple"] += 1
    elif type(data[i]) == dict: summ["dict"] += 1
    elif type(data[i]) == set: summ["set"] += 1
    
print(summ)

