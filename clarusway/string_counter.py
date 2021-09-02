# -*- coding: utf-8 -*-
"""
Created on Thu Sep  2 19:09:25 2021

@author: admin
"""
#Count the strings

string = "What a lovely day!"

dict_word = {}
for n in string:
    keys = dict_word.keys()
    if n in dict_word:
        dict_word[n] +=1
    else:
        dict_word[n] = 1
        
print(dict_word)


#-----------------------
a = input("Please write a sentence: ")
print({i: a.count(i) for i in a})
    