# -*- coding: utf-8 -*-
"""
Created on Sat Sep 11 17:01:51 2021

@author: admin
"""
#https://edabit.com/challenge/jfpfpH6w42tZeRo2T
count = int(input("How many points you want to enter? "))
ls = []
while True:
    point = int(input("Enter the movement: "))
    ls.append(point)
    if len(ls) == count:
        break
   
print(f"Your point list is below:\n{ls}\nAnd your end position is: ")


def position(ls):
    ls1 = []
    ls2 = []
    
    for i in range(len(ls)):
        if i%2 == 0:
            ls2.append(ls[i])
        else:
            ls1.append(ls[i])
    for j in range(len(ls1)):
        if j % 2 != 0:
            ls1[j] = -ls1[j]
    for y in range(len(ls2)):
        if y%2 != 0:
            ls2[y] = -ls2[y]
    return   [sum(ls1) , sum(ls2)]

print(position(ls))
    
            
 
            
        
            
            
            
        
        