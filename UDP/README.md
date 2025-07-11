# UDP Communication Demo

This folder contains a simple client-server demo using **UDP (User Datagram Protocol)** in Python.

## 💡 What It Covers

- Creating a connectionless UDP socket
- Sending multiple messages with `sendto()` and receiving with `recvfrom()`
- Using **Wireshark** to visualize how UDP transmits data without handshakes or ACKs
- Understanding **speed vs reliability** trade-offs

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
tcp.port == 1234
```

## 📄 Files

- `server.py`: listens for incoming datagrams
- `client.py`: sends multiple messages rapidly

## 📚 Concepts Practiced

- Connectionless communication
- Datagram-based message sending
- Real-world use cases: video calls, DNS, games, etc.
