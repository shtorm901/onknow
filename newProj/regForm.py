from PyQt6 import QtWidgets
from regWin import Ui_RegWindow

class RegWindow(QtWidgets.QMainWindow, Ui_RegWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.createTable()
        self.pushButton.clicked.connect(self.createUser)