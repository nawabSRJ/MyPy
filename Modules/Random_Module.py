import random

print(random.random())  # * returns random floating point number N in the range [0.0,1.0)
#that is 0.0<= N < 1.0

print(random.randint(-15,1)) # * returns a random integer in the range [a,b] that is
#* a<= N <= b

# ! randrange function can be used in 3 ways:

# * 1st Way

# *Syntax : random.randrange(<stopvalue>) -> to generate a random number in the range 0 to <stopvalue>
# the number in the <stopvalue> argument will be EXCLUSIVE

print(random.randrange(10)) 

# *2nd Way

# *Syntax : random.randrange(<start><stop>) -> generates from start to stop

print(random.randrange(10,12))

# * 3rd Way
# * Syntax : random.randrange(<start><stop><step>) -> generates multiple of <step> value between
#start - stop

print(random.randrange(10,20,4))



my_list = [100, 256, 339, 49, 69]
rand_choice = random.choice(my_list)
print(rand_choice)  # Output: Random element from the list



