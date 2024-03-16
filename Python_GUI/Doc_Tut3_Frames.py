from tkinter import *
from tkinter import ttk

# *A frame is a widget that displays as a simple rectangle. Frames help to organize your user interface, often both visually and at the coding level. Frames often act as master widgets for a geometry manager like grid, which manages the slave widgets contained within the frame.

# *Frames are created using the ttk.Frame class:
root = Tk()
frame = ttk.Frame(root)

# * Padding

# *The padding configuration option is used to request extra space around the inside of the widget. If you're putting other widgets inside the frame, there will be a margin all the way around. You can specify the same padding for all sides, different horizontal and vertical padding, or padding for each side separately.

frame['padding'] = 5             # ! 5 pixels on all sides
# frame['padding'] = (5,10)        # ! 5 on left and right, 10 on top and bottom
# frame['padding'] = (5,7,10,12)   # ! left: 5, top: 7, right: 10, bottom: 12

# * Borders

# *You can display a border around a frame widget to visually separate it from its surroundings. You'll see this often used to make a part of the user interface look sunken or raised. To do this, you need to set the borderwidth configuration option (which defaults to 0, i.e., no border) and the relief option, which specifies the visual appearance of the border. This can be one of: flat (default), raised, sunken, solid, ridge, or groove.

frame['borderwidth'] = 20
frame['relief'] = 'sunken'

# * Frames have a style configuration option, which is common to all of the themed widgets. This lets you control many other aspects of their appearance or behavior. This is a bit more advanced, so we won't go into it in too much detail right now. 
# ! But here's a quick example of creating a "Danger" frame with a red background and a raised border.

s = ttk.Style()
s.configure('Danger.TFrame', background='red', borderwidth=5, relief='raised')
ttk.Frame(root, width=200, height=200, style='Danger.TFrame').grid()


root.mainloop()