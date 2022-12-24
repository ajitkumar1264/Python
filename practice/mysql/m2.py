import mysql.connector

mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="Hrdk1264@"
)

mydbcursor=mydb.cursor()

mydbcursor.execute("CREATE DATABASE yuth")