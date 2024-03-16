import customtkinter as ctk
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
from Algo import encrypt
import os
import mysql.connector
mydb = mysql.connector.connect(host = 'localhost',
                               user = 'root',
                               password = 'nawab.saxena18',
                               database = 'undercover')

cur = mydb.cursor()

class Info():
    '''Colors used : 
    #E45BA0 -> for buttons

    '''

class Undercover():

    def Encrypt(self , folderPath):
         # * getting data from the entry widgets
             
             self.FileName = self.fname.get()
            #  self.pincode = self.pin.get()   
             self.content = self.dataframe.get("1.0", "end-1c")
             self.content = ''.join(map(encrypt , self.content))
           
             # todo - create a file and put the encrypted data into that file
             # ! to store the file in the specified 'user' directory it is important to maintain:
             # * Create a directory as per requirement (user - based) -> (os module)  
             #  *Create a file in that directory and then write to it 
             #  * specify absolute file path in 'with - open' clause 

             self.file_path = os.path.join(folderPath, self.FileName)   # ? linking file with the folder path

             try:
                with open(self.file_path,'w') as f:
                    f.write(self.content) 
                    pass
             except Exception as e :
                  print('Some Exception Occured : ', e)
             else :
                  print(self.FileName)
                #   print(self.pincode)
                  messagebox.showinfo('Done','File Has been Created!!')
             finally:
                  self.NewFileWin.withdraw()
                  self.dashboard(self.name_var, folderPath)



    def NewFileEncryption(self , folderPath):
             self.dashboard_win.withdraw()
             self.NewFileWin = Toplevel(self.root)
             self.NewFileWin.geometry(self.root.geometry())

            #  todo - create entry widgets for file name and PIN
             self.fname = ctk.CTkEntry(self.NewFileWin, width = 725 ,
                                height = 25,
                                placeholder_text = 'File Name :',
                                corner_radius = 12,
                                state = 'normal',
                                font = ('Cambria',20),   # size of text ~ font attribute
                                border_width = 2,
                                border_color = 'black',
                                text_color = 'white',
                                
                                )

             self.fname.pack(pady = 15)

             self.pin = ctk.CTkEntry(self.NewFileWin, width = 725 ,
                                height = 25,
                                placeholder_text = 'PIN',
                                corner_radius = 12,
                                state = 'normal',
                                font = ('Cambria',20),   # size of text ~ font attribute
                                border_width = 2,
                                show = '*',
                                border_color = 'black',
                                text_color = 'white',
                                
                                )

             self.pin.pack(pady = 3)

             self.dataframe = ctk.CTkTextbox(self.NewFileWin , width = 900, height = 400,
                                           font = ('Arial',18),
                                           border_color = 'black',
                                           border_width = 4,
                                           fg_color = 'white',
                                           text_color = 'black',
                                           corner_radius = 2
                                           )
            
            #  self.dataframe.insert(0,'Type or Paste Here')
            #  self.dataframe.focus_set()
             self.dataframe.pack(pady = 7)

             self.encrypt_btn = ctk.CTkButton(self.NewFileWin , text = 'Encrypt Data',
                                text_color = 'black',
                                fg_color = '#7CB58A',
                                width = 200,
                                height = 60,
                                border_width = 0,
                                border_spacing = 2,
                                corner_radius = 12,
                                font = ('Arial',20),
                                command = lambda: self.Encrypt(folderPath)
)

             self.encrypt_btn.pack(pady = 10)

            



    # * good method for frame replacement
    def dashboard(self , name_var , folderPath):
        self.root.withdraw()  # Hide the login window
        self.dashboard_win = Toplevel(self.root)
        self.dashboard_win.geometry(self.root.geometry())  # Set size to match the login window
        self.dash_frame = ctk.CTkFrame(self.dashboard_win, fg_color='#fff')
        self.welcomeLabel = ctk.CTkLabel(self.dash_frame , 
                                         width = 400,
                                         height = 200,
                                         corner_radius = 12,
                                         fg_color = 'yellow',
                                         text = f'Welcome \n{name_var}',
                                         text_color = 'black',
                                         font = ('Arial',45,'bold'),
                                         padx = 0,
                                         pady = 2
                                         )
        self.welcomeLabel.place(x = 14 , y = 20)
        self.dash_frame.pack(fill=BOTH, expand=True)

        self.files_heading = ctk.CTkLabel(self.dashboard_win , text = 'Files :',
                                          fg_color = 'white',
                                          text_color = 'black',
                                          pady = 7,
                                          width = 40,
                                          height = 15,
                                          font = ('Arial',21)
                                          ) 
        self.files_heading.place(x = 15 , y = 230)


        

        self.newf_btn = ctk.CTkButton(self.dashboard_win , text = 'New File \nEncryption',
                                 width =  160,
                                 height = 70,
                                 border_width = 1,
                                 border_color = 'black',
                                 fg_color = '#E45BA0',
                                 bg_color = '#fff',
                                 text_color = 'black',
                                 font = ('Arial',24),
                                 corner_radius = 32,
                                 border_spacing = 2,
                                 command = lambda: self.NewFileEncryption(folderPath)
)
        self.newf_btn.place(x = 730 , y = 122)

        self.oldf_btn = ctk.CTkButton(self.dashboard_win , text = 'Old File \nEncryption',
                                 width =  160,
                                 height = 70,
                                 border_width = 1,
                                 border_color = 'black',
                                 fg_color = '#E45BA0',
                                 bg_color = '#fff',
                                 text_color = 'black',
                                 font = ('Arial',24),
                                 corner_radius = 32,
                                 border_spacing = 2
                                 )
        self.oldf_btn.place(x = 730 , y = 222)

        self.decrypt_btn = ctk.CTkButton(self.dashboard_win , text = 'Decrypt \nData',
                                 width =  160,
                                 height = 70,
                                 border_width = 1,
                                 border_color = 'black',
                                 fg_color = '#E45BA0',
                                 bg_color = '#fff',
                                 text_color = 'black',
                                 font = ('Arial',24),
                                 corner_radius = 32,
                                 border_spacing = 2
                                 )
        self.decrypt_btn.place(x = 730 , y = 322)
        
             

    def authenticate(self):
            self.found = None
            if self.username.get() == '':
                messagebox.showerror('Error','Please Enter Username to Proceed!!')
            else:
                self.name_var = self.username.get()
                # print('The username entered : ',self.name_var)
                # todo - make the logic to check the username from the database
                q = 'SELECT username FROM USERS'
                cur.execute(q)     
                self.result = cur.fetchall()    # ? fetches all the records from the user table
                print(self.result)
                for i in self.result:
                    t = i
                    if t[0] == self.name_var:
                        self.found = 1
                        break
                    else :
                         self.found = 0
                
                if self.found:
                     messagebox.showinfo('Confirm','Valid User')
                     # * folder name for the user is = the username 
                     self.foldername = self.name_var
                     self.folder_path = os.path.join(os.getcwd(), self.foldername)  # * building path of the folder to check if it exists in cwd

                     if os.path.exists(self.folder_path):
                          pass # * no need to create a folder for this user
                     else :
                          # Join the current working directory with the folder name
                          self.folder_path = os.path.join(os.getcwd(), self.foldername)
                          os.makedirs(self.folder_path)
        
          
                     self.dashboard(self.name_var , self.folder_path)

                else :
                      messagebox.showerror('Confirm','User Not Found')

                     



    def __init__(self):

        self.root = Tk()
        self.root.title('Undercover')
        self.root.geometry('1200x650')
        self.root.configure(bg = '#fff')
        #ctk.set_default_color_theme('green')    # ??
        #ctk.set_appearance_mode('dark')
        self.root.resizable(False,False)

        self.main_heading = ctk.CTkLabel(self.root, text = 'UNDERCOVER' , fg_color = 'white',
                                    text_color = 'black',
                                    pady = 10,
                                    padx = 5,
                                    width = 120,
                                    height = 45,
                                    font = ('Comic Sans MS',52))
                                    # font = ('Century Gothic',52))
                                    # font = ('Times New Roman',52))
        self.main_heading.pack()


        self.pic_frame = ctk.CTkFrame(self.root, width = 300 , height = 190, bg_color = 'white' ,
                                fg_color = 'white',
                                border_width = 0,
                                border_color = 'white')

        self.original_image = Image.open('pic2.png')

        # Resize the image to fit within the frame while maintaining aspect ratio
        width, height = 280, 210
        self.resized_image = self.original_image.resize((width, height),  Image.LANCZOS)

        # Convert the resized image to PhotoImage
        self.img = ImageTk.PhotoImage(self.resized_image)

        # Create a label inside the frame with the image
        self.label = Label(self.pic_frame, image=self.img, bg='white')
        self.label.place(relx=0.5, rely=0.5, anchor='center')

        self.pic_frame.pack(pady = 7)

        

         

        self.username = ctk.CTkEntry(self.root, width = 225 ,
                                height = 40,
                                placeholder_text = 'username',
                                corner_radius = 12,
                                state = 'normal',
                                font = ('Cambria',20),   # size of text ~ font attribute
                                border_width = 2,
                                border_color = 'black',
                                text_color = 'white',
                                
                                )

        self.username.pack(pady = 15)

        self.password = ctk.CTkEntry(self.root, width = 225 ,
                                height = 40,
                                placeholder_text = 'password',
                                corner_radius = 12,
                                state = 'normal',
                                font = ('Cambria',20),   # size of text ~ font attribute
                                border_width = 2,
                                show = '*',
                                border_color = 'black',
                                text_color = 'white',
                                
                                )

        self.password.pack(pady = 3)

        self.login_btn = ctk.CTkButton(self.root , text = 'Login',
                                text_color = 'white',
                                fg_color = 'black',
                                width = 100,
                                height = 40,
                                border_width = 0,
                                border_spacing = 2,
                                corner_radius = 12,
                                font = ('Arial',20),
                                command = self.authenticate)

        self.login_btn.pack(pady = 20)

        self.root.mainloop()



obj = Undercover()
