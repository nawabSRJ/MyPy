# List Comprehensions
# ?to create a list having the length of words , but the word shoud not be 'the'

sentence = "the quick brown fox jumps"
words = sentence.split()    # type(words) ~ list

word_length = [len(word) for word in words if word != 'the']
print(word_length)

# ? list of even numbers from 1 to 20

even20 = [num for num in range(1,21) if num % 2 == 0]
print(even20)

# ? Uppercase Names:  Given a list of names, create a new list called "upperNames" using a list comprehension that contains the names converted to uppercase.
names = ['srajan','rajeev','stuti']
# upperNames = [name for name in names name = name.upper()]
upperNames = [name.upper() for name in names]
upper = list(map(str.upper , names))    # can be done by map also
print(upper)
print(upperNames)

# ? vowels in a word
word = 'Eoin Morgan'

vow = [letter for letter in word if letter in 'aeiou' or letter in 'AEIOU']
print(vow)

filter_vow = list(filter(lambda x : x in 'AEIOU' or x in 'aeiou', word))
print(filter_vow)   # using filter




