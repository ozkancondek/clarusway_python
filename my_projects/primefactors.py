# -*- coding: utf-8 -*-
"""
Created on Mon Aug  9 13:30:57 2021

@author: admin
"""
# Prime ones in factor list
num = int(input("Enter a number: "))

def prime_factors(num):
    ls = []
    prime_fac = []
    ls = [i for i in range(2,num+1) if num % i == 0]
    print(f"List of factors are below.\n{ls}")

    for x in ls:
        if x == 2:
            prime_fac.append(x)
        else:
            for j in range(2,x):
                    if (x % j) == 0:
                        break  
                     
                   
            else:
                prime_fac.append(x)
    print("And the prime ones in factors list are below.")                
    return prime_fac            
print(prime_factors(num))