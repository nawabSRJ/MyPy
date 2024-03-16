# This Tutorial is for the entry widget

import tkinter as tk
window = tk.Tk()

entry = tk.Entry(fg="yellow", bg="blue", width=500)
entry.pack()    #takes single line entry

# Todo - Getting user input with entry widgets

# * There are three main operations that you can perform with Entry widgets:

# * Retrieving text with .get()
# * Deleting text with .delete()
# * Inserting text with .insert()

label = tk.Label(text = "Name : ")
entry = tk.Entry()
name = entry.get()

label.pack()
entry.pack()

# * Text Widget

# * you can perform three main operations with Text widgets:

# * Retrieve text with .get()
# * Delete text with .delete()
# * Insert text with .insert()

text_box = tk.Text()
text_box.pack()

window.mainloop()