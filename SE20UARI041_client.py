import socket

# Server configuration
server_ip = "122.184.65.228"
server_port = 3000

# Create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
client_socket.connect((server_ip, server_port))
print("Connected to server")

while True:
    # Get user input
    message = input("Enter a message to send: ")

    # Send the message to the server
    client_socket.send(message.encode("utf-8"))

    # Receive the response from the server
    response = client_socket.recv(1024).decode("utf-8")
    print("Server response:", response)

    if message.lower() == "exit":
        break

# Close the connection
client_socket.close()
