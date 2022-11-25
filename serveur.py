import socket

msgsrv = ""
msgcl = ""

host = socket.gethostname()
print(host)
server_socket = socket.socket()
server_socket.bind((host,10000))
server_socket.listen(1)
while msgcl != "arret" and msgsrv != "arret":
    conn, address = server_socket.accept()
    while msgcl != "bye" and msgsrv != "bye" and msgcl != "arret" and msgsrv != "arret":

        msgcl = conn.recv(1024).decode()
        print(msgcl)
        msgsrv = input("Isis:")
        conn.send(msgsrv.encode())
    conn.close()
server_socket.close()
