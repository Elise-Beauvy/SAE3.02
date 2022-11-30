import socket,sys



msgclient = ""
msgserveur = ""

class Client():
    def __init__(self,hostname: str,port: int):
        self.__port = port
        self.__hostname = hostname
        self.__socket = None


    def isConnect(self):
        return self.__socket!=None

    def connect(self):
        try:

            self.__socket = socket.socket()
            self.__socket.connect((self.__hostname,self.__port))


        except socket.error:
            print("adresseIP/Port déja utilisé ou inexistant")
            sys.exit(-1)

    def send(self,msg):
        if self.isConnect():
            self.__socket.send(msg.encode())
            msgserveur = self.__socket.recv(1024).decode()
            print(msgserveur)
        else:
            print("n'est pas connecté")

    def close(self):
        self.__socket.close()


