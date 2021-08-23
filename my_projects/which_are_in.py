# -*- coding: utf-8 -*-
"""
Created on Mon Aug 23 15:32:21 2021

@author: admin
"""
#https://www.codewars.com/kata/550554fd08b86f84fe000a58
a1 = ["tarp", "mice", "bull"]
a2 = ["lively", "alive", "harp", "sharp", "armstrong"]
k =[]
for i in a2:
    for j in a1:
        if j in i:
           k.append(j)
           break
     
c = 0   
while True:
    if k == []:
        break 
    elif k.count(k[c])>1:
        k.remove(k[c])
    else:
        break
    c += 1
print(k)
        