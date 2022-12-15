import socket,sys,time,threading


class Client():
    def __init__(self,hostname: str,port: int):
        self.__port = port
        self.__hostname = hostname
        self.__socket = None

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
        message = ""
        while message != "kill" and message != "disconnect" and message != "reset":
            if self.isConnect():
                try:
                    message = input("client: ")
                    self.__socket.send(message.encode())
                    message_srv = self.__socket.recv(1024).decode()
                    print(message_srv)
                except BrokenPipeError:
                    print("erreur, socket fermée")
            else:
                print("n'est pas connecté")

    def send_interface(self, message):
        if self.isConnect():
            try:
                self.__socket.send(message.encode())
                message_srv = self.__socket.recv(1024).decode()
                return message_srv
            except BrokenPipeError:
                print("erreur, socket fermée")
        else:
            print("n'est pas connecté")

    def __receive(self):
        self.__socket.recv(1024).decode()

    def close(self):
        self.__socket.close()

    def send(self):
        threading.Thread(target=self.__send())

    def connect(self):
        threading.Thread(target=self.__connect())

    def receive(self):
        threading.Thread(target=self.__receive())


if __name__ == "__main__":

    print(sys.argv)
    if len(sys.argv) < 3:
        client = Client("127.0.0.1",10111)

    # en dehors du if
    client.connect()
    client.send()

