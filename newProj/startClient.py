from startWindowForm import StartForm
import sys
from PyQt6 import QtWidgets


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    start_Window = StartForm()
    start_Window.show()
    app.exec()