import sys
import csv
from client import Client


from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QGridLayout, QLabel, QPushButton, QLineEdit, QComboBox, \
    QHBoxLayout, QMessageBox
from PyQt5.QtCore import *
from PyQt5.QtGui import *


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
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
        self.__retour = QPushButton("<-")

        # Ajouter les composants au grid ayout
        self.__grid.addWidget(self.__srv1, 1, 1)
        self.__grid.addWidget(self.__srv2, 2, 1)
        self.__grid.addWidget(self.__srv3, 3, 1)

        self.__srv1.clicked.connect(self._action1)
        self.__srv2.clicked.connect(self._action2)
        self.__srv3.clicked.connect(self._action3)

        self.__srv1.setStyleSheet("color: red")
        self.__srv2.setStyleSheet("color: blue")
        self.__srv3.setStyleSheet("color: green")

    def _action1(self):
        self.__srv2.hide()
        self.__srv3.hide()
        self.__grid.addWidget(self.__disconnect,2,0)
        self.__grid.addWidget(self.__kill,3,0)
        self.__grid.addWidget(self.__reset,4,0)
        self.__grid.addWidget(self.__hostname,5,0)
        self.__hostname.clicked.connect(self._host)


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

    def closeEvent(self, _e: QCloseEvent):  # <--- Fermeture de l'application depuis la croix Windows
        box = QMessageBox()
        box.setWindowTitle("Quitter ?")
        box.setText("Voulez vous quitter ?")
        box.addButton(QMessageBox.Yes)
        box.addButton(QMessageBox.No)

        ret = box.exec()

        if ret == QMessageBox.Yes:
            QCoreApplication.exit(0)
        else:
            _e.ignore()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()