# -*- coding: utf-8 -*-
"""
Created on Tue Aug 17 13:58:18 2021

@author: admin
"""
#Roots of a quadratic equation

def root_finder(a,b,c):
     delta = b**2-4*a*c
      
      
     if delta < 0:
         return "no root"
    
         
     else:
         x_1 = (-1*b+(delta**0.5))/(2*a)
         x_2 = (-1*b-(delta**0.5))/(2*a)
         
         if x_1 == x_2:
             return x_1
         else:
             return [round(x_1),round(x_2)]
     
    

print(root_finder(1,-12,28))
    