# ! Create a function in python that accepts a filename and reports the file's longest line 

# * Method : Input Filename -> read through it while keeping track of lines and saving them in a
#string var(say s) as soon as you encounter a line longer than your current value of
#var s -> print s
    
while True:
    try :    
        name = input("Enter the file name : ") 
        s = '' # to store and keep track of the longest line
        with open(f'{name}','r') as f:
            y = f.readline()
            while y != '':
                if(len(y) > len(s)):
                    s = y
                y = f.readline()
    except Exception as e :
        print('File does not exist')
        q = input('Would like to enter again? (Y/N)')
        if q == 'y' or q == 'Y':
            continue
        else:
            break
    else :
        print('The longest line : ',s)
        break

