import customtkinter as ctk
from tkinter import *
from tkinter import messagebox

app = Tk()
app.geometry("500x500")
button1 = ctk.CTkButton(app, fg_color="red" , bg_color = 'black')  # single color name
button1.pack()
button2 = ctk.CTkButton(app, fg_color="#FF0000")  # single hex string
button2.pack()
button3 = ctk.CTkButton(app, fg_color=("#DB3E39", "#821D1A"))  # tuple color
button3.pack()

def button_event():
    messagebox.showinfo("Title","Button Pressed")

# * corner_radius : makes it round
# * border_width : specifies the width of the border
# * border_spacing : spacing between text and image and button border in px, default is 2 , height can affected if increased 
# * text_color : text color, tuple: (light_color, dark_color) or single color
# * text_color_disabled : text color when disabled, tuple: (light_color, dark_color) or single color

# * font	button text font, tuple: (font_name, size), (set negative size value for size in pixels)

# * image	put an image on the button, removes the text, must be class PhotoImage (This is ig used for logo-image buttons)
# * compound	set image orientation if image and text are given ("top", "left", "bottom", "right")

newbutton = ctk.CTkButton(app , text = "CTk Button" ,
                          width = 60,
                          height = 40,
                          border_width = 1,
                          fg_color = "purple",
                          corner_radius = 8,
                          border_spacing = 4,
                          text_color = "green",
                          font = ('Cambria',20),
                          command = button_event)



# *  Methods :
# .configure(attribute=value, ...) : All attributes can be configured, for example:
newbutton.configure(text="new text")

# .cget(attribute_name) : Pass attribute name as string and get current value of attribute, for example.
text = newbutton.cget("text")

newbutton.pack()

app.mainloop()