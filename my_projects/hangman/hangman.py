# -*- coding: utf-8 -*-
"""
Created on Mon Aug 30 23:25:35 2021

@author: admin
"""

 
from visual_dictionary import lives_visual_dict
 

word = "ozkan"

def hangman():
    for i in range(len(lives_visual_dict)):
        ch = input("Give me a letter: ")
        if ch in word:
            print("Correct go on")
            ch = input("Give me a letter: ")
        else:
            print(lives_visual_dict[len(lives_visual_dict)-i])
print(hangman())
            
            