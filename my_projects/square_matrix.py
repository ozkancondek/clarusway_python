# -*- coding: utf-8 -*-
"""
Created on Thu Aug  5 21:58:46 2021

@author: admin
"""
#Create a function that takes an integer n and returns the identity matrix of n x n dimensions.
# For this challenge, if the integer is negative,
# return the mirror image of the identity matrix of n x n dimensions.
n = int(input("Give me n: "))
def  square_matrix(n):
    ls = []
    ml = []
    a = True
    if n < 0:
        a = not a
        n = -n

    for i in range(n):
        for j in range(n):
            ls.append(0)
        ml.append(ls)
        ml[i][i] = 1
        ls = [] 
    if a == True:
        for x in range(len(ml)):
            print(ml[x]) 
    else:
        ml.reverse()
        for x in range(len(ml)):
            print(ml[x]) 
square_matrix(n)    
     
    
        
     
    
    

