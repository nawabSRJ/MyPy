# To add some space around each frame, you can set the padding of each cell in the grid. Padding is just some blank space that surrounds a widget and visually sets its content apart.

# The two types of padding are external and internal padding. External padding adds some space around the outside of a grid cell. It’s controlled with two keyword arguments to .grid():

# padx adds padding in the horizontal direction.
# pady adds padding in the vertical direction.

import tkinter as tk

window = tk.Tk()

for i in range(3):
    for j in range(3):
        frame = tk.Frame(
            master = window,
            relief=tk.RAISED,
            borderwidth=2
        )
        frame.grid(row = i, column = j, padx = 5, pady = 5)
        label = tk.Label(master=frame, text=f"Row {i}\nColumn {j}")
        # label.pack()
        # * The extra padding around the Label widgets gives each cell in the grid a little bit of breathing room between the Frame border and the text in the label:

        label.pack(padx = 5, pady= 5)

        
window.mainloop()

# * here the rows and columns will not expand as we resize the window. we will learn this in next Tutorial