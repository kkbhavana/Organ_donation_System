import mysql.connector

mydb = mysql.connector.connect(host='localhost', user='root', password='08bha16apz')
mycursor = mydb.cursor()
mycursor.execute("use miniproject")


def Log_In():
    u_name= input("Enter your  User name:")
    password = input("Enter your Password:")
    s = "select Username from Userdetails where password='{}' ".format(password)
    mycursor.execute(s)

    if mycursor.fetchone():
        print("\t\t\t\t\t\t\t\t\tLOGIN SUCCESSFULLY\n\n")
        search_organ()
    else:
        print("\t\t\t\t\t\t\t\t\tACCOUNT DOES NOT EXIST\n\t\t\t\t\t\t\t\t\t\tPLEASE SIGN UP")
        Sign_Up()



def Sign_Up():
    print("\n\t\tCREATE NEW ACCOUNT!!!")
    Name = input("Enter your name:")
    Username = input("enter your user name:")
    DOB = input("Enter your dob:")
    Phone = input("Enter your phone number:")
    Place = input("Enter your place:")
    Password = input("Enter your password")
    Confirm_Password = input("Re-enter your password:")
    if Confirm_Password == Password:
        y = "insert into Userdetails values('{}','{}','{}','{}','{}','{}') ".format(Username,Name,DOB, Phone, Place,                                                                            Password)
        mycursor.execute(y)
        mydb.commit()
        search_organ()
    else:
        print("\t\t\t\t\t\t\t\t\tPassword not matching")


def search_organ():
    while True:
        print("\t\t\t\t\t\t\t\t\t1. Search according to Organ:")
        print("\t\t\t\t\t\t\t\t\t2. Search according to Blood group:")
        print("\t\t\t\t\t\t\t\t\t3. Exit")
        ch = int(input("Enter your choice:"))
        if ch == 1:
            organ = input("Enter required organ:")
            a = f"select Name,Age,Blood_group,Phone_number ,Status from DonerDetails where organ='{organ}' "
            mycursor.execute(a)
            res=mycursor.fetchall()
            if not res:
                print("\n\t\t\t\t\t\t\t\t\tNO RECORDS FOUND\n\n")
            else:
                for i in res:
                    print(i)
        elif ch == 2:
            blood = input("Enter required blood group:")
            b= f"select Name,Age,Blood_group,Phone_number,Status from DonerDetails where Blood_group ='{blood}' "
            mycursor.execute(b)
            res = mycursor.fetchall()
            if not res:
                print("\n\t\t\t\t\t\t\t\t\tNO RECORDS FOUND\n\n")
            else:
                for i in res:
                    print(i)
        elif ch==3:
            print("\t\t\t\t\t\t\t\t\tTHANK YOU FOR VISITING")
            break

        else:
            print("\t\t\t\t\t\t\t\t\tINVALID ENTRY!!!")
            search_organ()




