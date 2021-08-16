# -*- coding: utf-8 -*-
"""
Created on Mon Aug 16 12:13:55 2021

@author: admin
"""
#https://edabit.com/challenge/76pRYoqrmEQQtFAME
num = int(input("Enter the positive integer bigger than 9: "))
def astonishing(num):
    a = str(num)
    result_A = 0
    result_B = 0
    
    for i in range(1,len(str(num))):
        if int(a[:i]) < int(a[i:]):
            for j in range(int(a[:i]),int(a[i:])+1):
                result_A = result_A + j
            if result_A == num:
                break
        else:
            for j in range(int(a[i:]),int(a[:i])+1):
                result_B = result_B + j
            if result_B == num:
                break       
                                   
        
             
             
    if result_A == num:
                print("AB-Astonishing")
    elif result_B == num:
                print("BA-Astonishing")
    else:
        print(False)
astonishing(num)