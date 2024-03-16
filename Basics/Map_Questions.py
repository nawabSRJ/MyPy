# ! Some Question based on Map functions

# ? q1 - Create a new list using map that contains the lengths of words from an existing list
#of words.

words = ['Hello','Namastey','Hi']

def length(word):
    return len(word)

#word_len = list(map(length , words))
word_len = list(map(lambda word : len(word) , words))
print(word_len)

# ? q2 - Use map to convert a list of temperatures in Celsius to Fahrenheit.

celcius = [40,42,43,21,1,2]

def to_fahren(temp):
    return (temp * 9) /5 + 32

in_fahren = list(map(to_fahren , celcius))

#in_fahren = list(map(lambda temp : (temp * 9) / 5 + 32 , celcius))

print(in_fahren)

# ? square each element

l = [2,4,5]
sq = list(map(lambda x : x ** 2 , l))
print(sq)
