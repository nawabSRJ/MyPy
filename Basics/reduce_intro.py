# reduce intro
from functools import reduce

nums = [1,2,3,4,5]

add = reduce(lambda x , y : x + y , nums)
prod = reduce(lambda x , y : x * y , nums)
print(add)
print(prod)
