''' The list containing the questions has the correct answer no. at the last index of each nested list
answer : [-1] position of nested list 
question : [0] position of the nested list
'''



ques = [["Who won the ICC Men's Cricket World Cup in 2011?" ,"Australia" , "India" ,"England","New Zealand",2],["Who was elected as the Prime Minister of India in 2014?","Narendra Modi","Kehsav Modi","Prithiviraj Chauhan","Maharaj Dogesh",1],["Who is known as the Iron Man of India","Sardar Vallabhbhai Patel","Amit Shah","Amitabh Bachchan","Ranu Mandal",1],["Which is the World's first Lunar Mission to land on South Polar region of Moon","Luna 69","Chandrayaan 3","Apollo 69","Shiv Shakti",2],["Which Indian Movie reachded to Oscars 2023?","RRR","Pathaan","Jawan","Baaghi",1],["How many cores are there in intel i5?","1","2","3","5",4],["Which Country won the ICC Men's Cricket World Cup in 2015?","India","Australia","America","New Zealand",2]]

levels = [1000,2000,3000,4000,5000,6000,7000]
money = 0

for i in range(len(ques)):
    question = ques[i]
    print(f"Question for Rs. {levels[i]}\n")
    print(question[0])
    print(f"A.{question[1]}\tB.{question[2]}\nC.{question[3]}\tD.{question[4]}\n")
    try :
        reply = int(input("Enter your answer(1-4) \t\n Enter -1 to Quit"))
        if(reply == -1):
            break
        if(reply == question[-1]):
            print(f"Correct Answer, You have won Rs. {levels[i]}")
            money += levels[i]
        else:
            print("Wrong Answer")
            break
    except ValueError:
        print("Please Enter a Number between 1-4")
        
print(f"Your Total Dhan Rashi is = {money}")