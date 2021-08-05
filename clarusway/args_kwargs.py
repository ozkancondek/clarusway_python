# -*- coding: utf-8 -*-
"""
Created on Wed Jul 28 23:36:13 2021

@author: admin
"""
def func(x, y):  #  args
    print(x, "Its from Generation X")
    print(y, "Its from Generation Y")
 
dict_1 = {'y' : "Marry", 'x' : "Fred"}
func(**dict_1)   

def func_1(x='Solomon', y='David'):  #  kwargs 
    print(x, "belongs to Generation X")
    print(y, "belongs to Generation Y")
 
dict_2 = {'y' : "Marry", 'x' : "Fred"}
func_1(**dict_2) 
     

#---------------------------------------
def animals(**kwargs):
    for  key, value in kwargs.items():
        print(value, "are", key)
               
animals(carnivores="Lions", Omnivores="Bears", Herbivores="deers", nomnivores="Human")
#------------------------------------------
def organizer(**people):
    name =[]  #print(list(kwargs.keys())
    age = []  #print(list(kwargs.values())
    for  key, value in people.items():
         name.append(key)
         age.append(value)
    print(name) 
    print(age)
               
organizer(a=1,b=2,c=3)
#--------------------------------------------

 