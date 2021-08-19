# -*- coding: utf-8 -*-
"""
Created on Wed Aug 18 19:04:48 2021

@author: admin
"""
# https://www.codewars.com/kata/550f22f4d758534c1100025a
ls = ["NORTH", "SOUTH", "SOUTH", "EAST", "WEST",
      "NORTH", "WEST", "SOUTH", "SOUTH", "EAST", "WEST"]
x = len(ls)
vert = ["NORTH", "SOUTH"]
horz = ["EAST", "WEST"]
location = []
c = 0


while c < x:

    location = ls[:2]
    location.sort()
    if location == vert or location == horz:
        ls = ls[2:]
    elif len(ls) == 0:
        break
    else:

        ls.append(ls[0])
        ls.remove(ls[0])

    c += 1

    print("ls", ls)
