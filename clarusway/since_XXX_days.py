# -*- coding: utf-8 -*-
"""
Created on Wed Aug 18 21:41:27 2021

@author: admin
"""

#since XXXXX days i am in life 

from  datetime import date
birth = date(1995,4,6)

death = date(2021,8,18)

a = date.toordinal(birth)
b = date.toordinal(death) 
print(b-a)


 

 