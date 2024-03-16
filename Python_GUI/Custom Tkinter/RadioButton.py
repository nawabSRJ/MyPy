import customtkinter as ctk
from tkinter import *
from tkinter import messagebox

app = Tk()
app.geometry("500x500")

def radiobutton_event():
    print("radiobutton toggled, current value:", radio_var.get())

radio_var = IntVar(value=0) # * common variable for Binding Radio Buttons 
radiobutton_1 = ctk.CTkRadioButton(app, text="CTkRadioButton 1",
                                             command=radiobutton_event, variable= radio_var, value = 1)
radiobutton_2 = ctk.CTkRadioButton(app, text="CTkRadioButton 2",
                                             command=radiobutton_event, variable= radio_var, value =2,
                                             state = 'disabled')
radiobutton_1.pack()
radiobutton_2.pack()
# width	width of complete widget in px
# height	height of complete widget in px
# radiobutton_width	width of radiobutton in px
# radiobutton_height	height of radiobutton in px
# corner_radius	corner radius in px
# border_width_unchecked	border width in unchecked state in px
# border_width_checked	border width in checked state in px
# radiobutton_1.grid(row = 1 , column = 4,padx = 5)
# radiobutton_2.grid(row = 1 , column = 5,padx = 5)

# fg_color	foreground (inside) color, tuple: (light_color, dark_color) or single color
# border_color	border color, tuple: (light_color, dark_color) or single color
# hover_color	hover color, tuple: (light_color, dark_color) or single color
# text_color	text color, tuple: (light_color, dark_color) or single color
# text_color_disabled	text color when disabled, tuple: (light_color, dark_color) or single color
# text	string
# textvariable	Tkinter StringVar to control the text
# font	button text font, tuple: (font_name, size)
# hover	enable/disable hover effect: True, False
# state	"normal" (standard) or "disabled" (not clickable, darker color)
# command	function will be called when the checkbox is clicked
# variable	Tkinter variable to control or read checkbox state
# value	string or int value for variable when RadioButton is clicked

app.mainloop()