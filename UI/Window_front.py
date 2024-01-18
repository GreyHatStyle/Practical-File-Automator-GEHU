from .MainUI import *
import sys

# def main_exe():
#     app = QtWidgets.QApplication(sys.argv)
#     MainWindow = QtWidgets.QMainWindow()
#     ui = Ui_MainWindow()
#     ui.setupUi(MainWindow)



#     # to show UI
#     ui.pg1_next.clicked.connect(lambda: ui.stackedWidget.setCurrentWidget(ui.page_2))

#     MainWindow.show()
#     sys.exit(app.exec())


# if __name__ == "__main__":
#     main_exe()


class GUI_Front:
    def __init__(self) -> None:
        app = QtWidgets.QApplication(sys.argv)
        MainWindow = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(MainWindow)
        self.setter()
        MainWindow.show()
        app.exec()
        

    def setter(self):
        self.ui.pg1_next.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_2))
        

    

if __name__ == "__main__":
    GUI_Front()
