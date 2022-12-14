import sys

from client import Client
from GUI_cpu import Cpu
from GUI_os import Os


from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QGridLayout, QLabel, QPushButton, QLineEdit, QComboBox, \
    QHBoxLayout, QMessageBox
from PyQt5.QtCore import *
from PyQt5.QtGui import *


class Serveur1(QMainWindow):
    def __init__(self):
        super().__init__()
        self.__widget = QWidget()
        self.__widget.setWindowTitle("Serveur1")
        self.setCentralWidget(self.__widget)
        self.__grid = QGridLayout()
        self.__widget.setLayout(self.__grid)

        self.__info = QLabel("Serveur1")
        self.__fichier = QLabel("Lire un fichier:")
        self.__lirefichier = QLineEdit("")
        self.__boutonlire = QPushButton("Lire")
        self.__etat = QLabel("état du serveur")
        self.__disconnect = QPushButton("Disconnect")
        self.__kill = QPushButton("Kill")
        self.__reset = QPushButton("Reset")
        self.__hostname = QPushButton("Hostname")
        self.__cmd = QLabel("Infos")
        self.__os = QPushButton("OS")
        self.__cpu = QPushButton("CPU")
        self.__ip = QPushButton("IP")
        self.__name = QPushButton("NAME")
        self.__ram = QPushButton("RAM")
        self.__python = QPushButton("Python version")


        self.__grid.addWidget(self.__info, 1,0)
        self.__grid.addWidget(self.__fichier,2,0)
        self.__grid.addWidget(self.__lirefichier,2,1)
        self.__grid.addWidget(self.__boutonlire,2,2)
        self.__grid.addWidget(self.__etat,3,0)
        self.__grid.addWidget(self.__disconnect,4,0)
        self.__grid.addWidget(self.__kill,5,0)
        self.__grid.addWidget(self.__reset,6,0)
        self.__grid.addWidget(self.__cmd,7,0)
        self.__grid.addWidget(self.__os,8,0)
        self.__grid.addWidget(self.__cpu,9,0)
        self.__grid.addWidget(self.__ip,10,0)
        self.__grid.addWidget(self.__name,11,0)
        self.__grid.addWidget(self.__ram,12,0)
        self.__grid.addWidget(self.__python,13,0)

        self.__boutonlire.clicked.connect(self._lireunfichier)
        self.__cpu.clicked.connect(self._cpu)
        self.__os.clicked.connect(self._os)
        """self.__disconnect.clicked.connect(self._disco)"""

        self.__info.setStyleSheet("color: red")

    def _lireunfichier(self):
        print(f"Lecture du fichier {self.__lirefichier}")
        self.__clientList = []
        IP = []
        IP.append("localhost")
        for ip in IP:
            print(f"Connexion à {ip} ...")
            monclient = Client(ip, 10111)
            monclient.connect()
            print("Client connecté au serveur")
            self.__clientList.append(monclient)

    def _cpu(self):
        Client.send_interface("cpu")

        """QMessageBox(text=).exec()"""
        """self.__cpu = Cpu()
        self.__cpu.show()"""

    def _os(self):
        self.__os = Os()
        self.__os.show()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Serveur1()
    window.show()
    app.exec()