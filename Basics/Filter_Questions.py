# ! Some Question based on Filter functions

# ? q1 - Given a list of strings, use filter to extract only those containing the letter 'a'.

words = 'Hello' , 'Name' ,'Age', 'Silence'

def has_a(word):
    if 'A'  in word or 'a' in word :
        return word

    

list_a = list(filter(has_a , words))
result = list(filter(lambda word : 'A'  in word or 'a' in word, words))
print(list_a)
print(result)