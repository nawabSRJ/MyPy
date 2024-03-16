from tkinter import *
from tkinter import ttk

root = Tk()

# * create a button passing two options :
button1 = ttk.Button(root, text = 'Hello' , command='PressButton1')
button1.grid()
button1['text']
root.mainloop()


 