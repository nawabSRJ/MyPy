import time
timestamp = time.strftime("%H:%M:%S")   # * gives the local time in computer
print(timestamp)

# * by default they are <str> , so typecasted to <int>
hour = int(time.strftime("%H"))  # * H for hours , M for minutes , S for seconds
minutes = int(time.strftime("%M"))
print(hour , type(hour))
print(minutes , type(minutes))


if(hour > 1 and hour<12):
    print("Good Morning!")
elif(hour>12 and hour < 16):
    print("Good Afternoon")
elif(hour > 16 and hour <24):
    print("Good Evening")