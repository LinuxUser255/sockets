#!/usr/bin/env python3

# Client socket example 2

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 9999))

all_data = ' '
while True:
    data = s.recv(8)
    if len(data) <= 0:
        break
    full_data += data.decode("utf-8")
    print(data.decode("utf-8")) 

print(all_data)
