# *in python a variable is created when the value is assigned to it

# num = 8
# name = "Srajan"
# surname = 'saxena'
# gender = 'M'
# single = True
# a = 1,7234  # *no error on assigning a numeric value with comma but this will not be considered as a numeric value instead as a tuple

# value = None    # *None is python ~ NULL in Cpp

# print(value , type(value))
# print(type(a))
# print(type(num))
# print(type(name))
# print(type(surname))
# print(type(gender))
# print(type(single))

# # * now we are going to look at types of strings

# #*single line strings :

# text1 = 'hello'  # *by default python creates single line strings with both '' & ""

# # *multiline strings    method 1 : by adding a backslash
# text2 = 'hello\
# there'

# # * method 2 : by typing text in triple quotation marks
# text3 = '''Hello
# THERE'''

# text4 = """Hello 
# World
# There i come!!!"""

# print(text1)
# print(text2)
# print(text3)
# print(text4)

# *lists datatype
person1 = ["Srajan",18,'M']
values_list = [1,2,3,4,5]

print(person1[0]) 
print(values_list[3])
# !lists also allow duplicate entries
list2 = [1,2,3,1,5,7,2]
print(list2)

# *Lists are MUTABLE
values_list[3] = 12
print(values_list[3])

# *Tuples are IMMUTABLE

person2 = ("Shivam",30,'M')
person3 = ("Aaditya",22,'M')


print(person2 , person3)
print(person2[0] , person3[0])

# *Sets are IMMUTABLE and they cannot contain duplicate entries


myset = {1,2,3,2,5}     
print(myset)    # !o/p of this statement : {1, 2, 3, 5}
#*even after initializing the set with duplicate entries it will not display it while printing


# * Sets can contain other 'IMMUTABLE' data types in it like : Tuples
myset2 = {1,2,3,(4,5),(7,18)}
print(myset2)


# *Dictionary(key : value) pair kind of data type where each key must have unique value
vowels = {'a' : 1, 'e' : 2, 'i' : 3, 'o' : 4, 'u' : 5}
print(vowels)
print(vowels['a'])
print(vowels['u'])
# ! print(vowels[1]) -> This statement will give error
