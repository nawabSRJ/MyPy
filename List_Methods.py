l = [11,45,65,23,69,92,2]
print(l)
l.append(5) # *appends an element at the last position
l.sort()    # !by default sorts in ascending order
l.append("Srajan")
print(l)    # *output here - [2, 5, 11, 23, 45, 65, 69, 92, 'Srajan']

# l.sort()  # ! this line will get error :  l.sort() TypeError: '<' not supported between instances of 'str' and 'int'   ~ which means sort() function won't work with list containing integer and string elements

# ? let's check if it works with int and float value

lst = [11,45,5,67,23,23.5,23.7,92,90,90.2,99,99.9]
lst.sort()
print(lst)      # * it is working!!!

# ? How to sort in descending order

lst.sort(reverse = True)    # * this will sort in descending order
print(lst)

lst2 = [1,5,7,3,1,6,3.2,5.7,7]

print(lst2.index(5)) # * returns the index of the 1st occurence element in '()'
print(lst2.index(7)) # ! REMEMBER index() returns index of only 1st occurence of the element only 

print(lst2.count(7)) # * returns the no. of times an element occurs in a list 

lst3 = lst2  # * lst2 cloned in lst3 ~ 'lst3' will point to the same memory reference which 'lst2' points to
print(lst3)

lst3[0] = 0     # ! this will change 'lst2' 0th index element as well ~ because 'lst3' also points to the same memory reference which 'lst2' does due to which change in either of them will reflect in the other 
print(lst2)

names = ["Srajan","Priyanshu","Utkarsh","Pratham","Aryan"]

names.insert(2,"Ansh")  # *inserting at a particular index ~ all the elements will shift to right
print(names)    

girls = ["Anshika","Anushka","Anjali","Stuti","Sheersha"]
 
print(names)
names.extend(girls) # *add the elements of 'girls' list at the end of 'names' list
print(names)
# * result : ['Srajan', 'Priyanshu', 'Ansh', 'Utkarsh', 'Pratham', 'Aryan', 'Anshika', 'Anushka', 'Anjali', 'Stuti', 'Sheersha'] 

# ? what if we used append() instead of extend(), let's try!!!

# *set 'names' list to initial state
names = ["Anshika","Anushka","Anjali","Stuti","Sheersha"] 
names.append(girls)  # * now using append() instead of extend()
print(names)  
# * result : ['Anshika', 'Anushka', 'Anjali', 'Stuti', 'Sheersha', ['Anshika', 'Anushka', 'Anjali', 'Stuti', 'Sheersha']]

#  * Clearly we can observe that the append() adds as a 'list' whereas using extend() the new elements will be added as string or int in case of numbers, you can further check by using type() method


# TODO :  Concatenate two lists 

k = l + lst
print(k)








