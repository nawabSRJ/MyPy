# This Tutorial contains about Buttons

import tkinter as tk

window  =  tk.Tk()

button = tk.Button(
    text="Click me!",
    width=25,
    height=5,
    bg="blue",      # bg and fg are short-form for background and foreground
    fg="yellow",
)
button.pack()
window.mainloop()