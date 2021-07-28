# -*- coding: utf-8 -*-
"""
Created on Mon Jul 26 18:37:31 2021

@author: admin
"""
def brothers(bro1, bro2, bro3):
    print('Here are the names of brothers :')
    print(bro1, bro2, bro3, sep='\n')

family = ['tom', 'sue', 'tim']
brothers(*family)