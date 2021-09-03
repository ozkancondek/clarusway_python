# -*- coding: utf-8 -*-
"""
Created on Fri Sep  3 17:10:05 2021

@author: admin
"""

from matrix_list_function import matrix

n = 3
mtr = matrix(n)
ls = []

for j in range(n):
    ls.append(mtr[0][j])
for i in range(n):
    ls.append(mtr[i][n-1])
for x in range(n-1,-1,-1):
    ls.append(mtr[n-1][x])
for y in range(n-1,-1,-1):
    ls.append(mtr[y][0])

print(ls)


