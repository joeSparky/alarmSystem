import socket

HOST = "127.0.0.1"
PORT = 5000

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
    client.connect((HOST, PORT))

    while True:
        msg = input("Enter message: ")

        client.sendall(msg.encode())

        reply = client.recv(1024)
        print(reply.decode())

        if msg == "STOP":
            break