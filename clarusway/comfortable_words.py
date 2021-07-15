# -*- coding: utf-8 -*-
"""
Created on Mon Jul 12 17:21:32 2021

@author: admin
"""

left = ["q", "w", "e", "r", "t", "a", "s"," d", "f"," g", "z"," x", "c", "v", "b"]
right = ["y", "u", "i", "o", "p", "h", "j", "k", "l", "n", "m"]
word = input("Enter a word.") #Take a word from the user
length = len(word)            
ls = []
letter = word[0]    #letter is index of my string
i = 0
 
while  i < length:  # I want to count all letters in string.
    letter = word[i]
    i += 1 
    

    if letter in right: #If letter in right list, add my list, ls, a 1.
        a=1
        ls.append(a)
    else:              #If letter in right list, add my list, ls, a 2.
        b=2
        ls.append(b)  #The ls list is consisting of only 1 and 2.
 #if elements of ls different from each other, 1 comes from right and 2 comes from left, 
 #my word gonna be comfortable.
 
print(ls)
for j in range(len(ls)-1): 
    
    t  = ls[j] + ls[j+1] #If sum of n. and (n+1). element equal to odd number or 3, thats mean elements are different.
    if t%2 == 1:
        print(True)
        break
    elif t%2 == 0:
        print(False)
        break
     
    j +=1
 