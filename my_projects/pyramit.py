# -*- coding: utf-8 -*-
"""
Created on Thu Jul 29 20:26:56 2021

@author: admin
"""
#draw a pyramit with entered variables.
#get building material from the user
#get base width for pyramid
#base width has to be odd number otherwise send user a massage that it has to be odd number.

a = input("Choose the building material: ")
b = " "
num =int(input("Base width of the pyramid: "))
while num%2 == 0:
    print("You have to chose odd number.")
    num =int(input("Base width of the pyramid."))

for i in range(1,num+1,2):
    print(int((num-i)/2)*b,(i*a))  
 
