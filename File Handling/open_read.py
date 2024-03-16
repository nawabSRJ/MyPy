f = open('myfile.txt', 'r')
# print(f)
text = f.read()
print(text)
f.close()   # ! imp. step , don't forget
# * remember before executing this code -> vs code should be opened in the same directory as the file that you are trying to acces (to read) , or else you need to specify the absolute path

# todo - reading a file present in some other directory

f = open('D:\Srajan\Python\myfile2.txt', 'r')
text = f.read()
print(text) # * Successful

# Note : Since i specified the absolute address, i can now read any file present in different directories

