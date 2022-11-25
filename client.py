import socket

msgcl = ""
msgsrv = ""

host = socket.gethostname()
print(host)
client_socket = socket.socket()
client_socket.connect((host,10000))

hostname = socket.gethostbyaddr("192.168.43.2")
print(hostname)

msgcl = input("Amon:")
client_socket.send(msgcl.encode())
msgsrv = client_socket.recv(1024).decode()
print(msgsrv)
client_socket.close()
