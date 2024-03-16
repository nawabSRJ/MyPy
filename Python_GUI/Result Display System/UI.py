from tkinter import *
from tkinter import messagebox
import customtkinter as ctk

app = Tk()
ctk.set_appearance_mode("System")

ctk.set_default_color_theme("green")
app.geometry("600x700")
app.title("Result")
app.resizable(False,False)

# * ------------------ main design
name_label = ctk.CTkLabel(app,text = 'Name')
name_label.grid(row = 0, column = 0, rowspan = 1, columnspan = 5, padx = 20 , pady = 20)

name_entry = ctk.CTkEntry(app,placeholder_text = 'Srajan')
name_entry.grid(row = 0 , column = 1 , columnspan = 3 , padx = 20, pady = 20)

# age_label = ctk.CTkLabel(app,text = 'Age ')

app.geometry("500x50")

app.mainloop()