import socket

# Define the login and password
LOGIN = "myusername"
PASSWORD = "mypassword"

# Create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to a public host and a well-known port
server_socket.bind(('0.0.0.0', 1234))

# Listen for up to 4 connections
server_socket.listen(4)

# Accept connections from clients
while True:
    # Wait for a client to connect
    client_socket, address = server_socket.accept()

    # Prompt the client for login and password
    client_socket.sendall(b"Login: ")
    login = client_socket.recv(1024).decode().strip()
    client_socket.sendall(b"Password: ")
    password = client_socket.recv(1024).decode().strip()

    # Check if the login and password are correct
    if login == LOGIN and password == PASSWORD:
        # Send a welcome message to the client
        client_socket.sendall(b"Welcome to the server!\n")
    else:
        # Send an error message to the client and close the connection
        client_socket.sendall(b"Invalid login or password.\n")
        client_socket.close()