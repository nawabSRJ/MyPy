
import mysql.connector
mydb = mysql.connector.connect(host = 'localhost',
                               user = 'root',
                               password = '123456',
                               database = 'PyTest')

cur = mydb.cursor()
s = "CREATE TABLE book(bookid int(4) , title varchar(20) , price float(5,2))"

cur.execute(s) # * this statement is mandatory for executing your command

