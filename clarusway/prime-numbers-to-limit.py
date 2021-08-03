# -*- coding: utf-8 -*-
"""
Created on Mon Aug  2 18:03:56 2021

@author: admin
"""

print("This program will give you a list of prime numbers from 1 to entered limit.")
num =int(input("Enter a limit: "))
ls = []
for j in range (2,num+1):
   for i in range(2,j):
      if (j % i) == 0:
         break
   else:
      ls.append(j) 
print(ls)          
            

   