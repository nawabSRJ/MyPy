# * Question 1 
# ? Write a program to create a phone dictionary for all your frinds and print each key value pair in separate lines

phone = {'Utkarsh' : 349542 , 'Priyanshu' : 198900 , 'Pratham' : '696969' , 'Aryan' : 900000 , 'Vaibhav' : 129845}

for name in phone :
    print(name , ' :' , phone[name])

# * here the loop variable 'name' was assigned the keys of the phone dict one at a time
