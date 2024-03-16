d = {}

d2 = dict()
print(type(d))
print(type(d2))

# *`````````````````````````````````````````````````````````````````````````````````````

# *(i) creating dictionaries by specifing key : value pairs as keyword arguments in dict()

Employee = dict(name = 'John' , salary = 10000, age = 26)
print(Employee)     # * no error ~ dictionary printed

# *(ii) specify with comma separated values

Emp2 = dict({'name' : 'John' , 'salary' : 10000, 'age' : 26})
print(Emp2)

# *(iii) specify keys separately and corresponding values separately ~ using zip()

Emp3 = dict(zip(('name','salary','age'),('john',10000,26)))
print(Emp3)

# *(iv) specify key : value pairs separately in form of sequences

Emp4 = dict([['name' , 'john'] , ['salary',10000],['age',26]])
print(Emp4)
#  ! be careful with brackets in all the above declarations

# * GETTING SAME OUTPUT FROM ALL THE ABOVE DECLARATIONS

# ! remember : keys must be unique but values may not be


# ? WAP to create a dictionar namely numerals from the following two lists
keys = ['One','Two','Three'] 
values = [1,2,3]
numerals = dict(zip(keys,values))
print(f"Dictionary with list {keys} and {values} is {numerals}")