from docx import Document
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.shared import Pt
from .Format_Doc import WordDocument_Handle
from PyQt6.QtWidgets import QProgressBar


class Main_Format_Handle:
    def __init__(self, doc: Document, BefIpList: list, GenFont: list, headFootList: list):
        self.document = doc

        self.start = WordDocument_Handle(doc, befIpOpList=BefIpList, genericFont=GenFont)
        self.bIpOpL = BefIpList
        self.start.set_headFoot(headFootList)

    
    def NextQues_PushB_Func(self, detail_list, detail_fsty, detail_fsize, detail_boldd, bef_ip_fsize, bef_ip_bold, file_address, 
                            bef_op_fsize, bef_op_bold, count, ipString, opc_fSize, opc_bold, question_,pg_bar2:QProgressBar,
                            mode):
        
        # Set Question
        self.start.set_question(question=question_)
        # Set Details Below Question
        self.start.set_details(DetailsList=detail_list, fontstyle=detail_fsty, fontsize=detail_fsize, isbold=detail_boldd)
        # Code Heading
        self.start.set_befCode(fontsize=bef_ip_fsize, isbold=bef_ip_bold)
        # Code Insertion
        self.start.set_code(address=file_address)
        # Output Heading
        self.start.set_befOutput(fontsize=bef_op_fsize, isbold=bef_op_bold)
        # Output Insertion
        self.start.set_outputCases_text(Address=file_address, frequency=count, inputStr=ipString, fontsize=opc_fSize, isbold=opc_bold, mode=mode)
        pg_bar2.setValue(80)

    
    def Save_File_Func(self, file_address):
        self.start.save_file(fileaddress=file_address)
        
        
    
    

