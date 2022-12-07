import sys
import csv
from client import Client


from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QGridLayout, QLabel, QPushButton, QLineEdit, QComboBox, \
    QHBoxLayout, QMessageBox
from PyQt5.QtCore import *
from PyQt5.QtGui import *


class Serveur2(QMainWindow):
    def __init__(self):
        super().__init__()
        self.__widget = QWidget()
        self.__widget.setWindowTitle("Serveur2")
        self.setCentralWidget(self.__widget)

        self.__grid = QGridLayout()
        self.__widget.setLayout(self.__grid)

        self.__info = QLabel("Serveur2")
        self.__etat = QLabel("état du serveur")
        self.__disconnect = QPushButton("Disconnect")
        self.__kill = QPushButton("Kill")
        self.__reset = QPushButton("Reset")
        self.__cmd = QLabel("Infos")
        self.__os = QPushButton("OS")
        self.__cpu = QPushButton("CPU")
        self.__ip = QPushButton("IP")
        self.__name = QPushButton("NAME")
        self.__ram = QPushButton("RAM")
        self.__python = QPushButton("Python version")

        self.__grid.addWidget(self.__info, 1, 0)
        self.__grid.addWidget(self.__etat,2,0)
        self.__grid.addWidget(self.__disconnect, 3, 0)
        self.__grid.addWidget(self.__kill, 4, 0)
        self.__grid.addWidget(self.__reset, 5, 0)
        self.__grid.addWidget(self.__cmd,7,0)
        self.__grid.addWidget(self.__os,8,0)
        self.__grid.addWidget(self.__cpu,9,0)
        self.__grid.addWidget(self.__ip,10,0)
        self.__grid.addWidget(self.__name,11,0)
        self.__grid.addWidget(self.__ram,12,0)
        self.__grid.addWidget(self.__python,13,0)



        self.__info.setStyleSheet("color: blue")

    """def _host(self):
        cr = csv.reader(open('../hostname.csv', 'r'))
        print(cr)
        QMessageBox(text="hostname.csv"[0])"""

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Serveur2()
    window.show()
    app.exec()