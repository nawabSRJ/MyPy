# Now onwards, we are going to cover geometry managers like .pack() , .place() , .grid()
import tkinter as tk

window = tk.Tk()

# * making 3 squares

# frame1 = tk.Frame(master=window, width=100, height=100, bg="red")
# frame1.pack()

# frame2 = tk.Frame(master=window, width=50, height=50, bg="yellow")
# frame2.pack()

# frame3 = tk.Frame(master=window, width=25, height=25, bg="blue")
# frame3.pack()

# window.mainloop()

# pack() accepts some keyword arguments for more precisely configuring widget placement. For example, you can set the fill keyword argument to specify in which direction the frames should fill. The options are tk.X to fill in the horizontal direction, tk.Y to fill vertically, and tk.BOTH to fill in both directions. Here’s how you would stack the three frames so that each one fills the whole window horizontally:

frame1 = tk.Frame(master=window, height=100, bg="red")
frame1.pack(fill=tk.X)

frame2 = tk.Frame(master=window, height=50, bg="yellow")
frame2.pack(fill=tk.X)

frame3 = tk.Frame(master=window, height=25, bg="blue")
frame3.pack(fill=tk.X)

window.mainloop()

# about more keyword arguments in the next Tutorial
