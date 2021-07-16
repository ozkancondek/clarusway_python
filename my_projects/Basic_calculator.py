# -*- coding: utf-8 -*-
"""
Created on Thu Jul 15 21:27:44 2021

@author: admin
"""

x = float(input("Enter the first number :"))
op =  input("Enter the operator :")
y = float(input("Enter the second number :"))

def calculator(x, op, y):
    if y == 0 and op == "/":
        return "Cant divide by 0!"
    elif op == "*":
        return x*y
    elif op == "/":
        return x/y
    elif op == "-":
        return x-y
    elif op == "+":
        return x+y
    else:
        return "Wrong operator!!"

print(calculator(x, op, y))