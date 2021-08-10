# -*- coding: utf-8 -*-
"""
Created on Mon Aug  9 22:19:05 2021

@author: admin
"""
word = "(){[]})"
def isValid(word):
    while "()" in word or "[]" in word or "{}" in word:
        word = word. replace("()",""). replace("[]",""). replace("{}" ,"")
        return word == ""
print(isValid( word))