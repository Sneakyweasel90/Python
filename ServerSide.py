# Server application

import socket

# create the socket object

s = socket.socket()

server_ip = '127.0.0.1'

port = 12345  # Range of 0 to 65535

# Have the application bind the socket, so it is the only
# application listening on this IP/Port combination
s.bind((server_ip, port))

print("Binding the socket " + server_ip + ". " + str(port))


# Listen for incoming connections
s.listen()

while True:
    conn, addr = s.accept()

    print("Connection: " + str(conn))
    print("Address: " + str(addr))
    reply = ""

    while reply != "Good Bye":
        welcomeMessage = "What is your name?"
        conn.send(welcomeMessage.encode())
        response = conn.recv(1024).decode()
        print(response)

        if response == "Neil":
            reply = "Hi Neil, your cat is asleep"
        elif response == "quit":
            reply = "Good Bye"
            conn.close()
        else:
            reply = "Thanks for connecting " + response + "."
        conn.send(reply.encode())

        if reply == "Good Bye":
            conn.close()
