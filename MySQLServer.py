#!/usr/bin/python3
#creates the database alx_book_store in a MySQL Server

import mysql.connector

#Replace with your connection details
try:
    #Connect to MysqlServer
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password=""
    )

    mycursor = mydb.cursor()
    #Executes sql statements using the execute() method on cursor
    mycursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")

    print("Database 'alx_book_store' created successfully!")

except mysql.connector.Error as e:
    print(f"Error:{e}")

finally:

    #close cursor and connection to the db
    try:
        mycursor.close()
        mydb.close()
    except Exception:
        pass