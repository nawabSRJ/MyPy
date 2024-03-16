# here is the question
# ! Create a program capable of displaying questions to the user like KBC
# ! Use list data type to store questions and their correct answers
# ! Display the final amount the person is taking home after playing the game

q_list = ["Capital of India?","Ceo Of Alphabet Inc?","Founder of Amazon?","Who is the Designer of Indian Flag?"]

a_list = ["Delhi","Sundar Pichai","Jeff Bezos","Shri Pingali Venkayya"]

total_q = len(q_list)
total_correct = 0


for q in range(total_q):
    question = q_list[q]
    print(question)
    answer = input()
    if(answer == a_list[q]):
        print("Correct Answer")
        total_correct += 1
    else :
        print("Wrong Answer")
        break
    
amount_won = total_correct * 10000
print("You won =",amount_won)


# ?why is python program giving error when i type for q in q_list & not when i write for q in range(total_q) -> the error is in line q_list[q] , list indices can only be int not str



