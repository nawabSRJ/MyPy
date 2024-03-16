import socket
# from Server2 import PORT , FORMAT , DISCONNET_MSG , SERVER

FORMAT = 'utf-8'
DISCONNET_MSG = '0'
SERVER = socket.gethostbyname(socket.gethostname())
# SERVER = "192.168.29.67"    # my lenovo ideapad
# print(SERVER)
PORT = 9999
ADDR = (SERVER ,PORT)
client = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
client.connect(ADDR)


def send():
    connected = True
    while connected:
        msg = input('Enter a message :')
        message = msg.encode(FORMAT)
        client.send(message)
        if message == DISCONNET_MSG:
            print('Disconnecting...')
            break
    

def send_manually(msg):
    message = msg.encode(FORMAT)
    client.send(message)
    if message == DISCONNET_MSG:
            print('Disconnecting...')
            client.close()

    


# send_manually('Namastey')
if __name__ == '__main__':
     send()
# send('Namastey')
# send('Srajan here!!')
# send(DISCONNET_MSG)

client.close()

