import mysql.connector
from project_fun import *
mydb = mysql.connector.connect(host='localhost',user='root',password='08bha16apz')
mycursor=mydb.cursor()
mycursor.execute("use miniproject")
print("\t\t\t\t\t\t\t\tWELCOME TO O.DONATION SYSTEM")
print("\t\t\t\t\t\t\t\t\t\t\t1. Sign Up")
print("\t\t\t\t\t\t\t\t\t\t\t2. Log In")
print("\t\t\t\t\t\t\t\t\t\t\t3. Exit")
ch=int(input("Enter your choice:"))
if ch==1:
    Sign_Up()
elif ch==2:
    Log_In()
else:
    print("\t\t\t\t\t\t\t\t\tTHANK YOU")



