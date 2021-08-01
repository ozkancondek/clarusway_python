# -*- coding: utf-8 -*-
"""
Created on Thu Jul 29 15:14:54 2021

@author: admin
"""
#Lambda in user defined func
def modular_function(n):
    return lambda x: x ** n
    
power_of_2 = modular_function(2)  # first sub-function derived from def
power_of_3 = modular_function(3)  # second sub-function derived from def
power_of_4 = modular_function(4)  # third sub-function derived from def

print("Square of 2 is equal to {}.".format(power_of_2(2)))  # 2 to the power of 2
print(power_of_3(2))  # 2 to the power of 3
print(power_of_4(2))  # 2 to the power of 4