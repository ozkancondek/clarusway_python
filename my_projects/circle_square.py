# -*- coding: utf-8 -*-
"""
Created on Thu Aug 12 17:35:12 2021

@author: admin
"""
#Imagine a circle and two squares: a smaller and a bigger one. For the smaller one, the circle is a circumcircle and for the bigger one, an incircle.
#Create a function, that takes an integer (radius of the circle) and returns the difference of the areas of the two squares.
radius = int(input("Give me the radius: "))
def area_square(radius):
    square_small = 2*(radius**2)
    square_big = 4*(radius**2)  
    difference = square_big - square_small
   
    print("Areas of the squares:\n Small square={}\n Big square={}\n Difference={} ".format(square_small,square_big,difference))
area_square(radius)