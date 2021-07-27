# -*- coding: utf-8 -*-
"""
Created on Mon Jul 26 20:18:41 2021

@author: admin
"""
#Algorithm Logic: Shift the consisting shape down one unit each time 
#and calculate the empty cells in between.
input("Welcome to Trapping Rain Water example.Please press enter to continue")
input("Each element on list is considered a cube placed on top of each other.")
input("Zero is considered free space.")
input("For example, if you type elements of the list like 2-0-1, there will be a 1-unit space between here.")
input("Now you have to determine a list.")

n = int(input("Enter the number of elements first: "))
pro = []
for y in range(n):
    element = int(input("Enter the {}. element: ".format(y + 1)))
    pro.append(element)
print("Your list is below:\n{}".format(pro))
# In the code above get list length and elements from user----------------
for i in range(len(pro)):
    if pro[i] != 0:
       break  
        
pro.reverse()       
for j in range(len(pro)): # I count first of all the list from the begining 
    if pro[j] != 0: 
       break  
   
pro.reverse()  #Than i count again from the end
d = pro[i:(len(pro)-j)] # And i make a new limited list

q = d.count(0) #Each 0 between non-zero elements is one-unit-space

result = 0
# The code above shows the limited list and counts each 0.----------------
for i in range(len(pro)): #Here i want to reduce  each elements of pro, until they reach 0.
    if pro[i] > 0 :
        for j in range(len(pro)):
            if pro[j] > 0:
                pro[j] = pro[j] -1
        
#Until here, each elements will be reduced
        for i in range(len(pro)):#Than i start again count to numbers of 0.
            if pro[i] != 0:
                break  
        
        pro.reverse()       
        for j in range(len(pro)):
            if pro[j] != 0:
                break  
       
        pro.reverse() 
        d = pro[i:(len(pro)-j)]
        s = d.count(0)
        result = s + result
        
        
print("Trapped water:{}".format(result+q))
