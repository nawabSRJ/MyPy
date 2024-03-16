# names = [[1,"Anshika Nagvanshi",None],[2,"Srajan Saxena"],[3,"Priyanshu Batham"],[4,"Utkarsh Rana"],[5,"Pratham Gupta"]]
# print(names[0][2])

# * Actual Code

names = [[1,"Anshika Nagvanshi"],[2,"Srajan Saxena"],[3,"Priyanshu Batham"],[4,"Utkarsh Rana"],[5,"Pratham Gupta"]]

def mark_att():
        
       for i in range(1,5):
         ent_id = int(input("Enter ID No. : "))
         if(ent_id == 0):
             break;
         elif(ent_id > 0 and names[i][0] == ent_id):
              names[i].append("Present")

mark_att()
print(names)