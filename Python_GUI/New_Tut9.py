# The side keyword argument of .pack() specifies on which side of the window the widget should be placed. These are the available options:

# tk.TOP
# tk.BOTTOM
# tk.LEFT
# tk.RIGHT

# If you don’t set side, then .pack() will automatically use tk.TOP

import tkinter as tk

window = tk.Tk()

frame1 = tk.Frame(master=window, width=200, height=100, bg="red")
frame1.pack(fill=tk.Y, side=tk.BOTTOM)

frame2 = tk.Frame(master=window, width=100, bg="yellow")
frame2.pack(fill=tk.Y, side=tk.RIGHT)

frame3 = tk.Frame(master=window, width=50, bg="blue")
frame3.pack(fill=tk.Y, side=tk.LEFT)

# * you can also specify tk.BOTH 
window.mainloop()