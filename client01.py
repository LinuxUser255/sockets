#!/usr/bin/env python3

# Python socket programs pass data 
# Basic example of a client using the socket object

import socket


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# The server binds
# The client connects. The gethostname() is unique to this example
# Because this client-server demo is taking place on the same machine. Local host.
s.connect((socket.gethostname(), 4444))

# Accept data byte stream sent using a specified buffer size
data = s.recv(4096)
print(data.decode("utf-8")) # decode the bytes
