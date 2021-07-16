# -*- coding: utf-8 -*-
"""
Created on Thu Jul 15 20:24:44 2021

@author: admin
"""
left = {"q", "w", "e", "r", "t", "a", "s", "d", "f", "g", "z", "x", "c", "v", "b"}
right = {"y", "u", "i", "o", "p", "h", "j", "k", "l", "n", "m"}
word = input("Enter the word")
  # küme farki ile dene. Girilen kelmímenin her iki küme ile de farkini al-Difference or intersection
set_word = set(word)
 
x = bool( set_word.intersection(left))
y = bool(set_word.intersection(right))

z = x and y

if z == True:
    print(True)
else:
    print(False)




 
 
    