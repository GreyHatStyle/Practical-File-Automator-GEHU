from Format_Control import Main_Format_Handle
from Utils import Format_Ctrl_Utils
from docx import Document

address = "D:\\Manas DMP.docx"
file = "matrix.c"
document = Document()
beflst = ["Code", "Output"]
ques = "Write a C program to take input of matrix and print it."
            
ques2 = "Write a C program to print sum of 3 integers"
            
ques3 = "Write a C program to take input of spaced strings and print it."
            
genFont = ["Times New Roman", "12", False]
headFoot = ["Graphic Era HIll University", r"E:\Manas Bisht\2219043\Sem III\Section - E1"]

details = ["Manas Bisht", "38", "E1", "B.Tech"]
c = 3
print(details)
ip1 = """
2 3
1 2 3
3 4 5
2 5
1 2 3 4 5
2 6 7 8 9
3 3
1 2 3
2 3 4
5 6 7"""

ip2 = """
34 100 4
22 98 23
100 100 100"""

ip3 = """3
Manas is good boy
he is okay with life
as always
2
This is good way
to check
1
I am done"""

start = Main_Format_Handle(doc=document, BefIpList=beflst, GenFont=genFont, headFootList=headFoot)
start.NextQues_PushB_Func(
    detail_list=details, detail_fsty=genFont[0], detail_fsize="12", detail_boldd=False,
    bef_ip_fsize="14", bef_ip_bold=True,
    file_address=file,
    bef_op_fsize="14", bef_op_bold=True,
    count=c, 
    ipString=ip1, 
    opc_fSize="12", opc_bold=False, question_=ques
    
)

start.NextQues_PushB_Func(
    detail_list=details, detail_fsty=genFont[0], detail_fsize="12", detail_boldd=False,
    bef_ip_fsize="14", bef_ip_bold=True,
    file_address="seriall.c",
    bef_op_fsize="14", bef_op_bold=True,
    count=c, 
    ipString=ip2, 
    opc_fSize="12", opc_bold=False, question_=ques2
    
)
start.NextQues_PushB_Func(
    detail_list=details, detail_fsty=genFont[0], detail_fsize="12", detail_boldd=False,
    bef_ip_fsize="14", bef_ip_bold=True,
    file_address="sp-string.c",
    bef_op_fsize="14", bef_op_bold=True,
    count=c, 
    ipString=ip3, 
    opc_fSize="12", opc_bold=False, question_=ques3
    
)
start.Save_File_Func(file_address=address)