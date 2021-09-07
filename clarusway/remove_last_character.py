

"""Remove last character in list of strings:
 given_list = ["Lessons", "Words", "Pythons", "Programers","Clarusways"] 
 expected output : ['Lesson', 'Word', 'Python', 'Programer', 'Clarusway']
 """

given_list = ["Lessons", "Words", "Pythons", "Programers","Clarusways"]
 
print(list(map(lambda i: i.replace(i[len(i)-1],""),given_list)))