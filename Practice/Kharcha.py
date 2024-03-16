# this is the front end of kharcha project
# * MENU 
def menu():
    print("What would you like to do :\n")
    print("1.Create Table Item\n2.Update Table(Insert Only)\n3.Display Table")
    print("\n\nEnter Choice : \t")

menu()
choice = int(input())   # * Specifying 'int' is important else the match case won't get executed as it will consider your choice as <str>

match choice:
    case 1:
        print("Here a new Table will be Created")
        print("Learning Now!!")
    case 2:
        print("Insertion of a new Item in any of the Tables will happen here")
    case 3:
        print("Here you will be able to see the stats related to your kharcha")
    case _:
        print("Please Enter a Valid Number")
