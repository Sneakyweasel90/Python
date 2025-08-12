# Client Application

import socket

# Create the socket object

s = socket.socket()

server_ip = '127.0.0.1'

port = 12345  # Range of 0 to 65535


print("Connecting to database " + server_ip + ":" + str(port))
s.connect((server_ip, port))

myName = ""
while myName != "quit":
    print(s.recv(1024).decode())
    myName = input()

    s.send(myName.encode())

    print(s.recv(1024).decode())
