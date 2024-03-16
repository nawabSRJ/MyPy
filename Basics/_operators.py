# *python is very versatile in assignment 
x , y = 10, 20
a=b=c= 25
print(x , y)
print(a,b,c)

# * Arithmetic Operators
print("\n\nArithmetic Operators\n\n")
p ,q = 10,5

print(p+q)
print(p-q)
print(p/q)
print(p*q)

print(p**q)     # *Exponentiation Operator

print(100/3)
print(100//3)       # *Floor Division Operator

print(10%3)     # * Modulus Operator

# * Augmented Assignment Operators
print("\n\nAugmented Assignment Operator\n\n")

r = 10
print("r initial value = ",r)
s = 2
r = r+s
print("r value after change = ",r)


print("s initial value = ",s)
s +=r
print("s value after change =",s)

# ! In Python we can combine the impact of an arithmetic operator with an assignment operator ~ Augmented Assignment Operator

r *= s
print(r)  


# * Relational Operators
print("\n\nRelational Operators\n\n")

o = 5
p = 10 - 5
print(r<s)
print(r>s)
print(o == p)
print(o != p)
print(o <= p)
print(o >= p)
print('a' == 'A')   # * Test for Case Sensitivity

# * Identity Operators
print("\n\nIdentity Operators\n\n")

a = 10
b = 10

print(a is b)   # ! returns True if both operands point to same memory location
print(a is not b)   # ! return True if both operands point to diff. memory location

# * can also use id() function to determine memory location

print(id(a) , id(b))
print(id(a) is id(b))
print(id(a) is not id(b))


# * or / and operators
t = 2
u = 1

# ! here relational expressions are treated as operands

if((a==b) and (t==u) == True) :
    print("Both are Equal")
else:
    print("One of them is unequal")
    
if((a==b) or (t == u) == True):
    print("At least one is equal")
else:
    print("both are unequal")
    
# * Chained Comparison Operators

print(11<13>12)
print(9>10<11)