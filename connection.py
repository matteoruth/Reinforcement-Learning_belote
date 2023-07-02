import socket

# Define the server address and port
SERVER_ADDRESS = '127.0.0.1'
SERVER_PORT = 1234

# Define the login and password
LOGIN = "myusername"
PASSWORD = "mypassword"

# Create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
client_socket.connect((SERVER_ADDRESS, SERVER_PORT))

# Send login and password to the server
client_socket.sendall(LOGIN.encode())
client_socket.sendall(b"\n")
client_socket.sendall(PASSWORD.encode())
client_socket.sendall(b"\n")

# Receive the server's response
response = client_socket.recv(1024).decode()

# Print the server's response
print(response)

# Close the connection
client_socket.close()