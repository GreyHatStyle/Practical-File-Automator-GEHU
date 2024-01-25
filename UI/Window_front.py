from .MainUI import *
import sys
from PyQt6.QtWidgets import QFileDialog
from Utils import Format_Ctrl_Utils

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

        # Next Commands
        self.ui.pg1_next.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_2))
        self.ui.pg2_next.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_3))
        self.ui.pg3_createNext.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_4))
        self.ui.pg4_quit.clicked.connect(lambda: sys.exit())

        # Back Commands
        self.ui.pg2_back.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_1))
        self.ui.pg3_back.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_2))
        self.ui.pg4_back.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_3))

        # Text Linker
        
        self.ui.pg4_TextBrowsr.append("<a href='https://github.com/GreyHatStyle'>@ManasBisht (GitHub)</a>")
        self.ui.pg4_TextBrowsr.append("<a href='https://www.linkedin.com/in/manas-bisht-2609a3258/'>@Manas_Bisht (Linkedin)</a>")
        
    # Traversing Folder
    def folder_traverse(self) -> list:
        util = Format_Ctrl_Utils()
        fname = QFileDialog.getExistingDirectory(self, caption='Select Folder that contains C files')
        c_files = util.get_c_files(fname)
        return c_files
    
    # Sending Data to docx
    def Next_question_Butn(self):
        pass
    

if __name__ == "__main__":
    GUI_Front()
