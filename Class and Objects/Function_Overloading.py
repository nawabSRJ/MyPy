# This is a demo code of function overloading in Python
# todo - To overload a user-defined function in Python, we need to write the function logic in such a way that depending upon the parameters passed, a different piece of code executes inside the function.

class Student:
    def hello(self,name = None):
        if name is not None:
            print(f'Hi {name}')
        else :
            print('Hi')

obj = Student()     # creating class object

obj.hello()     # method called with 0 parameter

obj.hello('Srajan')   # method called with 1 parameter

# * Different Output in different function calls