import mysql.connector
mydb = mysql.connector.connect(host = 'localhost' , 
                               user = 'root' ,
                               password = 'nawab.saxena18',
                               database = 'undercover')

cur = mydb.cursor()
name_var = 'im_srj07'
q = 'SELECT username FROM USERS'
cur.execute(q)
res = cur.fetchall()
print(res)

for i in res:
    t = i
    if t[0] == name_var:
        print('Found')
    