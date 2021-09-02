# -*- coding: utf-8 -*-
"""
Created on Thu Sep  2 19:38:10 2021

@author: admin
"""
#https://edabit.com/challenge/2C3gtb4treAFyWJMg
from string import ascii_uppercase

ls= list(ascii_uppercase)
ls.remove("J")
ls[ls.index("I")] = "I/J"
 
letter_dic = {}

for i in range(1,6):
    for j in range(1,6):
        letter_dic[int(str(i)+str(j))] =ls[0]
        ls.remove(ls[0])
        
#print(letter_dic)
r_dict = {}
user_input = "22 22 22" 

key1 = []
key = ""
user_output = ""
key_list = list(str(user_input))
if type(user_input) == int:
    for x in key_list:
        key = key + x
        if len(key) == 2:
            key1.append(int(key))
            key = ""
        
    for m in  key1:
        if letter_dic[m] == "I/J":
            letter_dic[m] = "I"
        elif m == " ":
            user_output = user_output + " "
        else:
            user_output = user_output + letter_dic[m]
    print(user_output)
     
else:
    user_input = user_input.upper()
    k = list(letter_dic.keys())
    v = list(letter_dic.values())
    ind = v.index("I/J")
    v[ind] = "I"
    for y in range(len(k)):
        r_dict[v[y]]=k[y]
    lss = list(user_input)
    for n in lss:
        if n == " ":
            user_output = user_output + " "
        else:
            user_output = user_output + str(r_dict[n])
    print(user_output)
        
    
        
        
        
            
        
        
        
 
    


         
 