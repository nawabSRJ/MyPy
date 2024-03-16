''' The list containing the questions has the correct answer no. at the last index of each nested list
answer : [-1] position of nested list 
question : [0] position of the nested list
options : [1:4] position of the nested list
'''
from tkinter import *
import customtkinter as ctk
from tkinter import messagebox
win = Tk()
win.geometry('1100x600')
win.resizable(False,False)
win.title('Kaun Banega Crorepati')

ques = [["Who won the ICC Men's Cricket World Cup in 2011?" ,"Australia" , "India" ,"England","New Zealand",2],["Who was elected as the Prime Minister of India in 2014?","Narendra Modi","Kehsav Modi","Prithiviraj Chauhan","Maharaj Dogesh",1],["Who is known as the Iron Man of India","Sardar Vallabhbhai Patel","Amit Shah","Amitabh Bachchan","Ranu Mandal",1],["Which is the World's first Lunar Mission to land on South Polar region of Moon","Luna 69","Chandrayaan 3","Apollo 69","Shiv Shakti",2],["Which Indian Movie reachded to Oscars 2023?","RRR","Pathaan","Jawan","Baaghi",1],["How many cores are there in intel i5?","1","2","3","5",4],["Which Country won the ICC Men's Cricket World Cup in 2015?","India","Australia","America","New Zealand",2]]
money = 0
# def ansPressed(answer):
#     if(answer == correctAns):
#         # print("Correct Answer") 
#         messagebox.showinfo("Result","Correct Answer")

#     else :
#         # print("Incorrect Answer")
#         messagebox.showinfo("Result","Incorrect Answer")

        
        
    
# correctAns = None
name = Label(text = 'Kaun Banega Crorepati', font=('Microsoft YaHei UI Light',32,'bold'))
name.pack()
qframe = Frame(win, width = 800, height=120,bg = 'blue')
qframe.place(x = 150 , y = 100)

def ansPressed():
    for i in range(len(ques)):
        global correctAns
        question = ques[i]
        currQuestion = question[0]
        correctAns = question[-1]
        qlabel = Label(qframe , text = f'{currQuestion}' , font=('Microsoft YaHei UI Light',12,'bold'))
        qlabel.pack()

# * -------------------------- Side Bar

sideframe = ctk.CTkFrame(win , width = 165, height = 400 , bg_color = 'black')
# sideframe.grid(row = 2, column = 0, rowspan = 10, columnspan = 4)
sideframe.place(x = 0 , y = 4)



# * ------------------------ Options Frame ------------------------------
op1 = Frame(win,width = 210 , height = 51,bg = 'blue')
op1.place(x = 240 , y = 320)
op1But = ctk.CTkButton(op1, text = 'Answer 1' , width = 200 , height = 35,font=('Microsoft YaHei UI Light',12,'bold'),border_color = "black" , corner_radius = 10, border_width = 3, bg_color = "white" , fg_color = "purple", command = ansPressed)
op1But.pack()

op3 = Frame(win, width = 210 , height = 51,bg = 'blue')
op3.place(x = 240 , y = 400)
op3But = ctk.CTkButton(op3, text = 'Answer 3' , width = 200 , height = 35,font=('Microsoft YaHei UI Light',12,'bold'),border_color = "black" , corner_radius = 10, border_width = 3, bg_color = "white" , fg_color = "purple", command = ansPressed)
op3But.pack()

op2 = Frame(win, width = 210 , height = 51,bg = 'blue')
op2.place(x = 600 , y = 320)
op2But = ctk.CTkButton(op2, text = 'Answer 2' , width = 200 , height = 35,font=('Microsoft YaHei UI Light',12,'bold'),border_color = "black" , corner_radius = 10, border_width = 3, bg_color = "white" , fg_color = "purple", command = ansPressed)
op2But.pack()


op4 = Frame(win, width = 210 , height = 51,bg = 'blue')
op4.place(x = 600 , y = 400)
op4But = ctk.CTkButton(op4, text = 'Answer 4' , width = 200 , height = 35,font=('Microsoft YaHei UI Light',12,'bold'),border_color = "black" , corner_radius = 10, border_width = 3, bg_color = "white" , fg_color = "purple", command = ansPressed)
op4But.pack()

win.mainloop()
