import customtkinter as ctk
from tkinter import *
from tkinter import messagebox
import Client2 as c2
# from Client2 import *

app = Tk()
app.resizable(False , False)
app.title('LAN CHAT')




def write_msg(event):
    
    message = msg_bar.get()
    if message.isspace():
        messagebox.showerror('Alert','Please enter a message')
        
    
    msg_bar.delete(0 , 'end')
    # write message in text box
    chat_text.configure(state="normal") # enable state to put message
    chat_text.insert('end' , message + '\n') # using 'end' will ensure that messages are below each other
    chat_text.configure(state="disabled")
    c2.send_manually(message)
    # msgs = message.encode(FORMAT)
    # client.send(msgs)
    # if msgs == DISCONNET_MSG:
    #     print('Disconnecting...')
        

    pass





chat_text = ctk.CTkTextbox(app , width=400 , height=400 , scrollbar_button_color = "red" , font=('Cambria',20) , state="disabled")
msg_bar = ctk.CTkEntry(chat_text , width = 400 , height=30 , placeholder_text="Enter your message" , font=('Cambria',20))


msg_bar.grid(row=20, column=0, sticky="ew")
chat_text.pack()

# todo - bind enter key with send message -> display in textbox
msg_bar.bind('<Return>', write_msg)

app.mainloop()

# start server as the program initiates
