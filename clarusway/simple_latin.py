# -*- coding: utf-8 -*-
"""
Created on Mon Aug 23 13:51:35 2021

@author: admin
"""
#Move the first letter of each word to the end of it, then add "ay" to the end of the word. Leave punctuation marks untouched.
import string
low_case = list(string.ascii_lowercase)
up_case = list(string.ascii_uppercase)
punct = list(string.punctuation)
sentence = "Hello world !"
c=list(sentence)
ls = []
sl = []
for i in c:
    if i in low_case or i in up_case:
        ls.append(i)
    else:
        sl.append(ls)
        ls = []
for j in sl:
    for x in j:
        j.append(j[0])
        j.append("ay")
        j.remove(j[0])
        break 
print(sl)
result = ""
for y in sl:
    for f in y:
        result = result + f
    result = result + " "
print(result)
for p in sentence:
    if p in punct:
        result = result[:len(result)-2]
        result = result+p
print(result)
 
        