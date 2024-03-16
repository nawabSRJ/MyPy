# Adjusting Frame Appearance With Reliefs
# * Frame widgets can be configured with a relief attribute that creates a border around the frame. You can set relief to be any of the following values:

# tk.FLAT: Has no border effect (the default value)
# tk.SUNKEN: Creates a sunken effect
# tk.RAISED: Creates a raised effect
# tk.GROOVE: Creates a grooved border effect
# tk.RIDGE: Creates a ridged effect

import tkinter as tk

border_effects = {
    "flat": tk.FLAT,
    "sunken": tk.SUNKEN,
    "raised": tk.RAISED,
    "groove": tk.GROOVE,
    "ridge": tk.RIDGE,
}

window = tk.Tk()

for relief_name, relief in border_effects.items():
    frame = tk.Frame(master=window, relief=relief, borderwidth=5)
    frame.pack(side=tk.LEFT)
    label = tk.Label(master=frame, text=relief_name)
    label.pack()

window.mainloop()