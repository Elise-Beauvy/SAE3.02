import socket,sys,time,threading


class Client():
    def __init__(self,hostname: str,port: int):
        self.__port = port
        self.__hostname = hostname
        self.__socket = None

    def dialogue(self):
        msg = ""
        msg_srv = ""
        while msg != "kill" and msg != "disconnect" and msg != "reset":
            msg = input("client: ")
            self.__socket.send(msg.encode())
            msg_srv = self.__socket.recv(1024).decode()
            print(msg_srv)

    def isConnect(self):
        return self.__socket!=None

    def __connect(self):
        try:

            self.__socket = socket.socket()
            self.__socket.connect((self.__hostname,self.__port))


        except socket.error:
            print("adresseIP/Port déja utilisé ou inexistant")
            sys.exit(-1)

    def __send(self):
        if self.isConnect():
            message = input("client: ")
            try:
                self.__socket.send(message.encode())
            except BrokenPipeError:
                print("erreur, socket fermée")
            return message
        else:
            print("n'est pas connecté")

    def __receive(self):
        message_srv = ""
        while message_srv != "kill" and message_srv != "disconnect" and message_srv != "reset":
            message_srv = self.__socket.recv(1024).decode()
            print(message_srv)

    def close(self):
        self.__socket.close()

    def send(self):
        threading.Thread(target=self.__send())

    def receive(self):
        threading.Thread(target=self.__receive())

    def connect(self):
        threading.Thread(target=self.__connect())


if __name__ == "__main__":

    print(sys.argv)
    if len(sys.argv) < 3:
        client = Client("127.0.0.1",10111)

    # en dehors du if
    client.connect()
    client.dialogue()