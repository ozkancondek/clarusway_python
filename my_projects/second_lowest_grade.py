# -*- coding: utf-8 -*-
"""
Created on Mon Aug  2 21:21:46 2021

@author: admin
"""
""" Second lowest grade example"""
input("You have to give the grades of 5 different student \n and this code will show you name/s of student/s with second lowest grade. ")
c= 1
class_list = []
grades = []
while c <= 5: #take datas
    name =  input(f"Enter the name of {c}. student: ")
    grade = float(input(f"Enter the grade of {c}. student: "))
    ls = [name,grade]
    grades.append(grade)
    class_list.append(ls)
    c+=1
print("The list of students informations are below.\n{}".format(class_list))
grades.sort()
for x in range(1,len(grades)): #find second lower grade
    if min(grades) != grades[x]: 
        break

names =[]
for i in range(len(class_list)): 
    for j in range(2):
        if class_list[i][j] == grades[x]:
            names.append(class_list[i][0])
names.sort()
print("Name/s of student/s with second lowest grade is/are below.")
for y in names:
    print(y)