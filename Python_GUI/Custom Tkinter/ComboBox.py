import customtkinter as ctk
from tkinter import messagebox
from tkinter import *

app = Tk()
app.geometry("500x500")

def combobox_callback(choice):
    print("combobox dropdown clicked:", choice)

# * button_color	right button color, tuple: (light_color, dark_color) or single color
# * corner_radius	corner radius in px ~ makes it round
# * border_width	border width in px
combobox = ctk.CTkComboBox(app, values=["Option 1", "Option 2","Option 3"],
                           command=combobox_callback,
                           width = 150,
                           height = 35,
                           font = ('Cambria',18),
                           dropdown_hover_color = ("purple"),
                           dropdown_fg_color = ("green"),
                           button_color = ("red"),
                           border_width = 4,
                           corner_radius = 12)

combobox.pack()
# combobox.set("option 4") # no error in case the option set in not present in the values list
combobox.set("Choose")

# * Methods
# .get()
# Get current string value of combobox entry.

# .set(value)
# Set combobox to specific string value. Value don't has to be part of the values list

# .cget(attribute_name)
# Pass attribute name as string and get current value of attribute, for example :
# state = combobox.cget("state")

# .configure(attribute=value, ...)
# All attributes can be configured, for example:
# combobox.configure(values=["new value 1", "new value 2"])

app.mainloop()