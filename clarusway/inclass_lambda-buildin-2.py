# -*- coding: utf-8 -*-
"""
Created on Wed Aug 18 19:04:54 2021

@author: admin
"""

def equal(a,b,c):
    numbers = [a,b,c]
    
    res = numbers.count(max(numbers, key = numbers.count))
    if res > 1:
        return res
    else:
        return 0
    
print(equal(1, 22, 22))

def equal(*a):
    numbers = list(a)
    
    res = numbers.count(max(numbers, key = numbers.count))
    if res > 1:
        return res
    else:
        return 0
    #return  numbers.count(max(numbers, key = numbers.count)) if numbers.count(max(numbers, key = numbers.count)) >1 else 0
    
print(equal(1, 22, 22,2,5,8,7,8,8,8,8,8,6)) 
#----------------------------------

equal_lambda = lambda a, b, c : [a, b, c].count(max([a, b, c], key = [a, b, b].count)) \
if  [a, b, c].count(max([a, b, c], key = [a, b, b].count)) > 1 else 0
#----------------------
equal_lambda = lambda *a: list(a).count(max(list(a), key = list(a).count)) \
if  list(a).count(max(list(a), key = list(a).count)) > 1 else 0
