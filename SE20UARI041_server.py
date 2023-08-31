import socket

# Server configuration
server_ip = "122.184.65.228"
server_port = 3000

# Create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the server address
server_socket.bind((server_ip, server_port))

# Listen for incoming connections
server_socket.listen()

print("Server is listening on {}:{}".format(server_ip, server_port))

# Accept a connection from a client
client_socket, client_address = server_socket.accept()
print("Connection established with:", client_address)

while True:
    # Receive data from the client
    data = client_socket.recv(1024).decode("utf-8")
    if not data:
        break
    print("Received from client:", data)

    # Send a response back to the client
    response = "Server received: " + data
    client_socket.send(response.encode("utf-8"))

# Close the connection
client_socket.close()
server_socket.close()
