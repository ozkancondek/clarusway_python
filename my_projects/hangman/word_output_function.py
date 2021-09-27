# -*- coding: utf-8 -*-
"""
Created on Thu Sep 16 01:24:35 2021

@author: admin
"""
 


def wor(word,ch):
    ls = list(word)
     
    c = 0
    while c < len(ls):
        if ls[c] != ch:
            ls[c] = "_"
        c += 1
    return "".join(ls)
 
 

     
    
    