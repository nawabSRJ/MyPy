class Student:
    def __init__(self,roll,name,mark) -> None:
        self.RollNo = roll
        self.Name = name
        self.Marks = mark   # pass a list containing marks of 3 subjects

    def result(self):
        # total = sum(self.Marks)
        # percentage = self.total / 3
        print('Name : ',self.Name)
        print('Roll No. : ',self.RollNo)
        print('Marks : ',self.Marks)
        # print('Total : ',total)
        # print('Total : ',percentage)

stu_name = input('Enter Name of Student :')
stu_roll = int(input('Enter Roll No. of Student : '))
# stu_marks = list(input('Enter Marks List'))
stu_marks = int(input('Enter Marks '))

obj = Student(stu_roll,stu_name,stu_marks)
obj.result()   # displaying the details
