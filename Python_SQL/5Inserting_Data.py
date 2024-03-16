
import mysql.connector
mydb = mysql.connector.connect(host = 'localhost',
                               user = 'root',
                               password = '123456',
                               database = 'PyTest')

cur = mydb.cursor()
s = "INSERT INTO book (bookid, title, price) VALUES(%s , %s, %s)"
b1 = (1,"Python3 Book",345)
cur.execute(s , b1)
mydb.commit() # * Must use statement , bcoz if u didn't use commit() after modifying then your changes won't be saved/displayed on the Database

# * Now entering Multiple Records

# todo - make a list of tuples to enter Multiple Records
books = [(2,'PHP',135),(3,'Java8',450),(4,'HTML',200)]

cur.executemany(s,books)
mydb.commit()



# ! "Python3" book record is now entered twice , bcoz you forgot to comment the code while executing the second time









