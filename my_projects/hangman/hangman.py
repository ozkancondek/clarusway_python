# -*- coding: utf-8 -*-
"""
Created on Mon Aug 30 23:25:35 2021

@author: admin
"""

from visual_dictionary import lives_visual_dict
 
 

word = "ozkancondeka" # Pick a word at the beginning.
re = len(word)*"_ "
str_out = []
ls = []
ls2=list("-"*len(word))
c = 1
 
print("Welcome to HANGMAN-GAME.\nYou need to enter a letter! ")
while c <= len(lives_visual_dict)+1:
     ch = input("Type a letter: ")
     
     if ch in word:
        print(f"Correct! {ch} is in word {word.count(ch)} times.")
        for x in word:
            if x == ch:
                ls.append(ch)
            else:
                ls.append("-")
        str_out.append(ls)
        ls = []
          
        for i in range(len(str_out[0])):
            for j in range(len(str_out)):
                if str_out[j][i] != "-":
                    ls2[i]=str_out[j][i]
             
    
        print("".join(ls2))
            
         
        
         
       # word = word.replace(ch,"",word.count(ch))  
         
        c -= 1
      
        if "".join(ls2) == word:
            print("You win!!")
            break
     
         
     else:
         result = lives_visual_dict[len(lives_visual_dict)-c]
         print(f"{ch} not in word. You have {len(lives_visual_dict)-c} more wrong right.")
         print("".join(ls2))
         print(result)
         
         if result == lives_visual_dict[0]:
              
             print("You losed!!!") 
             break
     c+=1
      
            
        
            
        
        