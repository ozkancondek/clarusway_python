# -*- coding: utf-8 -*-
"""
Created on Mon Aug  9 14:17:18 2021

@author: admin
"""
#Create a function that takes a number num and returns each place value in the number.
num = int(input("Enter a number"))


def splitter(num):
    if num < 0:
        num = num * -1
        ls = list(str(num))
        ls_1 = []
        for i in range(len(ls)):
            a = int(ls[i])*(10**((len(ls)-1)-i))
            ls_1.append(a)
        for j in range(len(ls_1)):
            ls_1[j] = ls_1[j]*-1

        return ls_1
    else:
        ls = list(str(num))
        ls_1 = []
        for i in range(len(ls)):
            a = int(ls[i])*(10**((len(ls)-1)-i))
            ls_1.append(a)
        return ls_1


print(splitter(num))
