from .MainUI import *
import sys
from PyQt6.QtWidgets import QFileDialog,QProgressBar

from Utils import Format_Ctrl_Utils, Ui_util_Handle
from .Features import Data_Put_Handle
from tkinter import messagebox
from subprocess import run



class GUI_Front:
    def __init__(self) -> None:
        app = QtWidgets.QApplication(sys.argv)
        MainWindow = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(MainWindow)
        MainWindow.setWindowTitle("Practical File Formater")

        # Storing Variables
        self.folder_address = ""
        self.headerfooterList = []  # [header, footer]
        self.mode = ""              # java, c, cpp, python
        self.bef_ip_conf = []       # [text, fontsize, bold]
        self.bef_op_conf = []
        self.generic_Font = []      # [fontstyle, fontsize]

        self.dct_data = {}
        self.sett_data = {}
        self.current_detail_lst = []
        
        
        self.setter()
        MainWindow.show()
        app.exec()


    def setter(self):
        
        #Test command
        # self.ui.pg3_NextQusButton.clicked.connect(lambda: self.ui.pg3_createNext.setEnabled(True))

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
        self.ui.pg3_NextQusButton.clicked.connect(lambda: self.Next_Ques_Butn())
        self.ui.pg3_createNext.clicked.connect(lambda: self.Create_func_Butn())
        self.ui.pg4_quit.clicked.connect(lambda: self.quit())
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
        c_files = util.get_c_files(self.folder_address)
        return c_files
    

    # Moving to Setting page
    def Start_Butn(self):

        # If details and save details doesn't match
        check_lst = self.memory_set.data_details
        self.current_detail_lst = [self.ui.pg1_NameInp.text(), self.ui.pg1_RollNoInp.text(), self.ui.pg1_SectionInp.text(), 
                       self.ui.pg1_CourseInp.text()]
            
        if check_lst != self.current_detail_lst:
            print("IT ran")
            self.memory_set.save_detailstxt(self.current_detail_lst[0], self.current_detail_lst[1], 
                                            self.current_detail_lst[2], self.current_detail_lst[3])
        
        # Get Folder Path (Also avoiding conflicts via changing button text)
        if self.ui.pg1_next.text() != "Continue" or check_lst != self.current_detail_lst:
            self.folder_address = QFileDialog.getExistingDirectory(caption='Select Folder that contains C Files')
        

        if self.folder_address == "":
            messagebox.showerror(title="Error!", message="No folder selected!")
            return

        if len(self.folder_traverse()) == 0:
            messagebox.showerror("No C files", "No C files found in Selected folder")
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
        # Added -1 to skip the Bool part of list
        self.dct_data = {'header_footer':self.headerfooterList, 'bef_ip':self.bef_ip_conf[:-1], 
                    'bef_op':self.bef_op_conf[:-1], 'gen_font':self.generic_Font}
        self.sett_data = self.memory_set.data_dct

        if self.dct_data != self.sett_data:
            ans = messagebox.askyesno("Changes Detected in Memory", "Seems like you have changed something...\nDo you want to keep it, for future?")
            if ans:
                
                self.Page2_InputSetting()
                self.memory_set.data_dct = self.dct_data
                print("Before put setting...",self.memory_set.data_dct)
                self.memory_set.save_settingData(
                    headFoot = self.headerfooterList,
                    befip = self.bef_ip_conf[:-1],
                    befop = self.bef_op_conf[:-1],
                    genfont = self.generic_Font
                )
    
        # Establishing Connection with this one
        self.connection_set = Ui_util_Handle(self.current_detail_lst, self.dct_data)
        self.connection_set.C_filesList = self.folder_traverse()
        self.connection_set.list_size = len(self.connection_set.C_filesList)
        self.connection_set.address = self.folder_address
        print(self.connection_set.C_filesList)
        
        #Set label
        curr_file = self.connection_set.C_filesList[0].split("\\")[-1]
        self.ui.pg3_quesLabel.setText(f'Current File: ({curr_file})')
        # Go to next page---
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_3)


    def Next_Ques_Butn(self):

        # Edge cases
        if self.ui.pg3_questionIP.toPlainText == "" or self.ui.pg3_testCasesIP.toPlainText() == "":
            messagebox.showwarning("Entry Not filled!", "Kindly Fill Question or Input Entry")
            return
        elif self.ui.pg3_IpFrequency.text() == "":
            messagebox.showwarning("Entry Not filled!", "Kindly Fill Frequency of test cases")
            return

        pg3F = self.ui.pg3_fontsizInp.text()
        if pg3F == "":
            pg3F = self.dct_data['gen_font'][1]

        # details list: ['ques','ip', 'freq', 'font']
        pg_3_details = [self.ui.pg3_questionIP.toPlainText(), self.ui.pg3_testCasesIP.toPlainText(),
                        self.ui.pg3_IpFrequency.text(), pg3F]
        
        # bold list: ['pg1_bold', 'bef_ip_bold', 'bef_op_bold', 'pg3_bold'] -> bool List
        bold_list = [self.ui.pg1_inforBoldCB.isChecked(), self.ui.pg2_BfBold.isChecked(),
                     self.ui.pg2_BoBold.isChecked(), self.ui.pg3_boldIp.isChecked()]
        
        
        # Progress Bar
        self.ui.pg3_progressBar.setValue(10)

        # SEND DATA TO WORD!!!!!
        check = self.connection_set.next_data_transfer_util(
            details_pg3 = pg_3_details,
            bold_lst = bold_list,
            label = self.ui.pg3_quesLabel,
            pg_bar = self.ui.pg3_progressBar
        )
        self.ui.pg3_progressBar.setValue(100)
        self.ui.pg3_questionIP.clear()
        self.ui.pg3_testCasesIP.clear()
        self.ui.pg3_IpFrequency.setText("")

        from time import sleep
        sleep(0.4)
        self.ui.pg3_progressBar.setValue(0)

    
        if check:
            self.ui.pg3_NextQusButton.setEnabled(False)
            self.ui.pg3_createNext.setEnabled(True)


    def Create_func_Butn(self):
        self.connection_set.save_file_1()
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_4)
        
    def quit(self):
        run(["rm", "input.txt", "output.txt"])
        sys.exit()


        
        



if __name__ == "__main__":
    GUI_Front()
