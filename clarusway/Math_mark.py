# -*- coding: utf-8 -*-
"""
Created on Mon Jul 12 18:55:59 2021

@author: admin
"""
math_mark = int(input('Please enter the mark: '))
if math_mark >= 85 and math_mark <= 100:
    print("A (Excellent)")
elif math_mark >= 70 and math_mark <= 84:
    print("B (Good)")
elif math_mark >= 60 and math_mark <= 69:
    print("C (Medium)")
elif math_mark >= 45 and math_mark <= 59:
    print("D (Not Bad)")
elif math_mark >= 0 and math_mark <= 44:
    print("F (Failed)")
    
 