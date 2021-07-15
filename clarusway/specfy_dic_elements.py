# -*- coding: utf-8 -*-
"""
Created on Thu Jul  8 19:05:21 2021

@author: admin
"""
item_number = int(input("how many items you need?"))
dic_1={}
for i in range( 0, item_number, +1):
    print("For ",(i+1),". element:")
    key = input("Enter the key") 
    value = input ("Enter the   value")
    dic_1[key]=value
print("Your new dictionary is:")
print(dic_1.items())   
    

