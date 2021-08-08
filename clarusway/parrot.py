# -*- coding: utf-8 -*-
"""
Created on Sat Aug  7 17:56:57 2021

@author: admin
"""

def parrot_trouble(talking, hour):
     if talking == True and hour <= 6  :
         return True
     elif  talking == True and hour >= 21:
         return True 
     else:
         return False
print(parrot_trouble(False, 22))