'''An array is given with full of anagrams (different meaningful words made up of same letter like - cat , eat , ate)
You need to group them and print them in separate line'''


word_list = ["eat","tea","tan","ate","nat","bat"]
grouped = {}
final_list = []

def disp()->list:
    for word in word_list:
        ans = calculate_group(word)
        if ans not in grouped:  # checks if a key type is in group or not
            grouped[ans] = [word]
        else:
            grouped[ans].append(word)

    for group in grouped.values():
        #print(group)
        final_list.append(group)

    return(final_list)
    
def calculate_group(word):
    sum = 0
    for char in word:
        sum += ord(char)   # adding up the ascii values
    return sum

disp()





        

