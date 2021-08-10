# -*- coding: utf-8 -*-
"""
Created on Tue Aug 10 12:58:34 2021

@author: admin
""" 
num =int(input("Enter a number: "))
def prime_factors(num):

    ls = []
    result = 0
    for i in range(2,num): # First division with prime: 20 = 2*10
        if num%i == 0:
            result = num /i
            ls.append(i)
            ls.append(int(result))
            break #break after to find 10
    else:
        ls.append(i)
 
    for j in ls: #then division process contunie with 10:2*2*5
        for x in range(2,j):
            if j%x == 0:
                result = j/x
                ls.remove(j) #remove 10
                ls.append(x) # append 2
                ls.append(int(result))# append 5
                break
     
    return ls
print(prime_factors(num))
        
     
        
        
 
 
 
    