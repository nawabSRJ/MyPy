# Write a Menu Driven Program to add , delete and display the inventory of Stationary

class Inventory:
    def __init__(self,total_pens,total_copy):
        self.TotalPens = total_pens
        self.TotalCopy = total_copy
    
    def add(self):
        q = input('What do you want to add?\n1->Pens\n2->Copy\nYour Choice : ')
        extra = int(input('How many units to add?\t'))
        match q:
            case 1:
                self.TotalPens += extra
                self.display(2) # * to show net units left after add/delete
            case 2:
                self.TotalCopy += extra
                self.display(1) # * to show net units left after add/delete
    def delete(self):
        q = input('What do you want to delete?\n1->Pens\n2->Copy\nYour Choice : ')
        deduct = int(input('How many units to delete?\t'))
        match q:
            case 1:
                self.TotalPens -= deduct
                self.display(2) # * to show net units left after add/delete
            case 2:
                self.TotalCopy -= deduct
                self.display(1) # * to show net units left after add/delete
    def display(self , q):        
        match q:
            case 1:
                ch = input('Which Item to display?\n1->Copy\n2->Pens\nChoice : \t')
                if ch == 1:
                    print(f'Total Copies are {self.TotalCopy}')
                elif ch == 2:
                    print(f'Total Pens are {self.TotalPens}')
            case 2:
                print(f'Total Copies are {self.TotalCopy}')
                print(f'Total Pens are {self.TotalPens}')
    
# ob = Inventory(10,5)
# q = input('What would you like to perform?\n1->Add\n2->Delete\n3->Display\nChoose : \t')

# match q:
#     case 1:
#         ob.add()
#     case 2:
#         ob.delete()
#     case 3:
#         q = input('Display : \n1->Item Wise\n2->Complete Inventory')
#         ob.display(q)
ob = Inventory(10, 5)
again = 'y'
while again == 'y':
    q = input('What would you like to perform?\n1->Add\n2->Delete\n3->Display\nChoose : \t')
    if  q == 1:
        ob.add()
    elif q == 2:
        ob.delete()
    elif q == 3:
        q = input('Display :\n1->Item Wise\n2->Complete Inventory')
        ob.display(q)
    again = input('Perform another operation? (y/n): ')

        