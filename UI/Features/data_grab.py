
from PyQt6.QtWidgets import QLineEdit, QTextEdit
from os import getcwd

class Data_Put_Handle:
    def __init__(self) -> None:
        pass
    
    def put_details(self, name :QLineEdit, roll :QLineEdit, sec :QLineEdit,
                    course: QLineEdit):
        path = getcwd()
        path = f"{path}\\UI\\Features\\Data\\details.txt"
        with open(path, "r") as ip:
            lst = ip.read().split('#')

        name.setText(lst[0])
        roll.setText(lst[1])
        sec.setText(lst[2])
        course.setText(lst[3])


    def get_settingData(self)->dict:
        data = {}
        path = getcwd()
        path = f"{path}\\UI\\Features\\Data\\settings.txt"
        with open(path, "r") as ip:
            data['header_footer'] = ip.readline().replace('\n','').split('#')
            data['bef_ip'] = ip.readline().replace('\n','').split('#')
            data['bef_op'] = ip.readline().replace('\n','').split('#')
            data['gen_font'] = ip.readline().replace('\n','').split('#')

        return data
    
    def put_settingData(self, headFoot :list, befip: list, befop: list, genfont: list):
        data = self.get_settingData()
        
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

        
