import socket
import threading

HOST = "0.0.0.0"
PORT = 5555

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind((HOST, PORT))
server.listen()

clients = []
usernames = []


def broadcast(message, sender=None):
    for client in clients[:]:
        if client != sender:
            try:
                client.sendall(message.encode())
            except:
                remove_client(client)


def remove_client(client):
    if client in clients:
        index = clients.index(client)
        username = usernames[index]

        clients.remove(client)
        usernames.remove(username)

        try:
            client.close()
        except:
            pass

        print(f"{username} disconnected.")
        broadcast(f"{username} left the chat.\n")


def handle_client(client):
    while True:
        try:
            message = client.recv(1024).decode()

            if not message:
                break

            print(message)
            broadcast(message + "\n", client)

        except:
            break

    remove_client(client)


def receive_connections():
    print(f"Server started on port {PORT}")
    print("Waiting for connections...\n")

    while True:
        client, address = server.accept()

        client.sendall("USERNAME".encode())
        username = client.recv(1024).decode()

        clients.append(client)
        usernames.append(username)

        print(f"{username} joined from {address}")

        client.sendall(
            "Connected to the chat server!\n".encode()
        )

        broadcast(f"{username} joined the chat.\n", client)

        thread = threading.Thread(
            target=handle_client,
            args=(client,)
        )

        thread.daemon = True
        thread.start()


receive_connections()