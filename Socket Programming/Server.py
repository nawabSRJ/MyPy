import socket

s = socket.socket() 
print('Socket Created')

s.bind(('localhost' , 9999))

s.listen(3)     # at max 3 client connections 
print('Waiting for Connections...')

while True:
    c , addr = s.accept()   # to accept connections simultaneously and not one by one
    print('Connected with ', addr)
    while True:

        msg = c.recv(1024).decode()
        print(msg)
        if msg == '0':
            break

        c.send(bytes('Namastey','utf-8'))
    print('Client Disconnected')
    c.close()