# * making a simple result display / registration form in tkinter
import customtkinter as ctk
from tkinter import * 
from tkinter import messagebox

app = Tk()
app.geometry("600x550")
app.resizable(False , False)

name_entry = ctk.CTkEntry(app , placeholder_text = 'Name', 
                          width = 180,
                          corner_radius = 10,
                          state = 'normal')
name_entry.grid(row = 0 , column = 14)
# name_entry.pack(pady = 12)

age_entry = ctk.CTkEntry(app , placeholder_text = 'Age', 
                          width = 180,
                          corner_radius = 10,
                          state = 'normal')
age_entry.grid(row = 1 , column = 14 ,pady = 12)
# age_entry.pack(pady = 12)

roll_entry = ctk.CTkEntry(app , placeholder_text = 'Roll No.', 
                          width = 180,
                          corner_radius = 10,
                          state = 'normal')
roll_entry.grid(row = 2, column = 14 , pady = 12)
# roll_entry.pack(pady = 12)

gender = ctk.CTkComboBox(app , values = ['Male' , 'Female'],
                        width = 120,
                        height = 25,
                        font = ('Cambria',18),
                        corner_radius = 10)
gender.grid(row = 3 , column = 14 , pady = 12)
# gender.pack(pady = 12)

submit = ctk.CTkButton(app ,text = 'Submit',width = 60,
                       height = 40,
                        border_spacing = 2,
                        border_width = 3,
                        fg_color = 'green',
                       font = ('Cambria',20))
submit.grid(row = 4 , column = 14, pady = 12)



app.mainloop()