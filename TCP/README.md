# Transmission Control Protocol(TCP)

# TCP Communication Demo

This folder contains a simple client-server implementation using **TCP (Transmission Control Protocol)** in Python.

## 💡 What It Covers

- Setting up a TCP server and client using the `socket` module
- Establishing a **3-way handshake**
- Observing **ACKs**, **PSH**, and **FIN** for data transmission and teardown
- Using **Wireshark** to inspect how TCP works behind the scenes
- Exploring reliable, ordered, connection-oriented communication

## 🚀 How to Run

1. Open one terminal and run the server:

```bash
python3 server.py
```

;
2. Open another terminal and run the client:

```bash
python3 client.py
```

;
3. (Optional) Open Wireshark and filter by:

```bash
tcp.port == 8080
```

## 📄 Files

- `server.py`: starts a TCP server that listens for a connection
- `client.py`: connects to the server and sends multiple messages

## 📚 Concepts Practiced

- Sockets and ports
- OSI model behaviour(Layer 4: Transport)
- TCP teardown and packet flags(SYN, ACK, FIN, etc)
