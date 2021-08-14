# -*- coding: utf-8 -*-
"""
Created on Wed Aug 11 16:06:19 2021

@author: admin
"""
#Question link:
#https://edabit.com/challenge/SHdu4GwBQehhDm4xT
ls = [1, 1, 0, 0, 0, 1, 0]
def freed_prisoner(ls):
    count = 0
    
    if ls[0] == 0:
        return 0
    else:
        for x in range(len(ls)):
                if ls[x] == 1:
                    ls[x]=0
                else:
                    ls[x]=1
        
        for j in range (len(ls)):
            for i in range(len(ls)):
                if ls[i] == 1:
                    ls[i]=0
                    
                else:
                    ls[i]=1  
            
            for y in range(len(ls)):
                if ls[y] == 1:
                    count += 1
                    ls = ls[y:]
                    break
            if sum(ls) == 0:
                break 
        return count  
print(freed_prisoner(ls))
       