import customtkinter
from tkinter import *

app = Tk()
# By default all colours are set by the color theme. Currently there a three themes available: "blue", "dark-blue" and "green", where "blue" is the standard theme. All themes provide tuple colors for a light and dark appearance mode.

# You can set the theme at the beginning of your programming like the following:
customtkinter.set_default_color_theme("green")  
# Themes: "blue" (standard), "green", "dark-blue"

app.mainloop()