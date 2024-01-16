import socket
client = socket.socket()
client.connect(('127.0.0.1',10295))
client.sendall((input()).encode('utf-8'))
print(client.recv(1024).decode())