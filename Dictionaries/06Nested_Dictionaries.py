# You can dictionaries inside a dictionary , BUT
# * You can store a dictionary as a value only , inside a dictionary

# ? A Dict contains details of two workers with their names as keys and other details in the form of dictionary as value. WAP to print the workers' information in records format

Emp = {'john' : {'age' : 26,'salary' : 10000},'divya' : {'age' : 35,'salary' : 50000}}
for key in Emp :
    print("Employee",key,':')
    print('Age :'  ,str(Emp[key]['age']))
    print('Salary :'  ,str(Emp[key]['salary']))
for key in Emp :
    print("whatever")
    while(True):
        while(False):
            