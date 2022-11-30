import sys
import csv


from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QGridLayout, QLabel, QPushButton, QLineEdit, QComboBox, \
    QHBoxLayout, QMessageBox

from client import Client

class MainWindow(QMainWindow, Client):
    def __init__(self,hostname: str,port: int):
        super().__init__(hostname,port)
        self.__widget = QWidget()
        self.__widget.setWindowTitle("Client")
        self.setCentralWidget(self.__widget)

        self.__grid = QGridLayout()
        self.__widget.setLayout(self.__grid)

        self.__srv1 = QPushButton("Serveur1")
        self.__srv2 = QPushButton("Serveur2")
        self.__srv3 = QPushButton("Serveur3")
        self.__disconnect = QPushButton("Disconnect")
        self.__kill = QPushButton("Kill")
        self.__reset = QPushButton("Reset")
        self.__hostname = QPushButton("Hostname")
        self.__msg = QPushButton("envoie des messages")

        # Ajouter les composants au grid ayout
        self.__grid.addWidget(self.__srv1, 1, 1)
        self.__grid.addWidget(self.__srv2, 2, 1)
        self.__grid.addWidget(self.__srv3, 3, 1)

        self.__srv1.clicked.connect(self._action1)
        self.__srv2.clicked.connect(self._action2)
        self.__srv3.clicked.connect(self._action3)

    def _action1(self):
        self.__srv2.hide()
        self.__srv3.hide()
        self.__grid.addWidget(self.__disconnect,2,0)
        self.__grid.addWidget(self.__kill,3,0)
        self.__grid.addWidget(self.__reset,4,0)
        self.__grid.addWidget(self.__hostname,5,0)
        self.__grid.addWidget(self.__msg,6,0)
        self.__hostname.clicked.connect(self._host)
        self.__msg.clicked.connect(self._message)


    def _host(self):
        cr = csv.reader(open('hostname.csv','r'))
        print (cr)
        QMessageBox(text="hostname.csv"[0])

    def _message(self):
        QMessageBox(Client)

    def _action2(self):
        self.__srv1.hide()
        self.__srv3.hide()
        self.__grid.addWidget(self.__disconnect, 2, 0)
        self.__grid.addWidget(self.__kill, 3, 0)
        self.__grid.addWidget(self.__reset, 4, 0)

    def _action3(self):
        self.__srv1.hide()
        self.__srv2.hide()
        self.__grid.addWidget(self.__disconnect,2,0)
        self.__grid.addWidget(self.__kill,3,0)
        self.__grid.addWidget(self.__reset,4,0)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow("127.0.0.1",10110)
    window.show()
    app.exec()