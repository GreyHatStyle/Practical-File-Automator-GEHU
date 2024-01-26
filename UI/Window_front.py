from .MainUI import *
import sys
from PyQt6.QtWidgets import QFileDialog
from Utils import Format_Ctrl_Utils
from .Features import Data_Put_Handle
from tkinter import messagebox


class GUI_Front:
    def __init__(self) -> None:
        app = QtWidgets.QApplication(sys.argv)
        MainWindow = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(MainWindow)


        # Storing Variables
        self.folder_address = ""
        self.headerfooterList = []  # [header, footer]
        self.mode = ""              # java, c, cpp, python
        self.bef_ip_conf = []       # [text, fontsize, bold]
        self.bef_op_conf = []
        self.generic_Font = []      # [fontstyle, fontsize]


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
        self.ui.pg1_next.clicked.connect(lambda: self.Start_Butn())
        self.ui.pg2_next.clicked.connect(lambda: self.Setting_next_Butn())
        self.ui.pg3_createNext.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_4))
        self.ui.pg4_quit.clicked.connect(lambda: sys.exit())
        self.ui.pg1_about.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_4))

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
    

    # Moving to Setting page
    def Start_Butn(self):

        # If details and save details doesn't match
        check_lst = self.memory_set.data_details
        current_lst = [self.ui.pg1_NameInp.text(), self.ui.pg1_RollNoInp.text(), self.ui.pg1_SectionInp.text(), 
                       self.ui.pg1_CourseInp.text()]
            
        if check_lst != current_lst:
            print("IT ran")
            self.memory_set.save_detailstxt(current_lst[0], current_lst[1], current_lst[2], current_lst[3])
        
        # Get Folder Path (Also avoiding conflicts via changing button text)
        if self.ui.pg1_next.text() != "Continue" or check_lst != current_lst:
            self.folder_address = QFileDialog.getExistingDirectory(caption='Select Folder that contains C Files')
        

        if self.folder_address == "":
            messagebox.showerror(title="Error!", message="No folder selected!")
            return

        self.ui.pg1_next.setText("Continue")

        # Moves to Next Page
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_2)

    def Page2_InputSetting(self):
        self.headerfooterList = [self.ui.pg2_header_box.text(), self.ui.pg2_footer_box.text()]
        self.bef_ip_conf = [self.ui.pg2_befcodeBox.text(), self.ui.pg2_befCodeFont.text(), self.ui.pg2_BfBold.isChecked()]
        self.bef_op_conf = [self.ui.pg2_befoutBox.text(), self.ui.pg2_befoutFont.text(), self.ui.pg2_BoBold.isChecked()]
        self.generic_Font = [self.ui.pg2_genFontsty.text(), self.ui.pg2_genFontsize.text()]


    # Collecting Inputs of "Setting page" and moving forward
    def Setting_next_Butn(self):
        self.Page2_InputSetting()

        # Setting mode---
        if self.ui.pg2_javaRb.isChecked():
            messagebox.showinfo("Please select differenty option", "For now only 'C' Mode is working...")
            return
        elif self.ui.pg2_cppRb.isChecked():
            messagebox.showinfo("Please select differenty option", "For now only 'C' Mode is working...")
            return
        elif self.ui.pg2_cRb.isChecked():
            self.mode = "c"

        # Edge Cases---
        if self.ui.pg2_befcodeBox.text() == "" or self.ui.pg2_befoutBox.text() == "":
            messagebox.showwarning("Please Select and fill all '*' feilds!", "Before Output or Before Code Field not filled.")
            return
        elif self.ui.pg2_befCodeFont.text() == "" or self.ui.pg2_befoutFont.text() == "":
            messagebox.showwarning("Please Select and fill all '*' feilds!", "Before Output Font or Before Code Font Field not filled.")
            return
        elif not self.ui.pg2_javaRb.isChecked() and not self.ui.pg2_cppRb.isChecked() and not self.ui.pg2_cRb.isChecked():
            messagebox.showwarning("Please Select and fill all '*' feilds!", "No 'Mode' Selected!")
            return
        elif self.ui.pg2_genFontsize.text() == "" or self.ui.pg2_genFontsty.text() == "":
            messagebox.showwarning("Please Completed 'Overall font' details!", "Please Select and fill all '*' feilds!")
            return
        
        # Check if details are new or old---
        dct_data = {'header_footer':self.headerfooterList, 'bef_ip':self.bef_ip_conf[:-1], 
                    'bef_op':self.bef_op_conf[:-1], 'gen_font':self.generic_Font}
        sett_data = self.memory_set.data_dct

        if dct_data != sett_data:
            ans = messagebox.askyesno("Changes Detected in Memory", "Seems like you have changed something...\nDo you want to keep it, for future?")
            if ans:
                
                self.Page2_InputSetting()
                self.memory_set.data_dct = dct_data
                print("Before put setting...",self.memory_set.data_dct)
                self.memory_set.save_settingData(
                    headFoot = self.headerfooterList,
                    befip = self.bef_ip_conf[:-1],
                    befop = self.bef_op_conf[:-1],
                    genfont = self.generic_Font
                )
    


        # Go to next page---
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_3)

        
        



if __name__ == "__main__":
    GUI_Front()
