# -*- coding: utf-8 -*-
"""
Created on Thu Jul 29 15:14:55 2021

@author: admin
"""
#anagram example
#Take two inputs from the user word and word-list.
#Than write code that will find all the anagrams of a word from a list.
# You should return a list of all the anagrams or an empty list if there are none. 
word = input("Give me a word. ")
ls = []
sl = []
for i in range(4):
    a = input(f"Give me {i+1}. word for list. ")
    ls.append(a)
print(f"Your list is:\n {ls}\nYour word is: {word}")
x = list(word)
x.sort()
 
for j in range(len(ls)):
    y= list(ls[j])
    y.sort()
     
    
    if x == y:
        sl.append(ls[j])
        
print("Your anagram list is below:\n ",sl)
        
    