import subprocess

class C_Complier:

    def __init__(self, address :str, frequency_input :int, input_str :str):
        self.address_str = address
        self.ip_string = input_str
        list: self.input_data = []
        list: self.buffer = []
        self.__set_input_file()
        self.__read_file()
        self.__get_c_contents()
        self.__set_temp_file(count=frequency_input)
        self.__set_ouput_file()
         


    def __bracket_content(self, s: str) -> str:
        strr = ""
        flag = False
        for i in s:
            if i=='(':
                flag=True
            
            if flag:
                strr+=i
        
        
        strr = strr.replace('&', '')
        strr = strr.replace(r"[^\n]", '')
        
        return strr[:-1]
    
    def __set_input_file(self):
        with open("input.txt", "w") as ip:
            ip.write(self.ip_string)

    def __read_file(self):
        with open("input.txt", "r") as ip:
            self.input_data = ip.read().strip()


    def __get_c_contents(self):
        with open(self.address_str, "r") as f:
            self.buffer = list(f.read().split("\n"))


    def __set_temp_file(self, count :int):
        No_of_times_output = count
        buff = self.buffer
        sizer = len(buff)

        with open("temp.c", "w") as fp:
            
            for i in range(sizer):
                strset = ""
                fp.write(f"\n{buff[i]}")
            
                if "int main(" in buff[i]:
                    fp.write("\n")
                    fp.write(f"int t = {No_of_times_output};\n")
                    fp.write("while(t--){\n")
                    fp.write(r'printf("\n\n");')
                    fp.write(f'printf("TEST CASE (%d):", {No_of_times_output}-t);')
                    fp.write(r'printf("\n");')

                if "scanf(" in buff[i]:
                    s = self.__bracket_content(buff[i])
                    fp.write(f"printf{s};")
                    ch = r'printf("\n");'

                    fp.write(ch)
                    fp.write("\n")

                if i == sizer-1:
                    fp.write("}\n")


    def __set_ouput_file(self):
        subprocess.run(["gcc", "temp.c", "-o", "temp"])

        with open("output.txt", "w") as op:
            subprocess.run([f"./temp.exe"], input=self.input_data, text=True, stdout=op)
            subprocess.run(["rm", "temp.c", "temp.exe"])

    def get_output(self):
        with open("output.txt", "r") as op:
            outt = op.read()
        
        return outt
    
