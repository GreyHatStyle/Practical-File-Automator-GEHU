
from PyQt6.QtWidgets import QLineEdit
from tkinter import messagebox
from os import getcwd

class Data_Put_Handle:
    def __init__(self) -> None:
        self.path = getcwd()

        # Setting Actual Path (Relative Path didn't work for some reason)
        self.details_path = f"{self.path}\\UI\\Features\\Data\\details.txt"
        self.settings_path = f"{self.path}\\UI\\Features\\Data\\settings.txt"
        
        # Strucuring Data from setting.txt
        self.data_dct = self.get_settingData()

        # Getting Data From details.txt
        self.data_details = self.check_details()
    
    # Function for putting details.txt in GUI
        
    def check_details(self)-> list:
        with open(self.details_path, "r") as ip:
            lst = ip.read().split('#')

        return lst
    
    def put_details(self, name :QLineEdit, roll :QLineEdit, sec :QLineEdit,
                    course: QLineEdit):
        
        lst = self.data_details
        name.setText(lst[0])
        roll.setText(lst[1])
        sec.setText(lst[2])
        course.setText(lst[3])


    # Function for updating details.txt in Memory
    def save_detailstxt(self, name: str, roll: str, sec: str, course: str):
        ans = messagebox.askyesno(message="Do you want to Save Changes?", title="Update Details")
        if ans:
            with open(self.details_path, "w") as ip:
                ip.write(f"{name}#{roll}#{sec}#{course}")
            messagebox.showinfo("Saved!", f"""Your details:\nName: {name}\nRoll: {roll}\nSection: {sec}\nCourse: {course}\n
has been saved successfully!""")

        self.data_details = self.check_details()

        


    # Function for putting setting memory data in GUI
    def get_settingData(self)->dict:
        data = {}

        with open(self.settings_path, "r") as ip:
            data['header_footer'] = ip.readline().replace('\n','').split('#')
            data['bef_ip'] = ip.readline().replace('\n','').split('#')
            data['bef_op'] = ip.readline().replace('\n','').split('#')
            data['gen_font'] = ip.readline().replace('\n','').split('#')

        return data
    
    def put_settingData(self, headFoot :list, befip: list, befop: list, genfont: list):
        data = self.data_dct
        
        # header and footer
        headFoot[0].setText(data['header_footer'][0])
        headFoot[1].setText(data['header_footer'][1]) 

        # before Ip, Fontsize
        befip[0].setText(data['bef_ip'][0])
        befip[1].setText(data['bef_ip'][1])

        # before Op, Fontsize
        befop[0].setText(data['bef_op'][0])
        befop[1].setText(data['bef_op'][1])

        # general fontstyle, general fontsize
        genfont[0].setText(data['gen_font'][0])
        genfont[1].setText(data['gen_font'][1])

        

    def save_settingData(self, headFoot :list, befip: list, befop: list, genfont: list):
        with open(self.settings_path, "w") as op:
            op.write(f"{headFoot[0]}#{headFoot[1]}\n{befip[0]}#{befip[1]}\n{befop[0]}#{befop[1]}\n{genfont[0]}#{genfont[1]}")

        messagebox.showinfo("Updated!", "Your information is updated for future")
        
