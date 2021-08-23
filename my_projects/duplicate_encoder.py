# -*- coding: utf-8 -*-
"""
Created on Mon Aug 23 13:51:35 2021

@author: admin
"""

#The goal of this exercise is to convert a string to a new string
# where each character in the new string is
# "(" if that character appears only once in the original string, or ")"
# if that character appears more than once in the original string. 
#Ignore capitalization when determining if a character is a duplicate.
    
    
word = "success"
wordp = word

 

for i in word:
    c = word.count(i)
    if c >= 2:
       wordp =  wordp.replace(i,")",1) 
    else:
       wordp =  wordp.replace(i,"(",1) 
print(wordp)
        
   
    