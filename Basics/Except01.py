# Exception Handling file 01 ~ BASICS
while True:
    try :
        n = int(input('Enter a number : '))
        break
    except (ArithmeticError , ValueError , ZeroDivisionError):
        print('Invalid Type')

# multiple exceptions can be given in form of tuple
  
  