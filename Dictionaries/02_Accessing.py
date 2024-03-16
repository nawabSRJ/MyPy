d1 = {5 : 2 , 'a' : 'string', (1,2) : 'tuple','[3,2]' : 'list'}

for key in d1:
    print(key, ':' , d1[key])

# * a dict key must be of IMMUTABLE type like - string , tuple or a number

# ! attempting to access a key that doesn't exist , causes an error
i = 7
if d1.get(i) is not None :
    print('Key exists')
    d1[5] += 5
else :
    d1[i] = 1

# if d1.get('a') is not None :
#     print('2nd Key exists')

print(d1[5])
print(d1[i])