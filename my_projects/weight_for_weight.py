# -*- coding: utf-8 -*-
"""
Created on Mon Aug 23 15:32:21 2021

@author: admin
"""
#https://www.codewars.com/kata/weight-for-weight/python
old_list = [56, 65, 74, 100, 99, 68, 86, 180, 90]
b = 0
dictw = {}
k = []
for i in old_list:
    a = str(i)
    for j in a:
         
        b = b + int(j)
    dictw[a]=b
    b = 0
ls = list(dictw.values())
ls.sort()
print(ls)
print(dictw)
#for key, value in dictw.items():
     #if value == ls[2]:
        # print(key)
        # break
for x in ls:
    if x in dictw.values():
        print(x)
        for key, value in dictw.items():
            if value == x:
                k.append(key)
                dictw.pop(key)
                break
         
print(k)         
             
            
            
