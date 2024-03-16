# By using .columnconfigure() and .rowconfigure() on the window object, you can adjust how the rows and columns of the grid grow as the window is resized. Remember, the grid is attached to window, even though you’re calling .grid() on each Frame widget. Both .columnconfigure() and .rowconfigure() take three essential arguments:

# * Index: The index of the grid column or row that you want to configure or a list of indices to configure multiple rows or columns at the same time

# * Weight: A keyword argument called weight that determines how the column or row should respond to window resizing, relative to the other columns and rows

# * Minimum Size: A keyword argument called minsize that sets the minimum size of the row height or column width in pixels

import tkinter as tk

window = tk.Tk()

for i in range(3):
    
    window.columnconfigure(i, weight=1, minsize=75)
    window.rowconfigure(i, weight=1, minsize=50)
    
    for j in range(3):
        frame = tk.Frame(
            master = window,
            relief = tk.RAISED,
            borderwidth = 2,
        )
        frame.grid(row = i , column = j , padx = 5 , pady = 5)
        label = tk.Label(master=frame, text=f"Row {i}\nColumn {j}")
        label.pack(padx = 5 , pady = 5)


window.mainloop()


