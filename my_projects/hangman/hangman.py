# -*- coding: utf-8 -*-
"""
Created on Mon Aug 30 23:25:35 2021

@author: admin
"""

 
from visual_dictionary import lives_visual_dict
from word_output_function import wor
 

word = "sena" # Pick a word at the beginning.
re = len(word)*"_ "
str_out = []
c = 1
 
print("Welcome to HANGMAN-GAME.\nYou need to enter a letter!\nNote:Dont type a letter twice.It will be counted as a mistake. ")
while c <= len(lives_visual_dict)+1:
     ch = input("Type a letter: ")
     
     if ch in word:
        print(f"Correct! {ch} is in word {word.count(ch)} times.")
        str_out = str_out + list(wor(word,ch))
        print(str_out)  # this line needs to correctness
        
            
         
        
         
        word = word.replace(ch,"",word.count(ch)) #delete the letters
         
        c -= 1
      
        if word == "":
            print("You win!!")
            break
     
         
     else:
         result = lives_visual_dict[len(lives_visual_dict)-c]
         print(result)
         
         if result == lives_visual_dict[0]:
              
             print("You losed!!!") 
             break
     c+=1
      
            
        
            
        
        