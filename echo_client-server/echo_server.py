import socket

addr = ("0.0.0.0", 4444)

with socket.socket() as s:
    s.bind(addr)
    s.listen()
    print("Server is started...")
    conn, addr = s.accept()
    print("client = {}:{}".format(addr[0], addr[1]))

    data = conn.recv(1024)
    conn.send(data)
    print(data.decode())