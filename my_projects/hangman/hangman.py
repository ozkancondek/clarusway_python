# -*- coding: utf-8 -*-
"""
Created on Mon Aug 30 23:25:35 2021

@author: admin
"""

 
from visual_dictionary import lives_visual_dict
 

word = "ozkan"
ls = []

for i in range(1,len(lives_visual_dict)+1):
     ch = input("Give me a letter: ")
     ls.append(ch)
     if ch in word:
        print("Correct go on")
        word.replace(ch,"") #delete the letter
        if word in "".join(ls):
            print("win")
            break
        else:
        
            ch = input("Give me a letter: ")
     else:
         result = lives_visual_dict[len(lives_visual_dict)-i]
         if result == lives_visual_dict[0]:
             print(lives_visual_dict[0])
             print("you losed") 
             break
 
            
            