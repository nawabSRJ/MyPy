'''Write a Program to remove vowels from a string'''

S = input("Enter String :\t")
string = ""
v = 'aeiouAEIOU'

for letter in S:
    if letter not in v :
        string += letter


print(string)
