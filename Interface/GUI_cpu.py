import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QGridLayout, QLabel, QPushButton, QLineEdit, QComboBox, \
    QHBoxLayout, QMessageBox
from PyQt5.QtCore import *
from PyQt5.QtGui import *

from client import Client

Client("127.0.0.1",10111)

class Cpu(QMainWindow):
    def __init__(self):
        super().__init__()
        self.__widget = QWidget()
        self.__widget.setWindowTitle("CPU")
        self.setCentralWidget(self.__widget)
        self.__grid = QGridLayout()
        self.__widget.setLayout(self.__grid)

        self.__info = QLabel("CPU")

        self.__grid.addWidget(self.__info,1,0)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Cpu()
    window.show()
    app.exec()