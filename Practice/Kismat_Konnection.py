import random

name = input("Enter Your Full Name :\n")
dob = input("Enter you DOB : \n")
rashi = input("Enter Your Rashi : \n")

print("Your Card Number : ", random.randrange(6))

cnum = int(input("Enter your card Number:\n"))
if(cnum == 0):
    print("Be safe from fraud people, you may get fooled")
elif(cnum == 1):
    print("Your are going to find a NEW JOB very Soon")
elif(cnum == 2) :
    print("Best time for you to start a business")
elif(cnum == 3):
    print("High Possibility of finding Love")
elif(cnum == 4):
    print("You may loose your job, be careful")
elif(cnum == 5):
    print("You will loose money, you can go bankrupt as well")

    


