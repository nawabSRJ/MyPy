import customtkinter as ctk
from tkinter import messagebox
from tkinter import *

app = Tk()
app.geometry("500x500")

# * state :	"normal" (standard) or "disabled" (not clickable)
# * placeholder_text : hint on the entry input (disappears when selected), default is None, don't works in combination with a textvariabl
# * placeholder_text_color	tuple: (light_color, dark_color) or single color
# * width :	entry width in px
# * height :	entry height in px
# * corner_radius :	corner radius in px
# * fg_color :	foreground color, tuple: (light_color, dark_color) or single color or "transparent"
# * text_color :	entry text color, tuple: (light_color, dark_color) or single color

entry = ctk.CTkEntry(app, placeholder_text="CTkEntry",
                     width = 180,
                     corner_radius = 10,
                     state = 'normal')
entry.pack()
app.mainloop()


# * METHODS
# .configure(attribute=value, ...)
# All attributes can be configured, for example:

# entry.configure(state="disabled")

# .cget(attribute_name)
# Pass attribute name as string and get current value of attribute, for example:

# state = entry.cget("state")

# .bind(sequence=None, command=None, add=None)
# Bind command function to event specified by sequence.

# .delete(first_index, last_index=None)
# Deletes characters from the widget, starting with the one at index first_index, up to but not including the character at position last_index. If the second argument is omitted, only the single character at position first is deleted.

# .insert(index, string)
# Inserts string before the character at the given index.

# .get()
# Returns current string in the entry.