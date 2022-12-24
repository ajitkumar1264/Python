import mysql.connector

mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="Hrdk1264@"
)
myquery=mydb.cursor()
myquery.execute("SHOW DATABASES")
for x in myquery:
    print(x)