# __init__ function demo -> used to assign values in a class, initiated with class

class NumberHolder:
    
    def __init__(self,number) :
        self.num = number
    
    def returnNumber(self):
        return self.num
        # print(self.num)

var = NumberHolder(12)

# when using print in returnNumber func -> then don't use print here :
res = var.returnNumber()  # you can also store the result in a var and then print it
print(res)
# when using return instead of print then -> use print to display the result
# print(var.returnNumber())

        