# -*- coding: utf-8 -*-
"""
Created on Thu Aug 12 17:35:11 2021

@author: admin
"""

#lambda in-class exercises
#If you need to use a one-time function, defining a lambda function is the best option.
def a (x,y):
    return x+y
#---or
lambda x,y: x+y
#-------------
lambda x: "odd" if x%2 !=0 else "evem"
#------------call
print((lambda x,y:x+y)(2,3)) # First option
a = lambda x,y:x+y
print(a(2,3)) #second option
#--reverse
print((lambda x: x[::-1])("ozkan"))#lambda+iterible
#--even,odd
 
for i in  [1,2,3,4,5,10]:
    print(i,":",(lambda x: "odd" if x%2==1 else "even")(i))
#-----reverser function
a = "ozkan"
reverser = lambda x:x[::-1]
print(reverser(a))