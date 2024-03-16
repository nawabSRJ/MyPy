power = lambda x  : x**2

print(power(2))

# * map function
# this function applies a particular func to every element of an iterable

l = [1,2,3,4,5]
print(map(power , l))   # will return a map object
new_l = list(map(power , l)) # using list() bcoz python3 returns map object when map() is used

print(new_l)

# * second example
my_lower = ['srajan','neel','luv','sid']

my_upper = list(map(str.upper , my_lower))
print(my_upper)

# ! playing with zip() function

my_strings = ['a', 'b', 'c', 'd', 'e']
my_numbers = [1, 2, 3]
my_nums = [1,2,3,4,5,6,7]

results = list(zip(my_strings, my_numbers)) # [('a', 1), ('b', 2), ('c', 3)] ~ will work until it gets arguments from both
results2 = list(zip(my_strings, my_nums)) 
# [('a', 1), ('b', 2), ('c', 3), ('d', 4), ('e', 5)]

print(results)
print(results2)

# todo - making custom zip function with map() function
my_strings = ['a', 'b', 'c', 'd', 'e']
my_numbers = [1, 2, 3, 4, 5]

results = list(map(lambda x, y: (x, y), my_strings, my_numbers))

print(results)

# * learning - only even numbers
nums = [1,2,3,4]

def only_even(num):
    if num  % 2 == 0:
        return num
    else :
        # continue ~ only in loops
        pass

even = list(map(only_even , nums))
print(even)     # [None, 2, None, 4] ~ this teaches us to understand where to use map and where to use filter, in this question ~ filter function is ideal to use 

