import socket
import threading

HOST = "127.0.0.1"
PORT = 5555

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

username = input("Enter your username: ")

client.connect((HOST, PORT))


def receive_messages():
    while True:
        try:
            message = client.recv(1024).decode()

            if message == "USERNAME":
                client.sendall(username.encode())
            else:
                print(message, end="")

        except:
            print("\nDisconnected from server.")
            break


def send_messages():
    while True:
        try:
            message = input()

            if message.strip():
                full_message = f"{username}: {message}"
                client.sendall(full_message.encode())

        except:
            break


receive_thread = threading.Thread(target=receive_messages)
receive_thread.daemon = True
receive_thread.start()

send_messages()