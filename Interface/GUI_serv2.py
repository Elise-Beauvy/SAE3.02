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
        self.__disconnect = QPushButton("Disconnect")
        self.__kill = QPushButton("Kill")
        self.__reset = QPushButton("Reset")
        self.__hostname = QPushButton("Hostname")

        self.__grid.addWidget(self.__info, 1, 0)
        self.__grid.addWidget(self.__disconnect,2,0)
        self.__grid.addWidget(self.__kill,3,0)
        self.__grid.addWidget(self.__reset,4,0)
        self.__grid.addWidget(self.__hostname,5,0)
        self.__hostname.clicked.connect(self._host)

    def _host(self):
        cr = csv.reader(open('../hostname.csv', 'r'))
        print(cr)
        QMessageBox(text="hostname.csv"[0])

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Serveur2()
    window.show()
    app.exec()