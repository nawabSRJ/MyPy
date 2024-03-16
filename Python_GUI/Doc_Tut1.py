from tkinter import *   # * (*) imports all the functions of the Module at once
from tkinter import ttk     # * ttk is a sub-module in tkinter (here we will need to prefix w/ 'ttk')


# *This function converts feet to metres
def calculate(*args):
    try:
        value = float(feet.get())
        metres.set(int(0.3048 * value * 10000.0 + 0.5)/10000.0)
    except ValueError:
        pass
        # print("Please enter a Valid Value")
    
# *-------------------------- GUI Part  -----------------------------

root = Tk()
root.title("Feet to Metres")    # * these 2 lines set up the main application window

# * we create a frame widget, which will hold the contents of our user interface.
mainframe = ttk.Frame(root , padding = "3 3 12 12")
mainframe.grid(column = 0, row = 0 , sticky = (N, W, E, S))

root.columnconfigure(0 , weight = 1)
root.rowconfigure(0 , weight = 1)
# *The columnconfigure/rowconfigure bits tell Tk that the frame should expand to fill any extra space if the window is resized. 


feet = StringVar()
feet_entry = ttk.Entry(mainframe , width = 7, textvariable=feet)    # * creating the Entry Input for value in Feet
# * the arguements above -:
# *'mainframe' : the first arg tells where the 'feet_entry' widget will be placed or mainframe if the parent widget of the child widget 'feet_entry'
# * 'width' : Here, we specify how wide we want the entry to appear, i.e., 7 characters.
# *'textvariable' : 


feet_entry.grid(column = 2 , row = 1,sticky = (W,E))

# *The sticky option to grid describes how the widget should line up within the grid cell, using compass directions. So w (west) means to anchor the widget to the left side of the cell, we (west-east) means to attach it to both the left and right sides, and so on. Python also defines constants for these directional strings, which you can provide as a list, e.g. W or (W, E).

metres = StringVar()
ttk.Label(mainframe , textvariable = metres).grid(column = 2, row = 2, sticky=(W , E))

ttk.Button(mainframe , text = "Calculate" , command = calculate).grid(column = 3 , row = 3 ,sticky = W)

# * 'command' option telling it what to do when pushed, while a label, which holds just static text, does not.

# ! message display :
ttk.Label(mainframe, text = "feet").grid(column = 3, row = 1, sticky = W)
ttk.Label(mainframe , text = "is equivalent to").grid(column = 1 ,row = 2 , sticky = E)
ttk.Label(mainframe , text = "metres").grid(column = 3, row = 2, sticky = W)


# todo - add some space b/w elements of interface
for child in mainframe.winfo_children(): 
    child.grid_configure(padx=5, pady=5)
feet_entry.focus()
root.bind("<Return>", calculate)

# *The first part walks through all of the widgets contained within our content frame and adds a little bit of padding around each so they aren't so scrunched together. (We could have added these options to each grid call when we first put the widgets onscreen, but this is a nice shortcut.)

# *The second part tells Tk to put the focus on our entry widget. That way, the cursor will start in that field, so users don't have to click on it before starting to type.

# * The third line tells Tk that if a user presses the Return key (Enter on Windows), it should call our calculate routine, the same as if they pressed the Calculate button.





root.mainloop()     # * Running the App