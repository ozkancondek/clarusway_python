# -*- coding: utf-8 -*-
"""
Created on Thu Aug 19 19:01:50 2021

@author: admin
"""
#Count the number of each letter in a sentence.
s = input("Give me a sentence: ")
d = {}
for i in s:
      d[i]=s.count(i)
print(d)