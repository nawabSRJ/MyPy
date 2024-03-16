# this exercise is provided by codebasics on YT
# * URL of the exercise - https://github.com/codebasics/data-structures-algorithms-python/blob/master/data_structures/2_Arrays/2_arrays_exercise.md 

# ! Question : Create a list of all odd numbers between 1 and a max number. Max number is something you need to take from a user using input() function 

max = int(input("Enter max number :"))

lst = []

for i in range(max):
    if(i % 2 != 0):
        lst.append(i) 

print(lst)