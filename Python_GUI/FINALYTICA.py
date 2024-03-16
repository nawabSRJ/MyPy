import tkinter
import customtkinter
import mysql.connector

# *------------------------------ SQL Code ----------------------------
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
    

# * System Settings
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

# * App frame
app = customtkinter.CTk()
app.geometry("720x480")
app.title("FINALYTICA")

# * adding UI elements
title = customtkinter.CTkLabel(app, text = 'FINALYTICA')
# title.pack(padx = 10, pady=10)  # * only extend till the dimensions mentioned
title.pack()  # * full maximization possible

# * Button
New_Table = customtkinter.CTkButton(app , text = 'New Table', command = NewTable)
New_Table.pack(padx = 10 , pady = 10) # ! this command is imp. otherwise the button won't show up

# * Run loop
app.mainloop()


