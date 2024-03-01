from PyQt6 import QtWidgets
from startWindow import Ui_MainWindow

class StartForm(QtWidgets.QMainWindow, Ui_MainWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.pushButton.clicked.connect(self.registration)
        self.pushButton_2.clicked.connect(self.loggin)