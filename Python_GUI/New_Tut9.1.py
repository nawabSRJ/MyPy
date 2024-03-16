# Practicing the New_Tut9 thing, and making a Tiranga from Tkinter

import tkinter as tk

window = tk.Tk()

frame1 = tk.Frame(master = window , bg = "orange",width=2000, height = 100)
frame1.pack(fill = tk.Y , side = tk.TOP)

frame2 = tk.Frame(master = window , bg = "white",width=2000, height = 100)
frame2.pack(fill = tk.Y , side = tk.TOP)

frame3 = tk.Frame(master = window , bg = "green",width=2000, height = 100)
frame3.pack(fill = tk.Y , side = tk.TOP)

window.mainloop()