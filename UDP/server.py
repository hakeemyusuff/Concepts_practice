import socket

# create a socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# bind  socket to an address
server_address = ("127.0.0.1", 1234)
server_socket.bind(server_address)
print(f"[+] Server started on {server_address[0]}:{server_address[1]}")

while True:
    data, client_address = server_socket.recvfrom(1024)
    print(f"[+] Received data: '{data.decode("utf-8")}' from client: {client_address}.")

server_socket.close()