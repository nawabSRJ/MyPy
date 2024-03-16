# * source : tech with tim yt channel Socket Programming Python
import socket
import threading


PORT = 9999
FORMAT = 'utf-8'
DISCONNET_MSG = '0'
# SERVER = ""   put your IPv4 addr or just write below line to get it done automatically:
SERVER = socket.gethostbyname(socket.gethostname())
# print(SERVER) -> gives IPv4 address
ADDR = (SERVER , PORT)  # putting in tuple as it will go in binding parameters
server = socket.socket(socket.AF_INET , socket.SOCK_STREAM)  # what type of IP address are we going to looking for (IPv4) , STREAMING DATA THROUGH SOCKET
server.bind(ADDR)


# @to handle individual connections / this func will run concurrently for each client
def handle_client(conn, addr):
    print(f"New Connection {addr} Connected")
    connected = True
    while connected:
        try:
            msg = conn.recv(1024).decode(FORMAT)  # decode from byte to utf-8 format
            if not msg:
                break  # If empty message received, assume client disconnected
            print(f"[{addr}] : {msg}" , end='\n')
            # sui.print_msg(addr , msg)
            # print_msg(addr , msg)
            if msg == DISCONNET_MSG:
                print(f"[{addr}] : Disconnected")
                connected = False
        except ConnectionResetError:
            break  # If the connection is reset by the client, break the loop
    print('Client Disconnected')
    conn.close()


# @to handle / distribute new connections
def start():
    server.listen()
    print(f"Server is Listening on {SERVER}")
    while True:
        conn , addr = server.accept()
        thread = threading.Thread(target = handle_client , args = (conn ,addr))
        thread.start()
        # to see the active connection currently on the server
        print(f"[ACTIVE CONNECTIONS] {threading.active_count() - 1}")    # no. of threads(or clients) - 1 because of the start thread running always to listen to new connections
    input("Press any key to exit...")
    pass




print("Starting Server...")
start()



