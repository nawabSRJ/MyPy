# Appearance Mode
import customtkinter
from tkinter import *

app = Tk()

# The appearance mode decides, which color will be picked from tuple colors, if the color is specified as a tuple color. You can set the appearance mode at any time with the following command:
customtkinter.set_appearance_mode("system")  # default
customtkinter.set_appearance_mode("dark")
customtkinter.set_appearance_mode("light")

app.mainloop()
