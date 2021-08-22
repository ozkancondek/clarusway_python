# -*- coding: utf-8 -*-
"""
Created on Sun Aug 22 17:23:50 2021

@author: admin
"""

#  https://edabit.com/challenge/hY6BMxxEYycT83GPs

num = "9572"#input("Enter a number")

def  multi_11(num):
    result = ""
    ls = [num[0]]
    for i in range(len(num)-1):
        
        result = result + str(int(num[i]) + int(num[i+1]))
        ls.append(result)
        result = ""
    ls.append(num[-1:])

    c = 0
    while c< len(ls):
        if len(ls[c]) == 2:
            ls[c]=ls[c][1]
            ls[c-1] = str(int(ls[c-1])+1)
            c = 0
     
        c+=1
    if len(ls[0]) == 2:
        ls[0]=ls[0][1]
        ls.insert(0,"1")
    numr=""
    for j in ls:
        numr = numr + j
        

    
    return numr  
    
     
     
print(multi_11(num)) 