# -*- coding: utf-8 -*-
"""
Created on Mon Jul 26 19:27:14 2021

@author: admin
"""
#for_lopp: split with "-"
word = input("Give me a name")
count = 0
for i in word:
    count +=1
    if count < len(word):
        i = i + "-"
    print(i, end = "")
