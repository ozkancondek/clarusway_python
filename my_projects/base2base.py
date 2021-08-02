# -*- coding: utf-8 -*-
"""
Created on Mon Aug  2 22:13:13 2021

@author: admin
"""
num = int(input("Give me a number: "))
base = int(input("Give me the base of number: "))
c_base = int(input("To which base, you want to convert: "))
a = list(str(num)) 
a.sort()
max_digit = a[len(a)-1] #max digit in number
count = 1
while count <= 4:
    if base < int(max_digit):        
        print("The base cant be smaller than any digit in number.")
        num = int(input(f"Give me a number that all digits have to be smaller than {base}: "))
        a = list(str(num)) 
        a.sort()
        max_digit = a[len(a)-1] 
        
    else:
        break
    count += 1
 
def converter(num, base, c_base):
    result = 0
    number = ""
    ls = []
    b = str(num)
    a = len(str(num))
    for i in range(a):
        result = result + int(b[a-1-i])*(base**i)
    while result > 0:
        
         a = result % c_base
         result = result // c_base
         ls.append(a)
        
    ls.reverse()
    for y in range(len(ls)):
        number = number + str(ls[y])
    print("{} in base {} is equal to {} in base {}.".format(num,base,number,c_base))
converter(num,base,c_base)
