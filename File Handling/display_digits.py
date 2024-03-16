#A text file is created that contains alphanumeric text.. Now read that text file and print only digits from that file
# todo - go through the file -> use ord() to detect it as an alphabet and then print it

while True:
    try:
        name = input('Enter the name of the file : ')
        with open(f'{name}','r') as f:
            text = f.read()
        for i in text:
            if(ord(i) >= 48 and ord(i) <= 57):
                print(i , end='')
                print()

    except Exception as e:
        print('File does not exist')
        q = input('Would like to enter again? (Y/N)')
        if q == 'y' or q == 'Y':
            continue
        else:
            break
        
        