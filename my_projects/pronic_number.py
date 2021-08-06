# -*- coding: utf-8 -*-
"""
Created on Thu Aug  5 21:58:46 2021

@author: admin
"""
num = int(input("Enter number: ")) 
def pronic(num):
    a = False
    for i in range(num):
        if i*(i+1) == num:
            a = not a
            print(a)
            break
    if a == False:
        print(a)
         
pronic(num)