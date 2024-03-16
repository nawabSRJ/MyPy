# * Set Basics
# * It can have any number of items and they may be of different types (integer, float, tuple, string etc.). But a set cannot have a mutable element, like list, set or dictionary, as its element.

my_set = {1,2,3}
print(my_set)

my_set={1.0, "Hello", (1, 2, 3)}
print(my_set)

my_set=set([1,2,3,2])   # * we can make set from a list -> it will iterate and make every element of the list as a separate element of the set 
print(my_set)


# * Note : Indexing and Slicing have no meaning as sets are UN-ORDERED 