import customtkinter as ctk
from tkinter import messagebox
from tkinter import *

app = Tk()
app.geometry("500x500")


def checkbox_event():
    checkbox.configure(state = "disabled")  # this will let the user either select or deselect once and cannot change later
    # print("checkbox toggled, current value:", check_var.get())

# * variable: This is a Tkinter variable that is associated with the checkbox. It's typically an instance of StringVar, IntVar, or BooleanVar. The variable will hold the value of the checkbox. If the checkbox is checked, the variable will be set to the onvalue; if unchecked, it will be set to the offvalue 

# OR SIMPLY -> variable	: Tkinter variable to control or read checkbox state

# * onvalue: This is the value that the associated variable will be set to when the checkbox is checked. In your example, it's set to "on." (you can set this to anything , like : 'khula'/'band')

# * offvalue: This is the value that the associated variable will be set to when the checkbox is unchecked. In your example, it's set to "off." (you can set this to anything , like : 'khula'/'band')

# *checkbox_width :	width of checkbox in px

# *checkbox_height : height of checkbox in px

# * state	tkinter.NORMAL (standard) or tkinter.DISABLED (not clickable, darker color) ~ remember - your default state will be set, if on , and your state is disabled then you cannot deselect the check box

check_var = ctk.StringVar(value="off")

checkbox = ctk.CTkCheckBox(app, text="CTkCheckBox",
                           command=checkbox_event,
                           variable=check_var, 
                           width = 70,
                           height = 70,
                           checkbox_width = 20,
                           checkbox_height = 20,
                           onvalue="on",
                           offvalue="off",
                           )
                
                
checkbox.pack()                     


# * Methods 
# .configure(attribute=value, ...)
# All attributes can be configured, for example

# checkbox.configure(state="disabled")

# .get()
# Get current value, 1 or 0 (checked or not checked)


# .select()
# Turn on checkbox (set value to 1), command will not be triggered.

# .deselect()
# Turn off checkbox (set value to 0), command will not be triggered.

# .toggle()
# Flip current value, command will be triggered

app.mainloop()