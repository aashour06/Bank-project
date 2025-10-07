import sqlite3
import pandas as pd


data=pd.read_excel("random_data_no_rowid.xlsx")


conn=sqlite3.connect("database.db")
cur=conn.cursor()
cur.execute("""create table if not exists customers(
            name text,
            phone text,
            address text,
            balance intger,
            password intger
            )""")

data.to_sql("customers",conn,if_exists="replace",index=False)
conn.commit()
conn.close()


def addToDataBase(name ,phone,address,balance,password):
    conn=sqlite3.connect("database.db")
    cur=conn.cursor()
    cur.execute("insert into customers (name,phone,address,balance,password) values (?,?,?,?,?)",(name,phone,address,balance,password))
    conn.commit()
    conn.close()
    print(f"{name} Added Successfully")


def check_password(name,password):
    conn=sqlite3.connect("database.db")
    cur=conn.cursor()
    cur.execute("select rowid, * from customers where name=? And password=?",(name,password))
    Returned=cur.fetchall()
    if Returned==True:
        print("access allowed")
        conn.commit()
        conn.close()
    else:
        print("cannot access")

def change_phone(name,password):
    conn=sqlite3.connect("database.db")
    cur=conn.cursor()
    cur.execute("select rowid, * from customers where name=? And password=?",(name,password))
    Returned=cur.fetchall()
    if Returned:
        print("access allowed")
        phone=input("enter your phone +20 ")
        new_phone= "+20"+phone
        cur.execute("update customers set phone=? where name=? And password=?",(new_phone,name,password))
        print("Added successfully")
        conn.commit()
        conn.close()
    else:
        print("cannot access")

def display_info_from_db(name,password):
    conn=sqlite3.connect("database.db")
    cur=conn.cursor()
    cur.execute("select * from customers where name=? And password=?",(name,password))
    Returned=cur.fetchall()
    if Returned:
        print("access allowed")
        cur.execute("select  * from customers where name=? And password=?",(name,password))
        Returned=cur.fetchall()
        for i in Returned:
            print(i)
        conn.commit()
        conn.close()
    else:
        print("cannot access")


def deposite(name,password,amount):
    conn=sqlite3.connect("database.db")
    cur=conn.cursor()

    cur.execute("select balance from customers where name=? And password=? ",(name,password))
    result=cur.fetchone()
    if result:
        balance=result[0]+amount
        cur.execute("update customers set balance=? where name=? And password=?",(balance,name,password))
        conn.commit()
        conn.close()
        display_info_from_db(name,password)
    else: 
        print("not defined")
    




def withdraw(name,password,amount):
    conn=sqlite3.connect("database.db")
    cur=conn.cursor()

    cur.execute("select balance from customers where name=? And password=?",(name,password))
    result=cur.fetchone()
    if amount<=result[0]:
        balance =result[0]-amount
        cur.execute("update customers set balance=? where name=? And password=?",(balance,name,password))
        conn.commit()
        conn.close()
        display_info_from_db(name,password)
    else:
        print("your balance doesnot enough")
