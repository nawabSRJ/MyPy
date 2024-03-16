# .place() geometry manager
import tkinter as tk

window = tk.Tk()
frame = tk.Frame(master=window, width=150, height=150)
frame.pack()

label1 = tk.Label(master=frame, text="I'm at (0, 0)", bg="red")
label1.place(x=0, y=0)

label2 = tk.Label(master=frame, text="I'm at (10, 10)", bg="yellow")
label2.place(x=10, y=10)

window.mainloop()

#  .place() isn’t used often. In addition to this, it has two main drawbacks:

# ! Layout can be difficult to manage with .place(). This is especially true if your application has lots of widgets.

# ! Layouts created with .place() aren’t responsive. They don’t change as the window is resized.

# ! .place() is a poor choice for making responsive and cross-platform layouts.