# -*- coding: utf-8 -*-
"""
Created on Tue Aug 17 13:58:19 2021

@author: admin
"""
#Create a shape in co-ordinate system with elemnts of ls
#What is  area of the smallest rectangele that can contain the shape

ls = [[-4,-6],[-5,8],[3,6],[6,-5]]
x =[]
y = []

for i in range(4):
    for j in range(2):
        x.append(ls[i][0])
        y.append(ls[i][1])
        break
x.sort()
y.sort()
m = max(x)
mm = min(x)
n = max(y)
nn = min(y)
if m<0 : 
    m = -m
if mm < 0:
    mm = -mm
if nn < 0 :
    nn = -nn
if n< 0:
    n = -n
area = (m+mm)*(n+nn)
print(area)
        
        
