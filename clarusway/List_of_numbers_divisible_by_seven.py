# -*- coding: utf-8 -*-
"""
Created on Wed Jul 21 14:56:09 2021

@author: admin
"""
numbers = [18,21,14,84,65,35,10,20,28,42,24,91,5,7,54,69]

ls = []

for i in range(len(numbers)):
    if numbers[i] % 7 == 0:
        ls.append(numbers[i])
ls.sort()
print (f"List of numbers divisible by seven:\n{ls}\n and totaly {len(ls)} numbers ")

