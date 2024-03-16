
import mysql.connector
mydb = mysql.connector.connect(host = 'localhost',user = 'root', password = '123456')

cur = mydb.cursor()

cur.execute("CREATE DATABASE PyTest")

# *creating a database with name 'PyTest' to work with Python - SQL 
