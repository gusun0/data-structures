import socket
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM) #tcp
s.connect(('127.0.0.1', 55555))
msg = s.recv(1024)
s.close()
print(msg.decode())


