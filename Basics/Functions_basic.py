# writing a function to demonstrate type of arguments

def name(fname , lname = "Saxena"):  # *default Arguments
    print("Hello",fname,lname)

name("Srajan")
name("Stuti")
name("Shivam")

name("Arush","Tiwari")  # * default arg. will be overriden by function calling arg

# !------------------------------------------------------------------------------

# * taking tuple as function arguments and unpacking it inside the funciton using asterisk(*) operator

def average(*numbers):
    sum = 0
    for i in numbers:
        sum = sum + i
    print("Average is = ",sum/ len(numbers))

average(5,5)
average(5,5,2)