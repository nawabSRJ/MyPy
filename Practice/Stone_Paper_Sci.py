'''Press 1 for Stone 
2 for Paper
3 for Scissor '''
import random
print(__doc__)
comp = random.randint(1,3)
user = int(input("Enter Number :\n"))

match user:
    case 1 :
        if(comp == 2):
            print("You loose , Computer Won")
        elif(comp == 3):
            print("You Won")
        else:
            print("Draw")
    case 2:
        if(comp == 1):
            print("You Won")
        elif(comp == 3):
            print("You Loose , Computer Won")
        else :
            print("Draw")
    
    case 3:
        if(comp == 1):
            print("You Loose , Computer Won")
        elif(comp == 2):
            print("You Won")
        else :
            print("Draw")
    


        