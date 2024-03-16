# Delete Object Properties -> By using the del keyword, properties of objects can be deleted.

class Person:
    def __init__(self, name , age) -> None:
        self.name = name
        self.age = age

    def display(self):
        print(f'My name is {self.name} and age is {self.age}')

p1 = Person('John' , 36)
print()
p1.display()
print()
del p1.age  # * deletes the age contained in the object
p1.display()    # ! object has no attribute age 





