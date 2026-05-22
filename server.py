import socket

HOST = "127.0.0.1"
PORT = 5000

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
    server.bind((HOST, PORT))
    server.listen(1)

    print(f"Listening on {HOST}:{PORT}...")

    conn, addr = server.accept()

    with conn:
        print(f"Connected by {addr}")

        while True:
            data = conn.recv(1024)

            if not data:
                print("Client disconnected")
                break

            message = data.decode(errors="replace").strip()

            print("Received:", message)

            if message == "STOP":
                conn.sendall(b"Server shutting down\n")
                print("STOP command received")
                break

            conn.sendall(b"Message received\n")

print("Server exited")