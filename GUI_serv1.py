import socket
import sys

from client import Client


from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QGridLayout, QLabel, QPushButton, QLineEdit, QComboBox, \
    QHBoxLayout, QMessageBox, QTextBrowser, QTableView, QTableWidget
from PyQt5.QtCore import *
from PyQt5.QtGui import *


class Serveur1(QMainWindow):
    def __init__(self):
        super().__init__()
        self.__widget = QWidget()
        self.__widget.setWindowTitle("Serveur")
        self.setCentralWidget(self.__widget)
        self.__grid = QGridLayout()
        self.__widget.setLayout(self.__grid)

        self.__info = QLabel("Serveur1")
        self.__fichier = QLabel("Lire un fichier:")
        self.__lirefichier = QLineEdit("")
        self.__boutonlire = QPushButton("Lire")
        self.__etat = QLabel("état du serveur/client")
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

        self.__boutonlire.clicked.connect(self._lireunfichier)
        self.__disconnect.clicked.connect(self._disconnect)
        self.__kill.clicked.connect(self._kill)
        self.__reset.clicked.connect(self._reset)
        self.__cpu.clicked.connect(self._cpu)
        self.__os.clicked.connect(self._os)
        self.__ip.clicked.connect(self._ip)
        self.__name.clicked.connect(self._name)
        self.__ram.clicked.connect(self._ram)

        self.__info.setStyleSheet("color: red")
        self.__disconnect.setStyleSheet("color: green")
        self.__kill.setStyleSheet("color: green")
        self.__reset.setStyleSheet("color: green")
        self.__cpu.setStyleSheet("color: blue")
        self.__os.setStyleSheet("color: blue")
        self.__ip.setStyleSheet("color: blue")
        self.__name.setStyleSheet("color: blue")
        self.__ram.setStyleSheet("color: blue")

    def _lireunfichier(self):
        print(f"Lecture du fichier {self.__lirefichier}")
        self.__clientList = []
        IP = []
        IP.append("localhost")
        for ip in IP:
            print(f"Connexion à {ip} ...")
            self.__monclient = Client(ip, 10111)
            self.__monclient.connect()
            print("Client connecté au serveur")
            self.__clientList.append(self.__monclient)

    def _disconnect(self):
        try:
            for Client in self.__clientList:
                Client.send_interface("disconnect")
                print("Client déconnecté")
        except:
            print ("Serveur ou client pas connecte")

    def _kill(self):
        try:
            for Client in self.__clientList:
                Client.send_interface("kill")
                print("serveur déconnecté")
        except:
            print ("Serveur ou client pas connecté")

    def _reset(self):
        try:
            for Client in self.__clientList:
                Client.send_interface("reset")
                print("redémarrage du serveur, client déconnecté")
        except:
            print ("Serveur ou client pas connecte")

    def _cpu(self):
        try:
            for Client in self.__clientList:
                cpu = Client.send_interface("cpu")
                QMessageBox(text=f"{cpu}").exec()
        except:
            print("Serveur ou client pas connecté")

    def _os(self):
        try:
            for Client in self.__clientList:
                os = Client.send_interface("os")
                QMessageBox(text=f"{os}").exec()
        except:
            print("Serveur ou client pas connecté")

    def _ip(self):
        try:
            for Client in self.__clientList:
                ip = Client.send_interface("ip")
                QMessageBox(text=f"{ip}").exec()
        except:
            print("Serveur ou client pas connecté")

    def _name(self):
        try:
            for Client in self.__clientList:
                name = Client.send_interface("name")
                QMessageBox(text=f"{name}").exec()
        except:
            print("Serveur ou client pas connecté")

    def _ram(self):
        try:
            for Client in self.__clientList:
                ram = Client.send_interface("ram")
                QMessageBox(text=f"{ram}").exec()
        except:
            print("Serveur ou client pas connecté")

    def closeEvent(self, _e: QCloseEvent):
        box = QMessageBox()
        box.setWindowTitle("Quitter")
        box.setText("Voulez vous quitter ?")
        box.addButton(QMessageBox.Yes)
        box.addButton(QMessageBox.No)

        ret = box.exec()

        if ret == QMessageBox.Yes:
            for Client in self.__clientList:
                Client.send_interface("disconnect")
            QCoreApplication.exit(0)
        else:
            _e.ignore()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Serveur1()
    window.show()
    app.exec()