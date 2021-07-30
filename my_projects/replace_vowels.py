# -*- coding: utf-8 -*-
"""
Created on Fri Jul 30 00:28:10 2021

@author: admin
"""
#Create a function that replaces all the vowels in a string with a specified character.
ls =["a","e","i","o","u"]
word = input("Give me a word. ")
character = input("Give me a character to replace vowels. ")
def func(word,character):
    
    for i in range(len(word)):
    
        for j in range(len(ls)):
            if word[i] == ls[j]:
                word = word.replace(word[i],character)
    return word
print(func(word,character)) 
 