import socket

# create a socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server_address = ("127.0.0.1", 1234)

# send data to server
messages = [
    "Hello",
    "so you don't really need a connection",
    "this might get lost",
    "but you're kinda fast",
    "There is use for you in some places",
]

for message in messages:
    client_socket.sendto(message.encode("utf-8"), server_address)
