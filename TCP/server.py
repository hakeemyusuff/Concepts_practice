import socket
#create a TCP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#Bind socket to localhost on port 8080
server_address = ("127.0.0.1", 8080)
server_socket.bind(server_address)
print(f"[+] Server started on {server_address[0]}:{server_address[1]}")
#Listen for incoming communication
server_socket.listen(2) # 1 = how many connections to queue
print(f"[+] Waiting for a connection...")
#Accept a client connection(where TCP handshake happens)
connection, client_address = server_socket.accept()
print(f"[+] Connection established with {client_address}")
#Receive data from client
data = connection.recv(1024).decode("utf-8")
print(f"[+] Received from client: {data}")
#send a response back to client
response = "Message received, thank you!"
connection.send(response.encode("utf-8"))
print(f"[+] Response sent to client")
#close connection
connection.close()
#shutdown the server socket
server_socket.close()
