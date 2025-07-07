import socket
#Create a TCP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ("127.0.0.1", 8080)
#connect to the server address and intitiate the TCP 3-way handshake
client_socket.connect(server_address)
print(f"[+] Connected to server at {server_address[0]}:{server_address[1]}")
#Send a message to the server
message = "Hello Server, It's your favourite backend engineer."
client_socket.send(message.encode("utf-8"))
print("[+] Message sent.")
#Receive response from server
response = client_socket.recv(1024).decode("utf-8")
print(f"[+] Server responded with: {response}")
#Cloxd the connection
client_socket.close()
print("[+] Connection closed")
