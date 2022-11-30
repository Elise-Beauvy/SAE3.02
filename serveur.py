import socket
import csv

def serv():
    msgserveur = ""
    msgclient = ""

    host = socket.gethostname()
    host="127.0.0.1"

    with open('hostname.csv', 'w', newline='') as hostname:
        writer = csv.writer(hostname)
        writer.writerow([host])

    server_socket = socket.socket()
    server_socket.bind((host,10110))
    server_socket.listen(1)
    while msgserveur != "kill" and msgserveur != "reset":
        conn, address = server_socket.accept()
        while msgserveur != "disconnect" and msgserveur != "kill" and msgserveur != "reset":
            msgclient = conn.recv(1024).decode()
            print(msgclient)
            msgserveur = input("Serveur1:")
            conn.send(msgserveur.encode())
        conn.close()
    server_socket.close()
    print("socket serveur fermé")
serv()