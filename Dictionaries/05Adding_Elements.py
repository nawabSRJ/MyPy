# you can add new elements to a dictionary using assignment operator , BUT the key being added must not exist in the dictionary and must be unique.
# * In case the key already exists, then the value of existing key will ne changed
# * Syntax : <dict_name>[<key>] = <value>

Emp = {'name' : 'John' , 'age' : 24, 'salary' : 10000}
Emp['dept'] = 'Sales'
print(Emp)

# ? WAP to add new students' roll numbers and marks in the dictionary M created with roll no. as keys and marks as values

M = {}
n = int(input("How many students :"))
for a in range(n):
    r , m = eval(input("Enter roll no. and marks : "))
    M[r] = m
    
print("Created Dictionary")
print(M)
# todo : making simple way to iterate over again as per user choice : 
ans = 'y'
while ans == 'y':
    print("Enter details of the new student :")
    r , m = eval(input("Roll no. and Marks : "))
    M[r] = m
    ans = input("More Students?(y/n) :")
print("Dictionary after adding new students : ")
print(M)

