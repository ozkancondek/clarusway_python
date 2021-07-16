# -*- coding: utf-8 -*-
"""
Created on Fri Jul 16 17:08:52 2021

@author: admin
"""
 
leng = int(input("How many element dou you need for list. "))
ls = []
for i in range(leng):
    el = int(input(f"Give me {i+1}. element. "))
    ls.append(el)
    i +=1

print(f"Your current list is:\n {ls} ")

def accumulate (ls ):
    for i in range(len(ls)-1):
        ls[i+1] = int(ls[i]) + int(ls[i+1])
        i +=1
    return ls 
print(f"Accumulated list is: \n {accumulate(ls )}")