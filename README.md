# Real-Time Chat Application

A simple real-time chat application built using Python socket programming and multithreading. The application uses a client-server architecture that allows multiple users to communicate with each other in real time.

## Features

- Real-time messaging
- Multiple client support
- Username-based chat
- Client-server architecture
- Multiple users can connect simultaneously
- Server displays connected users and messages
- Users are notified when someone joins or leaves the chat
- Multithreading for handling multiple clients

## Technologies Used

- Python
- Socket Programming
- TCP/IP
- Multithreading
- Git
- GitHub

## Project Structure

```text
chat-application
│
├── server.py
├── client.py
├── README.md
├── .gitignore
└── screenshots/
    ├── server.png
    ├── client1.png
    └── client2.png
## How It Works

The application follows a client-server architecture.

The server listens for incoming client connections and manages multiple connected users.

Each client connects to the server using a TCP socket and provides a username. Messages sent by one client are forwarded by the server to the other connected clients.

Multithreading allows the server to handle multiple users at the same time.

## How to Run
1. Start the Server

Open a terminal in the project folder and run:

python server.py

The server will start listening on port 5555.

2. Start the First Client

Open another terminal:

python client.py

Enter a username when prompted.

3. Start Another Client

Open a third terminal:

python client.py

Enter another username.

Both clients can now exchange messages in real time.

Example
Client 1:
Alex: Hello, Sam

Client 2:
Alex: Hello, Sam
Sam: Hey, Alex
Screenshots
Server

Client 1

Client 2

## Future Improvements
Graphical user interface
Private messaging
Message timestamps
Chat rooms
User authentication
Message history
File sharing

```
