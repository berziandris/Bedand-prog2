import sys

from PyQt5 import QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from ot import Ui_TicTacToe
from mainwindow import Ui_Main

class TicTacToe:
    def __init__(self):
        self.MainWindow = QtWidgets.QMainWindow()
        self.ui = Ui_Main()
        self.ui2 = Ui_TicTacToe()
        self.ui.setupUi(self.MainWindow)
        self.ui.btn_start.clicked.connect(self.game)
        self.MainWindow.show()


    def game(self):
        self.newWindow = QtWidgets.QMainWindow()
        self.ui2.setupUi(self.newWindow)
        self.ui2.b1.clicked.connect(self.btn_clicked)
        self.newWindow.show()

    def btn_clicked(self):
        self.b1.setText("X")







#MAIN
app = QtWidgets.QApplication(sys.argv)
TTT = TicTacToe()
sys.exit(app.exec_())