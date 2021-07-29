# -*- coding: utf-8 -*-
"""
Created on Thu Jul 29 15:59:29 2021

@author: admin
"""

#if body - if - condition - else - else body
condition = False

print("ozkan" if condition else "OZKAN")

 
#newlist = [expression for item in iterable if condition == True]

ls = [1,2,3,4,5,6,7,8,9,10]
a = [i**2 for i in ls if i%2]#all ods and their squares 
a = [i**2 for i in ls if i%2==0]#all evens and their squares
#numbers until 5
a =[i for i in range(11) if i<5]

#make a list
ls = []
for i in range(10):
    ls += [i]
 
#or----------
a = [i for i in range(10)]
 
#or
lt = list(range(10))
 
#-----------------------------
x = [j for j in range(10) if j % 2 ==0] # even numbers till 10
#-----------------------------
 