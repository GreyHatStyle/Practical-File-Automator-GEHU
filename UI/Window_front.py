from .MainUI import *
import sys
from PyQt6.QtWidgets import QFileDialog, QMessageBox
from Utils import Format_Ctrl_Utils
from .Features import Data_Put_Handle


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

        # Save Command
        self.ui.pg1_SaveInfoButton.clicked.connect(lambda: self.memory_set.save_detailstxt(
            name = self.ui.pg1_NameInp.text(),
            roll = self.ui.pg1_RollNoInp.text(),
            sec = self.ui.pg1_SectionInp.text(),
            course = self.ui.pg1_CourseInp.text()
        ))
        
        # Next Commands
        self.ui.pg1_next.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_2))
        self.ui.pg2_next.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_3))
        self.ui.pg3_createNext.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_4))
        self.ui.pg4_quit.clicked.connect(lambda: sys.exit())

        # Back Commands
        self.ui.pg2_back.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_1))
        self.ui.pg3_back.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_2))
        self.ui.pg4_back.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_1))

        # Fill memory (Sending LineEdits class)
        self.memory_set = Data_Put_Handle()
        self.memory_set.put_details(
            name = self.ui.pg1_NameInp,
            roll = self.ui.pg1_RollNoInp,
            sec = self.ui.pg1_SectionInp,
            course = self.ui.pg1_CourseInp
        )
            #(Sending List of LineEdits)
        self.memory_set.put_settingData(
            headFoot = [self.ui.pg2_header_box, self.ui.pg2_footer_box],
            befip = [self.ui.pg2_befcodeBox, self.ui.pg2_befCodeFont],
            befop = [self.ui.pg2_befoutBox, self.ui.pg2_befoutFont],
            genfont = [self.ui.pg2_genFontsty, self.ui.pg2_genFontsize]
        )

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
