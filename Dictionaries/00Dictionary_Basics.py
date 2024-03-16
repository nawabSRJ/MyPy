# dictionary is way of organizing elements in key : value pairs
# * dictionaries are MUTABLE

# * example : key -> name of teachers , value -> subjects taught

teachers = {"Shalini":"Data Structures","Rinku" : "Multimedia", "Amit" : "C++" , "Shweta" : "Operating System"}

# ! accessing elements :

print(teachers)
print(teachers["Amit"])         # * passing key
# print(teachers["Multimedia"])   # ! passing value ~ results in error

# ! -> Keys of a dictionary must be of IMMUTABLE TYPE ;     if you try to give mutable type as key then an ERROR will occur
# * so keys can only be immutable type that are : string, number, tuple

# ?-----------------------------------------------------------------------------------------

# todo : WAP to create to read roll numbers and marks of four students and create a dictionary from it having roll numbers as keys

rno = []
marks = []

for a in range(4):
    # * using 'eval' will help accept int and float values at the same time
    r = eval(input("Enter Roll Number :"))
    m = eval(input("Enter Marks :"))
    rno.append(r)
    marks.append(m)

dct = {rno[0] : marks[0],rno[1] : marks[1] , rno[2] : marks[2], rno[3] : marks[3]}
print("Created Dictionary : \n\n")
print(dct , type(dct))

# * accessing elements and their type 
print(dct[1] , type(dct[1]))
print(dct[2] , type(dct[2]))

# *********************************************************************

# todo - now consider dict dct and check if roll no. 2 has scored more than 75 or not

if dct[2] > 75 :
    print("Roll Number 2 scored ",dct[2],"(>75)")
else :
    print("Roll Number 2 scored ",dct[2], "(<75)")
    
