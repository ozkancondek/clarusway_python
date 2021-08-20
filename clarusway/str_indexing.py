# -*- coding: utf-8 -*-
"""
Created on Thu Aug 19 19:01:51 2021

@author: admin
"""
#Given a non-empty string and an int n, 
#return a new string where the character at index n has been removed. 
#The value of n will be a valid index of a character in the original string
# (i.e. n will be in the range 0....len(str)-1 inclusive).
def missing_char(word, n): 
    ls = list(word)
    ls.pop(n)
    result = ""
    for i in ls:
        result = result + i
    return result
print(missing_char('kitchen', 0))

        