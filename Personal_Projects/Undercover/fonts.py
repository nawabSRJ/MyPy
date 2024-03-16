from tkinter import font, Tk

# Create a temporary root window
temp_root = Tk()

# Print available font families
x = font.families()
with open('fontStyles','w')  as f:
    f.write(str(x))
print('Done')
# Close the temporary root window
temp_root.destroy()
