# -*- coding: utf-8 -*-
"""
Created on Tue Aug 17 13:58:18 2021

@author: admin
"""
#Given two lines, determine whether or not they are parallel.

#Lines are represented by a list [a, b, c], which corresponds to the line ax+by=c.


l_1 = [0,1,5]
l_2 = [0,1,5]
def parallel(l_1,l_2):
    if l_1[1] > 0:
        m_1 = -l_1[0]/l_1[1]
    else:
        m_1 = l_1[0]/l_1[1]   
    if l_2[1] > 0:
        m_2 = -l_2[0]/l_2[1]
    else:
        m_2 = l_2[0]/l_2[1]
    if m_1 == m_2:
        return True
    else:
        return False
print(parallel(l_1, l_2))
    
 
   
        