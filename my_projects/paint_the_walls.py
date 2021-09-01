# -*- coding: utf-8 -*-
"""
Created on Wed Sep  1 15:27:25 2021

@author: admin
"""
 
# It takes 22 minutes for 10 people to paint 10 walls.
# How many minutes does it take 14 people to paint 14 walls?

rate = {
  "people": 10,
  "walls": 10,
  "minutes": 22
}

x = int(input("How many people? "))
y= int(input("How many wall? "))

def time (rate,x,y):
    return (rate["minutes"]*y)/x 
print(time(rate,x,y))
