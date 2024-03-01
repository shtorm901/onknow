from PyQt6 import QtWidgets
from mainWin import Ui_MainWindow

class MainForm(QtWidgets.QMainWindow, Ui_MainWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.DbConnect()
        self.pushButton.clicked.connect(self.Enter)