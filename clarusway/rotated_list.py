# -*- coding: utf-8 -*-
"""
Created on Tue Aug  3 22:49:14 2021

@author: admin
"""
k = [[1,2],[3,1]]
result = 0
for i in range(len(k)):
    for j in range(len(k)):
         
        if k[i][j]%2 == 0:
            result = result + k[i][j]
print(result)






#even =filter(lambda y : y % 2 == 0, k)
#print(list(even))