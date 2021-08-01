# -*- coding: utf-8 -*-
"""
Created on Thu Jul 29 15:08:10 2021

@author: admin
"""
#filter(function, sequence)
first_ten = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] 
#tests each element in the sequence to be true or not.
even = filter(lambda x:x%2==0, first_ten) 
odds = filter(lambda y:y%2!=0, first_ten)
print(type(even))  # it's 'filter' type, 
                   # in order to print the result,
                   # we'd better convert it into the list type

print('Even numbers are :', list(even))
print('Odd numbers are :', list(odds))   