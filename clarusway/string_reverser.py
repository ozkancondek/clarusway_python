# -*- coding: utf-8 -*-
"""
Created on Thu Aug 19 19:01:51 2021

@author: admin
"""
#string reverser  ozkan = nzkao
def front_back(word):
    ls = list(word)
    a = ls[0]
    ls[0] = ls[len(ls)-1]
    ls[len(ls)-1] = a
    result =""
    for i in ls:
        result = result + i
    return result

print(front_back("ozkan"))
    
     
    