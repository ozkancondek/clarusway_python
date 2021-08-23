# -*- coding: utf-8 -*-
"""
Created on Mon Aug 23 15:32:21 2021

@author: admin
"""

#send mail
import smtplib
server = smtplib.SMTP("smtp.gmail.com",587) #protochol
print(server.starttls())
password="Ozkancm577"
print(server.login("ozkncndek",password)) #https://myaccount.google.com/lesssecureapps?pli=1&rapt=AEjHL4OyUv_3cZhxjGeUWvUZ4DWopsS4QwvyFHZzKi2Xj8te-X183lbVecvPi5kMItu-IELwVzDNkeuCdscZKrIlaFCl_FyPyw
message = "Pyhton Message"
mail = "ozkancondek07@gmail.com "
print(server.sendmail("ozkncndk@gmail.com", mail, message))
server.quit()

