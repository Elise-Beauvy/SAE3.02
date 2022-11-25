import socket

msgcl = ""
msgsrv = ""

host = socket.gethostname()
print(host)
client_socket = socket.socket()
client_socket.connect(("127.0.0.1",80))

while msgcl != "bye" and msgsrv != "bye" and msgcl != "arret" and msgsrv != "arret":
    msgcl = input("Amon:")
    client_socket.send(msgcl.encode())
    msgsrv = client_socket.recv(1024).decode()
    print(msgsrv)
client_socket.close()
