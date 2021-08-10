# -*- coding: utf-8 -*-
"""
Created on Mon Aug  9 19:36:10 2021

@author: admin
"""

dict_couple = {"bride" : ["mary", "bella", "linda", "emma"],
               "groom" : ["jack", "robert", "eric", "adam"]}

def match(bride,groom):
    match_list = []
    for i in zip(bride,groom): #its matches and makes tuples
        match_list.append(i)
    return match_list  
        
print(match(**dict_couple))

#-------------same function-----------

 
def match(bride,groom):   
     return[ i for i in zip(bride,groom)]
print(match(**dict_couple))

#---------kwargs---------
friends = {"Alfred":44, "Jonna":24, "Sarah": 49}

def meaner(Alfred,Jonna,Sarah):
    avg = (Alfred + Jonna + Sarah)/3
    print(f"The avarage of age is {avg}")
meaner(**friends)