#!/usr/bin/env python3

# Server.

import socket

# set up socket object and bind to an IP and port
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 9999))

# Now listen for incomming connections
# 5 consecutive connections qued
s.listen(8)

# Create While Looop to await connection
while True:      #clientsocket is a socket object & wemwait for the client's IP  
    clientsocket, address = s.accept() 
    # print an f-string for debugging
    print(f"Connection from {address} successfull? or not?")
    
    # Send data to the client socket
    clientsocket.send(bytes("Sending data in Unicode Transformation Format 8-bit ", "UTF-8"))
    clientsocket.close()
    
   # Close the connection ^
