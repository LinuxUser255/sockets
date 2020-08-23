#!/usr/bin/env python3

# Server

import socket
import threading

HEADER = 64 #message byte length 
PORT = 4444
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "Connection terminated."


# the server's socket object:
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

#Handle connections & comunications between server & client
def handle_coms(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected.")

    connected = True
    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT)
        msg_length = int(msg_length)
        msg = conn.recv(msg_length).decode(FORMAT)
        if msg == DISCONNECT_MESSAGE:
            connected = False
        print(f"[{addr}] {msg}")


# Initiate the socket server & listen for incoming connections
# The begin thread is allways running
def begin():
    server.listen()
    # What IP address are we connected to?
    print(f"[LISTENING] Server is listening on {SERVER}")
    while True:
        conn, addr = server.accept()#This line waits on a new connection
        thread = threading.Thread(target=handle_coms, args=(conn, addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.activeCount() -1}")
        # the number of active threads = ammount of clients conn
        # because the start thread is allways running then the count begins at -1 (subtract 1)

begin()
