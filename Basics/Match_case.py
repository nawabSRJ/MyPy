# * program to showcase working of match case statements in python
# * match case in python is similar to switch case in other languges like Java , C++ etc.

num = int(input("Enter value : \t"))

match num :
    case 1:
        print('One')
    case 3:
        print('Three')
    case 10:
        print("Ten")
    case _ if num>10 and num < 15:  # * for specification use '_ if'
        print("Greater than Ten")
    case _ if num>15 and num <20:
        print("More than 15 and less than 20")
    case _:                         # * for default case, if no case matched
        print("More than 20")