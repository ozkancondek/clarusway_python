# -*- coding: utf-8 -*-
"""
Created on Mon Aug  9 18:46:01 2021

@author: admin
"""
# Palindrome number check

num = int(input("Enter a number: "))
def palindrome(num):
    if  num == int(str(num)[::-1]):
        print ("correct")
    else: 
        print("not")     
    
       
            
palindrome(num)