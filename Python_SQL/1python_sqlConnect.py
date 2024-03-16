
import mysql.connector
mydb = mysql.connector.connect(host = 'localhost',
                               user = 'root',
                               password = 'nawab.saxena18')

print(mydb.connection_id) 

# * Congrats the Connection is ESTABLISHED !!!