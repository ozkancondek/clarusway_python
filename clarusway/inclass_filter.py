# -*- coding: utf-8 -*-
"""
Created on Thu Aug 12 21:07:41 2021

@author: admin
"""

#filter
#filter(function,sequence) if sequence True it returns
num1 = [1,2,3,4]

even = filter(lambda x: x%2==0,num1)
print(list(even))

#------------
words = ["ozkan", "condek","aa","bbb"]
print(list( filter (lambda x: len(x)<5,words)))     
#------------
first_ten = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
vowels = ["a","e","i","u","o"]
print(list(filter(lambda x:x in vowels,first_ten)))