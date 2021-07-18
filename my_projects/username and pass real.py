
user_name = input("User name: ")
password = int(input("Password: "))
count=1
while user_name != "ozkan" or password != 3507:
    if user_name == "ozkan":
        print("your password is wrong. Enter your informations again")
       
    if password == 3507:
        print("Your username is wrong. Enter your informations again")
        
    if user_name != "ozkan" and password != 3507:
        print("both of your infos wrong")
    user_name = input("User name: ")
    password = int(input("Password"))
    count+=1
    if count >2: 
        print("your account is locked")
        break
    #if count == 3:
       # print("your account is locked")
       # break
 
    
if user_name == "ozkan" and password == 3507:
    print("access confirmed in ",count,". attampt")
 
