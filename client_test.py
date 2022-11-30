from client import Client
import socket

host = input("hostname:")
port = int(input("port:"))
heim = Client(host,port)
heim.connect()
rep = heim.send("hye")
if rep == "":
    print("serveur non connecté")
else:
    print(rep)