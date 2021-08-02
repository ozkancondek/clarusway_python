# -*- coding: utf-8 -*-
"""
Created on Mon Aug  2 20:23:45 2021

@author: admin
"""
#https://edabit.com/challenge/Y5Ji2HDnQTX7MxeHt


length = int(input("Enter the side of the game screen: "))
area = length * length
def snake(length):
    for i in range(area):
        if area < 2**i:
            return print(i-1," times the snake can eat before it runs out of space.")
            break
snake(length)
        