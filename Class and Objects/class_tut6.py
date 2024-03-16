# Class Variables vs Instance Variable

# ? Python program to show that the variables with a value assigned in class declaration, are class variables and variables inside methods and constructors are instance variables. 

class Samsung:
    # class Var
    mobile = 'Samsung'
    # the init constructor
    def __init__(self,model,color) -> None:
        # instance var
        self.model = model
        self.color = color

# Object of class samsung
a7 = Samsung('A7Series','Blue')
s7 = Samsung('S7Series','Red')

print('A7 Details : ')
print(a7.mobile)
print(a7.model)
print(a7.color)

print('S7 Details : ')
print(s7.mobile)
print(s7.model)
print(s7.color)


# * class var can be accessed using class name also
print()
print(Samsung.mobile)

        
