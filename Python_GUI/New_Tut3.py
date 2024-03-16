# This Tutorial Contains about Labels

import tkinter as tk

window = tk.Tk()
label = tk.Label(text="Hello, Tkinter", background="#34A2FE")
greeting = tk.Label(
    text = "Namastey",
    foreground="white",     #  * Set the text color to white
    background="black",      # * Set the background color to black
    width=10,
    height=10   # *setting up height and width
    )
           
greeting.pack()              
label.pack()      
window.mainloop()