# -*- coding: utf-8 -*-
"""
Created on Tue Aug  3 22:49:14 2021

@author: admin
"""

a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
ls = []
k = []
l = len(a)
print ("Your list is below.Cconverted in  3X3 form: ")
for i in a:
    print(i)
 
a.reverse()
for x in range(l):
    for y in range(l):
        ls.append(a[y][x])
    k.append(ls)
    ls = []
print("The list is rotaded by 90 degrees: ")
for j in k:
    print(j)
 