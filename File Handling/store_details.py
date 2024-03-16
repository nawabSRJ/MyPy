# Create a file student that stores the details of the studens
# todo - create a list of tuples to store data : Name , ID , CGPA , course
with open('Student.txt','w') as f:
    f.writelines(['Id\t','Name\t','CGPA\t',' Course'])
    f.write('\n--------------------------------------------------------------')

while True :
    stu_data = []
    Name = input("Enter the Name : ")
    Id = int(input("Enter the ID of the student :"))
    cgpa = int(input("Enter the CGPA of the student : "))
    course = input("Enter the Course : ")
    # stu_data.append((Name , Id , cgpa , course))
    stu_data = (Name , str(Id) , str(cgpa) , course)
    with open('Student.txt','a') as f:
        f.write("\n")
        # f.writelines(stu_data)
        f.write('\t'.join(stu_data))
    q = input('Would you like to continue? (Y/N)')
    if q == 'y' or q == 'Y':
        continue
    else:
        break

