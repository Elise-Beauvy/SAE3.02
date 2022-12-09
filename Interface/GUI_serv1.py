import sys
import csv

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
        self.__grid.addWidget(self.__etat,2,0)
        self.__grid.addWidget(self.__disconnect,3,0)
        self.__grid.addWidget(self.__kill,4,0)
        self.__grid.addWidget(self.__reset,5,0)
        self.__grid.addWidget(self.__cmd,7,0)
        self.__grid.addWidget(self.__os,8,0)
        self.__grid.addWidget(self.__cpu,9,0)
        self.__grid.addWidget(self.__ip,10,0)
        self.__grid.addWidget(self.__name,11,0)
        self.__grid.addWidget(self.__ram,12,0)
        self.__grid.addWidget(self.__python,13,0)

        self.__cpu.clicked.connect(self._cpu)
        self.__os.clicked.connect(self._os)
        """self.__disconnect.clicked.connect(self._disco)"""

        self.__info.setStyleSheet("color: red")

    """def _host(self):
        cr = csv.reader(open('../hostname.csv', 'r'))
        print(cr)
        QMessageBox(text="hostname.csv")"""

    def _cpu(self):
        self.__cpu = Cpu()
        self.__cpu.show()

    def _os(self):
        self.__os = Os()
        self.__os.show()

    """def _disco(self):
        client = Client("127.0.0.1", 10111)
        client.send("disconnect")
        self.__deconn = QLabel("Serveur déconnecté")
        self.__grid.addWidget(self.__deconn,3,1)"""



if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Serveur1()
    window.show()
    app.exec()