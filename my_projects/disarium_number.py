# -*- coding: utf-8 -*-
"""
Created on Sun Jul 25 23:37:51 2021

@author: admin
"""
#A number is said to be Disarium if the sum of its digits
# raised to their respective positions is the number itself.
num = int(input("Enter the number: "))
order =str(num)


def disarium(num):
    result = 0
    
    for i in range(len(order)):
        result = result + int(order[i])**(i+1)
    if result == num:
        print(f"{num} is disarium number.")
    else:
        print(f"{num} is not disarium number")
disarium(num)
        
        
    