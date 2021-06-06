from User import User
from Utils import *
import os

header()
command = ''
while command!=":q":
    menu()
    command = int(input("enter command:\t"))
    if command==1:
        user = User(input("username:\t"),input("master password:\t"))
    elif command==2:
        record = {
            'account':input("account:\t"),
            'email':input("email:\t"),
            'login':input("login:\t"),
        }
        user.addRecord(record)
    elif command==3:
        print(user.getRecords(input("password:\t")))
    elif command==4:
        user.dumpFile(input("filename:\t"),input("decrypting? (yes/no):\t"))
    elif command==5:
        user.setConfig(email='yaroslav.tsepkov@gmail.com')
    else:
        print("Not found command:\t")
