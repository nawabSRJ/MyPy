# remember : if you open an existing file in write mode, your file will get overwritten else if file dosen't exist then it will be created

# f = open('newfile1.txt','w')
# f.write('Hi there, my name is Srajan \n This file is created by Python (used w mode)')
# f.close()   # most imp. step is to close a file after writing to it

# * Note : The escape sequence character are working (not getting printed as it is, rather functiong as they do on output window) 

# * Second Way -> where you don't have to explicitly close the file

with open('newfile2.txt','w') as f:
    f.write('Hi, i used "with" keyword this time to open and write to a file')

with open('newfile2.txt','r') as f:
    content = f.read()
    print(content)

