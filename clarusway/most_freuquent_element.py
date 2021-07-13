# -*- coding: utf-8 -*-
"""
Created on Wed Jul  7 17:43:31 2021

@author: admin
"""

#a=[1,2,3,4,5,6,2,5,1,5,4,9,5,1]
#print(max(a, key=a.count))
numbers = [1, 3, 7, 4, 3, 0, 3, 6, 3]

length = len(numbers)
 
list_1=[]

for i in range(0,length,+1):#I want to know how many times does each element repeat.
    t = numbers.count(numbers[i])
    
    list_1.append(t)  #and than add all the t values in list_1.

maxi=max(list_1)  #max value of the list_1 is my most repeated element.
order = numbers[maxi]  # the order of this element has the same order in numbers list.
print(f"The most frequent number is {order} and it was {maxi} times repated.")
 
    
    
    
    
    
 


#print(numbers.count(numbers[0]))

#print("the most frequent number is 3 and it was 4 times repeated")