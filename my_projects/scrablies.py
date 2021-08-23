# -*- coding: utf-8 -*-
"""
Created on Mon Aug 23 13:51:35 2021

@author: admin
"""

#Complete the function scramble(str1, str2) that returns true
# if a portion of str1 characters can be rearranged to match str2, 
#otherwise returns false.

a = 'rkqodl'
b = 'world'
def scramble(a,b):
    for i in b:
        if i not in a:
            c = False
            break
        else:
            c = True
    return c
print(scramble(a,b))