# -*- coding: utf-8 -*-
"""
Created on Thu Aug 12 21:38:26 2021

@author: admin
"""
#return the current position of robot
C= ["right 20","right 30 ", "left 50","down 20"]
x = y = 0

for i in range(len(C)) :
    if C[i].startswith("r") : x = x + int(C[i].split()[1]) #a = c.split() = ['ozkan', '20']
    elif C[i].startswith("l") : x = x - int(C[i].split()[1])
    elif C[i].startswith("u") : y = y + int(C[i].split()[1])
    elif C[i].startswith("d") : y = y - int(C[i].split()[1])
        
print([x, y])