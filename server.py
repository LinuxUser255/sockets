#!/usr/bin/env python3

# Basic Server
# Socket Object: socket.socket(socket.AF_INET, socket.SOCK_STREAM)

import socket
import threading


HEADER = 64 #message byte length (buffer overflow vuln??)
PORT = 4444
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!CLOSE CONNECTION!"


# the server's socket object:
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected.")

    connected = True
    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT)
        msg_length = int(msg_length)
        msg = conn.recv(msg_length).decode(FORMAT)
        if msg == DISCONNECT_MESSAGE:
            connected = False
        print(f"[{addr}] {msg}")


# Begin listening to connections and passing them
def start():
    server.listen()
    # What IP address are we connected to?
    print(f"[LISTENING] Server is listening on {SERVER}")
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.activeCount() -1}")
        # the number of active threads = ammount of clients conn
        # because the start thread is allways running then the count begins at -1 (subtract 1)


#print("Server is listening for active connections.. ")
start()

