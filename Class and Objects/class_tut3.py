''' In this tut , we will see how to create an object of a class'''
class Myclass:
    x = 10
    def func(self):
        print('Hello')
        pass

ob = Myclass() # creating an object of 'Myclass'

#print(Myclass.func)

#print(ob.func)

#Myclass.func()
ob.func()
