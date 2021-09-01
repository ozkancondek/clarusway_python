# -*- coding: utf-8 -*-
"""
Created on Wed Sep  1 15:27:28 2021

@author: admin
"""
#https://edabit.com/challenge/5bYXQfpyoithnQisa



from chars import char_to_dots


word = input("Enter a sentence: ").upper()
 

def encode_morse(word):
    ls = []
    for i in word:
        ls.append(char_to_dots[i])
    return " ".join(ls) 
    
    
print(encode_morse(word))
        
         
    