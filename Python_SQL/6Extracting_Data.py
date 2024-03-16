
import mysql.connector
mydb = mysql.connector.connect(host = 'localhost' , user = 'root' , password = '123456')

cur = mydb.cursor()

s = 'SELECT * FROM BOOK'
cur.execute(s)

result = cur     # * this will fetch all the data from the database

# * Now printing all data :
print(result)
for rec in result :
    print(rec)
    
    
    
    
    
    