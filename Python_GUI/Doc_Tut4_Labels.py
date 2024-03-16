from tkinter import *
from tkinter import ttk

root = Tk()
root.title("ATM")
#  * Label

#  * A label is a widget that displays text or images, typically that users will just view but not otherwise interact with. Labels are used to identify controls or other parts of the user interface, provide textual feedback or results, etc.
#  * Labels are created using the ttk.Label class. Often, the text or image the label will display are specified via configuration options at the same time:


mainframe = ttk.Frame(root , padding = "3 3 12 12")
mainframe.grid(column = 0, row = 0 , sticky = (N, W, E, S))
root.columnconfigure(0 , weight = 1)
root.rowconfigure(0 , weight = 1)

label = ttk.Label(mainframe, text='Full name:').grid(column = 2, row = 2, sticky=(W , E))
root.mainloop()