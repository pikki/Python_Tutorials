"""
Login System :

Insert your username : himalaya
Insert your email : himalaya@mom.com
Insert your password : himalayakilaru123#
Welcome
Invalid Credentials
"""

print("Login System :")

#taking input
name = input("Insert your username :")
email = input("Insert your email :")
password = input("Insert your password : ")

if (name == 'himalaya' and email == 'himalaya@mom.com' and  password == 'himalayakilaru123#') :
    print('Welcome!')
else :
    print('Invalid Credentials')