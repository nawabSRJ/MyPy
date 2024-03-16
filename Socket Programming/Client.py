import socket

c = socket.socket()

c.connect(('localhost',9999))
msg = ''
while True:
    msg = input('Enter Message : ')
    c.send(bytes(msg , 'utf-8'))
    if msg == '0':
        break
    #print(c.recv(1024).decode())    # decode() is used to just print the string format with no prefixes of bytes


