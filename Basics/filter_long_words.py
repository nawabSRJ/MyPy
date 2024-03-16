# filter words with more than 3 char length

words = ['oneone','hello','hi','m','','ojowej']

def check(word):
    if len(word) > 3:
        return True
    else :
        return False



high = list(filter(lambda word : len(word) > 3 , words))
print(high)
