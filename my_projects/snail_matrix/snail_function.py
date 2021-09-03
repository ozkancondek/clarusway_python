# -*- coding: utf-8 -*-
"""
Created on Fri Sep  3 17:10:05 2021

@author: admin
"""

from matrix_list_function import matrix
from simplifier import simplifier
 
def snail(n):

    mtr = matrix(n)
    ls = []
    for I in range(n//2):
        for j in range(len(mtr)):
            ls.append(mtr[0][j])
        for i in range(len(mtr)):
            ls.append(mtr[i][len(mtr)-1])
        for x in range(len(mtr)-1,-1,-1):
            ls.append(mtr[len(mtr)-1][x])
        for y in range(len(mtr)-1,-1,-1):
            ls.append(mtr[y][0])
         
        for m in mtr:
            
                m.remove(m[len(m)-1])
            
        for q in mtr:
            
                q.remove(q[0])
            
        mtr.remove(mtr[0])
        
        mtr.remove(mtr[len(mtr)-1]) 
         
    if n%2 != 0:
        ls.append(mtr[0][0])
    return simplifier(ls)

 
    
 


