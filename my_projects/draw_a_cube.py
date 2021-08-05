# -*- coding: utf-8 -*-
"""
Created on Thu Aug  5 15:18:34 2021

@author: admin
"""
#Get element of the cube and line length from the user and print out a cube.
el = input("Give me the element of the cube: ")
line = int(input("What is the length of the line: "))
for i in range(line):
    print(line*(el+(" ")))
        