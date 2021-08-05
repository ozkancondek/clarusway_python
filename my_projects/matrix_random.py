# -*- coding: utf-8 -*-
"""
Created on Thu Aug  5 15:21:11 2021

@author: admin
"""
import random
 
l = int(input("What is the length of the matrix: "))
def even_in_matrix(l):
    """This function will calculate the sum of all even numbers in matris.
    The user just defines a length of matrix and program will create automatically
    a matrix """
    ls = []
    k =[]
    
    for j in range(l):
        for i in range(l):
            a = random.randint(0,9)
            ls.append(a)
        k.append(ls)
        ls = []
    print(f"Here is your {l}X{l} matrix: ")
    for x in k:
        print (x)
     
    result = 0
    for m in range(len(k)):
        for n in range(len(k)):
             
            if k[m][n]%2 == 0:
                result = result + k[m][n]
    print(f"Sum of even numbers in matrix is equal to {result}.")
even_in_matrix(l)