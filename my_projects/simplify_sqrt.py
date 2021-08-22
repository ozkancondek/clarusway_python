# -*- coding: utf-8 -*-
"""
Created on Sun Aug 22 17:23:50 2021

@author: admin
"""

#https://edabit.com/challenge/XPCqS7GYYouXg5ut9
n = 72#int(input("Enter a number: "))
def simplify_sqrt(n):  
    ls = [i**2 for i in range(n)]
    for j in range(n-1,1,-1):
        if n%j == 0 and j in ls:
             
            return (int(j**(1/2)),int(n/j))  
            break
        elif n in ls:
            return (int(n**0.5),1)
            break
    else:
        return (1,n)
         
print(simplify_sqrt(n))
 
    
        