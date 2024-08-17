from os import listdir
class Format_Ctrl_Utils:
    
    def __init__(self):
        pass

    def person_details_formatter(self, detailsList: list) ->str:
        Name = detailsList[0].upper()  # Name
        Roll_num = detailsList[1].upper()  # Roll Number
        Section = detailsList[2].upper()  # Section
        Course = detailsList[3].upper()  # Course
        format = f"""/*
NAME - {Name}
ROLL NO - {Roll_num}
SECTION - {Section}
COURSE - {Course}
BRANCH - CSE
*/
"""
        return format
    
    def get_c_files(self, folder_address: str):
        dir_list = listdir(folder_address)
        c_files = []
        for i in dir_list:
            if i[-2::] == ".c":
                c_files.append(f"{folder_address}\\{i}")
        try:
            c_files.remove('tempCodeRunnerFile.c')
        except:
            print("")
        # print("List is : ", c_files)
        return c_files
    
    
    def get_cpp_files(self, folder_address: str):
        dir_list = listdir(folder_address)
        print(dir_list)
        cpp_files = []
        for i in dir_list:
            if i[-4::] == ".cpp":
                cpp_files.append(f"{folder_address}\\{i}")
        try:
            cpp_files.remove('tempCodeRunnerFile.cpp')
        except:
            print("")
        # print("List is : ", cpp_files)
        return cpp_files