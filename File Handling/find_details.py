# 'students.txt' file has a rollNo Name Course Fee

while True:
    try:
        s = '' 
        with open('Students.txt') as f:
            y = f.readline()
            while y != '':
                if '1005' in y :
                    ans = y
                y = f.readline()
    except Exception as e:
        print('Exception Occured : ', e)
        q = input('Would like to enter again? (Y/N)')
        if q == 'y' or q == 'Y':
            continue
        else:
            break
    else :
        
        print('Record :\nRollNo Name Course Fee\n', ans)
        break
                    
                    
