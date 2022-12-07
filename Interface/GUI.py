import sys
from Interface.GUI_serv1 import Serveur1
from GUI_serv2 import Serveur2
from GUI_serv3 import Serveur3


from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QGridLayout, QPushButton, QMessageBox
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

        # Ajouter les composants au grid ayout
        self.__grid.addWidget(self.__srv1, 1, 1)
        self.__grid.addWidget(self.__srv2, 2, 1)
        self.__grid.addWidget(self.__srv3, 3, 1)

        self.__srv1.clicked.connect(self._clicserveur)
        self.__srv2.clicked.connect(self._clicserveur2)
        self.__srv3.clicked.connect(self._clicserveur3)

        self.__srv1.setStyleSheet("color: red")
        self.__srv2.setStyleSheet("color: blue")
        self.__srv3.setStyleSheet("color: green")

    def _clicserveur(self):
        self.__serv1 = Serveur1()
        self.__serv1.show()

    def _clicserveur2(self):
        self.__serv2 = Serveur2()
        self.__serv2.show()

    def _clicserveur3(self):
        self.__serv3 = Serveur3()
        self.__serv3.show()

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