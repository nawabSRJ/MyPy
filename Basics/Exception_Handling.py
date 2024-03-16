# Exception Handling 
# * In Python, try-except is a mechanism for handling exceptions or errors in a program. The try block contains the code that might raise an exception, and the except block contains the code that handles the exception if it occurs.


# todo - get to know try - except in python

# a = input("Enter the number :  ")       # ? what if we passed a string in here
# print(f"Multiplication table of {a} is : \n")

# try :
#     for i in range(1,11):
#         print(f"{a} x {i} = {int(a) * i}")
# except Exception as e:  # * can also just write 'except :'
#     print("Some error occured : \n")
#     print(e)
    
# print("Some lines of code")    # * this will get executed only when exception handling is performed above else the program will terminate as soon as error is encountered
    
# ! try-except can handle multiple types of errors and that too specific , for ex:

# try:
#     num = int(input("Enter a number : "))
#     a = [6,3]
#     print(a[num])
# except ValueError:
#     print("Not a Number")
# except IndexError:
#     print("Invalid Index")
    
# * ----------------- Finally Keyword ---------------------

# * The finally keyword in Python is used to define a block of code that will be executed no matter what, whether an exception occurs or not. It is often used for cleanup operations, ensuring that certain actions are taken regardless of whether an exception is raised or a return statement is passed

def func1():
    try :
        num = int(input("Enter a number : "))
        l = [2,5,7]
        print(l[num])
        return 1        # * success
    except :
        print("Some error occured")
        return 0        # ! fail

    finally:
        print("I am INEVITABLE")


x = func1()
print(x)
    

    