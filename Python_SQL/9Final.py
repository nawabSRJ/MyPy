# * In this Code i will merge all the info i gathered in the previous lectures and files and make once single program for all the operations we have laerned so far
#  TODO - Make This Program Menu Driven
import mysql.connector
mydb = mysql.connector.connect(host = 'localhost' , user = 'root' , password = '123456' , database = 'PyTest')
cur = mydb.cursor()

def NewTable():
    column_names = []
    print(type(column_names))
    TableName = input("Enter Name of the Table :\t")
    Column_No = int(input("Enter no. of columns : \t"))
    for i in range(Column_No):
        names = input("Name of the Column :")
        column_names.append(names)
    print(column_names, type(column_names))    
    s = f"CREATE TABLE {TableName}({column_names[0]} int(4) , {column_names[1]} varchar(20) , {column_names[2]} int(10))"
    # print(s)
    cur.execute(s)
    

# NewTable()
# * Table Created SUCCESSFULLY !!!

def NewEntry():
    # todo - display tables here (make one func for it)
    TableName = input("Enter Name of the Table where you want to make change :\t")
    # todo - display content of {TableName}
    _id = input("\nEnter bookid :")
    _item = input("\nInput Title :")
    _price = input("\nEnter Price : ")
    s = f"INSERT INTO {TableName}(bookid , title, price) VALUES({_id} ,'{_item}' , {_price})"
    cur.execute(s)
    mydb.commit()
    # todo - Ek tuple of clm_names and clm_values should be created after iterating in the table/ getting info abt the table

    
# NewEntry()
# * Entry(through command) done SUCCESSFULLY !!!
# *Entry(throug input) done SUCCESSFULLY !!!

def display_tables():
    c = "show tables"
    cur.execute(c)
    result = cur.fetchall()
    print(result)
      
      
NewTable()
# display_tables()

