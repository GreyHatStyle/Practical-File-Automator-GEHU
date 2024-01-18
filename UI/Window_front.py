from PyQt6.QtWidgets import QMainWindow, QApplication
from PyQt6.QtWidgets import QLabel, QPushButton, QStackedWidget
from PyQt6 import uic
import sys

class UI(QMainWindow):
    def __init__(self):
        super(UI, self).__init__()

        #load the UI file
        uic.loadUi("Main.ui", self)

        #Show the app
        self.show()


# Initialize the app
def main_exe():
    app = QApplication(sys.argv)
    window = UI()
    app.exec()


if __name__ == "__main__":
    main_exe()