# -*- coding: utf-8 -*-
"""
Created on Tue Aug 10 12:43:15 2021

@author: admin
"""

 

n = int(input("Enterfirst n column: "))


def pascal(n):
    ls_1=[1]
    ls_2 = [1,1]
    ls=[]

    sp = " "
    print((n-1)*sp,ls_1)
    print((n-2)*sp,ls_2)
    for j in range(n-2):
        for i in range(len(ls_2)-1):
            a = ls_2[i] + ls_2[i+1]
            ls.append(a) 
        ls.insert(0,1)     
        ls.append(1)
        ls_2 = ls
        ls = []
        print(sp*((n-3)-i),ls_2)
pascal(n)
       
 
    
     