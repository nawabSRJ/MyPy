# * Anonymous Functions
# * filter() function

# ? The following is a list (iterable) of the scores of 10 students in a Chemistry exam.
#Let's filter out those who passed with scores more than 75...using filter.

scores = [66, 90, 68, 59, 76, 60, 88, 74, 81, 65]

def even(num):
    if num % 2 == 0:
        return True
    else :
        return False
    


evens = list(filter(even , scores))

print(evens)
def check_score(score):
    return (score > 75) # True if score > 75


over_75 = list(filter(check_score , scores))    # syntax : (function , iterable)

print(over_75)



# ? The next example will be a palindrome detector. 

dromes = ("demigod", "rewire", "madam", "freer", "anutforajaroftuna", "kiosk")

palindromes = list(filter(lambda word : word == word[::-1] , dromes))

print(palindromes)
