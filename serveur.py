import socket
import csv

host = "127.0.0.1"

with open('hostname.csv', 'w', newline='') as hostname:
    writer = csv.writer(hostname)
    writer.writerow([host])
import socket

def serveur():
    msg = ""
    conn = None
    server_socket = None
    while msg != "kill" :
        msg = ""
        server_socket = socket.socket()
        """ options qui permette de réutiliser l'adresse et le port rapidement"""
        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
# l'adresse 0.0.0.0 permet d'écouter toutes les IP de la machine, localhost, locale comme publique
        server_socket.bind(("0.0.0.0", 10111))

        server_socket.listen(1)
        print('Serveur en attente de connexion')
        while msg != "kill" and msg != "reset":
            msg = ""
            msgsrv = ""
            try :
                conn, addr = server_socket.accept()
                print (addr)
            except ConnectionError:
                print ("erreur de connection")
                break
            else :
                while msg != "kill" and msg != "reset" and msg != "disconnect":
                    msg = conn.recv(1024).decode()
                    print ("réception du client: ", msg)
                    msg_srv = str(input("Serveur:"))
                    conn.send(msg_srv.encode())
                    # msg = input('Enter a message to send: ')
                    """ 
                    le serveur va ici récupere les commandes du client et lui renvoyer. Dans la suite de la SAÉ, 
                    le serveur fera pareil mais en renvoyant le résultat des commandes demandées par le client.
                    """
                conn.close()
        print ("Connection closed")
        server_socket.close()
        print ("Server closed")

# Coder les commande ici

if __name__ == '__main__':
    serveur()