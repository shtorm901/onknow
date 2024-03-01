from PyQt6 import QtWidgets
from SecondMain import Ui_MainWindow

class SecondWin(QtWidgets.QMainWindow, Ui_MainWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.DbConnect()
        self.getAlltable()