import socket
import threading

HOST = "0.0.0.0"
PORT = 5555

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()

clients = []
usernames = []


def broadcast(message, sender=None):
    for client in clients:
        if client != sender:
            try:
                client.send(message)
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

        broadcast(f"{username} left the chat.\n".encode())


def handle_client(client):
    while True:
        try:
            message = client.recv(1024)

            if not message:
                break

            broadcast(message, client)

        except:
            break

    remove_client(client)


def receive_connections():
    print(f"Server started on port {PORT}")
    print("Waiting for connections...\n")

    while True:
        client, address = server.accept()

        client.send("USERNAME".encode())
        username = client.recv(1024).decode()

        clients.append(client)
        usernames.append(username)

        print(f"{username} connected from {address}")

        client.send("Connected to the chat server!\n".encode())

        broadcast(f"{username} joined the chat.\n".encode(), client)

        thread = threading.Thread(target=handle_client, args=(client,))
        thread.start()


receive_connections()