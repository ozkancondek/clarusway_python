# -*- coding: utf-8 -*-
"""
Created on Mon Sep 20 22:49:59 2021

@author: admin
"""

"""
The number 81 has a special property, a certain power of the sum of its digits is equal to 81 (nine squared). Eighty one (81), is the first number in having this property (not considering numbers of one digit). The next one, is 512. Let's see both cases with the details
8 + 1 = 9 and 92 = 81
512 = 5 + 1 + 2 = 8 and 83 = 512
We need to make a function, power_sumDigTerm(), that receives a number n and may output the n-th term of this sequence of numbers. The cases we presented above means that
power_sumDigTerm(1) == 81
power_sumDigTerm(2) == 512
"""


ls = [] 
n = 0
for x in range(10,10000):
    for i in str(x):
        n = n + int(i)
     
    for j in range(n):
        if n**j == x:
            ls.append(x)
    n = 0
        
def power_sumDigTerm(n):
    return ls[n]

print(power_sumDigTerm(3))
        
    
 
    
    
    


 