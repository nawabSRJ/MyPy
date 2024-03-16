
import mysql.connector
mydb = mysql.connector.connect(host = 'localhost' , user = 'root' , password = '123456', database = 'PyTest')
cur = mydb.cursor()

s = "DELETE from book WHERE title = 'PHP' "
cur.execute(s)
mydb.commit()

# * Deletion SUCCESSFUL !!!
# * Code is Working Properly !!!





