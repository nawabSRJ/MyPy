class Animal:
 def sound(self):
     print('Animal makes sound.')
class Dog(Animal):
 def sound(self):
     Animal.sound(self)
     #print('Dog barks.')
d = Dog()
d.sound()
