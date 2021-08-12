# -*- coding: utf-8 -*-
"""
Created on Thu Aug 12 17:35:13 2021

@author: admin
"""
#Write a function that takes coordinates of two points on a two-dimensional plane 
#and returns the length of the line segment connecting those two points.
x_1 = int(input("Enter the x1: "))
y_1 = int(input("Enter the y1: "))
x_2 = int(input("Enter the x2: "))
y_2 = int(input("Enter the x2: "))

ls = [[x_1,y_1],[x_2,y_2]]

def length_line(ls):
    line = ((x_2 - x_1)**2 +(y_2-y_1)**2)**(1/2)
    return f"{line:.2f}"

print(length_line(ls))    
    