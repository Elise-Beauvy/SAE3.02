import socket

msgsrv = ""
msgcl = ""

host = socket.gethostname()
print(host)
server_socket = socket.socket()
server_socket.bind((host,25))
server_socket.listen(1)
conn, address = server_socket.accept()

msgcl = conn.recv(1024).decode()
print(msgcl)
msgsrv = input("Isis:")
conn.send(msgsrv.encode())
conn.close()
server_socket.close()
