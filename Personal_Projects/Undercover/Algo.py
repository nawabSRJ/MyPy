# 2 Pointer Hashing Algorithm
# constraints - currently working for lower case letter text data only
# info about ASCII Values :
'''
+----------------------+---------------+--------------+
| Character Type       | ASCII Range   | Description  |
+----------------------+---------------+--------------+
| Lowercase Letters    | 97 to 122      | a to z       |
| Uppercase Letters    | 65 to 90       | A to Z       |
| Numerals (0 to 9)    | 48 to 57       | 0 to 9       |
| Other Special Chars  | 0 to 47, 58 to 64, |              |
|                      | 91 to 96, 123 to 127 |            |
+----------------------+---------------+--------------+
'''

alps = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def encrypt(x):
    if x == ' ':
        return ' '
    elif x == '\n' or x == '\t' :
        return x
    else :
        i = alps.index(x) + 1
        x = alps[-i]
        return x
    
if __name__ == '__main__':
    text = input('enter a text : ')
    encrypted = ''.join(map(encrypt , text))    # str() not working, returns map object !!, idk why!
    print(encrypted)



