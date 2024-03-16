import math
print(math.ceil(1.5))
print(math.floor(1.5))   

print(math.sqrt(25))    # * for square root

# * math.fabs() returns absolute value 
print(math.fabs(1.25))
print(math.fabs(-1))
print(math.fabs(-5.2))
print(math.fabs(-7))

print("Natural Log ? ->",math.log(1024))  # * math.log(num,base)
print("with base ->",math.log(1024 , 2))
print(math.log10(1))    # * gives base 10 logarithm for 1

print(math.pow(10,2))  # * exponent ,  math.pow(base,exponent)
print(math.exp(2))     # * exponent of e ~ math.exp(arg) will give e^2

print(math.sin(0))  # * math.sin(arg) returns sin of arg, value of arg must be in radians
print(math.sin(90))  # * math.sin(arg) returns sin of arg, value of arg must be in radians
print(math.cos(0))
print(math.cos(90))
print(math.tan(45))

print(math.degrees(3.14)) # * converts angle from radians to degrees
print(math.radians(179.91)) # * converts angle from degrees to radians

print("\n\n")
print(math.pi)
print("\n\n")

# ! Question - Radius of Sphere = 7.5 m , calculate area and volume of sphere
# ! area = pie * r * r    ;   volume = 4 * pi * r * r * r

r = 7.5
area = math.pi * r * r
volume = 4 * math.pi * math.pow(r, 3)

print("Area of Sphere = ", area)
print("Volume of Sphere = ", volume)


