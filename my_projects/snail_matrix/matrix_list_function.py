# -*- coding: utf-8 -*-
 

"""
matrix function create a nxn matrix list
"""

def matrix(n):
    end_list = []
    matrix_list = []
    a = 0
    for i in range(1,n+1):
        for j in range(1,n+1):
            a += 1
            matrix_list.append(a)
        end_list.append(matrix_list)
        matrix_list = [] 
    
    return end_list
 