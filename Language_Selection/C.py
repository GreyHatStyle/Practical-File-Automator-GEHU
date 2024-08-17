import subprocess

class C_Compiler:

    def __init__(self, address :str, frequency_input :int, input_str :str):
        self.address_str = address
        self.ip_string = input_str
        self.process_path = "Language_Selection\\Process"
        list: self.input_data = []
        list: self.buffer = []
        
        self.__set_input_file()
        self.__read_file()
        self.__get_c_contents()
        self.__set_temp_file(count=frequency_input)
        self.__set_ouput_file()
        
         


    def __bracket_content(self, s: str) -> str:
        """
        Takes bracket content of scanf and in next line use it to print using printf\n
        example:\n
        scanf("%d %d", &n, &m); printf("%d %d", n, m);printf("New line char");
        - returns: *("%d %d", n, m)*
        """
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
        """
        Takes input from user from GUI textbox and store it in "input.txt"
        """
        with open(f"{self.process_path}\\input.txt", "w") as ip:
            ip.write(self.ip_string)

    def __read_file(self):
        """
        Read input from "input.txt" and store it for printing in "temp.c" file
        """
        with open(f"{self.process_path}\\input.txt", "r") as ip:
            self.input_data = ip.read().strip()


    def __get_c_contents(self):
        """
        Get C conents from selected C file and store it
        """
        with open(self.address_str, "r") as f:
            self.buffer = list(f.read().split("\n"))


    def __set_temp_file(self, count :int):
        """
        Essential Function:\n
        - Creates "temp.c" using selected C file.
        - Sets up a *while loop* after **int main or signed main**.
        - This for loop helps to run and **display output**, any number of time user wants. 
        - Prints the input also, to display in word file.
        - Prepares the "temp.c" to execute
        """
        No_of_times_output = count
        buff = self.buffer
        sizer = len(buff)

        with open(f"{self.process_path}\\temp.c", "w") as fp:
            
            for i in range(sizer):
                strset = ""
                fp.write(f"\n{buff[i]}")
            
                if "int main(" in buff[i] or "signed main(" in buff[i]:

                    # Dealing with '{' below int main
                    if '{' in buff[i+1]:
                        fp.write("{")

                    fp.write("\n")
                    fp.write(f"int t = {No_of_times_output};\n")
                    fp.write("while(t--){\n")
                    fp.write(r'printf("\n\n");')
                    fp.write(f'printf("TEST CASE (%d):", {No_of_times_output}-t);')
                    fp.write(r'printf("\n");')

                    if '{' in buff[i+1]:
                        buff[i+1] = ""

                if "scanf(" in buff[i]:
                    s = self.__bracket_content(buff[i])
                    fp.write(f"printf{s};")
                    ch = r'printf("\n");'

                    fp.write(ch)
                    fp.write("\n")

                if i == sizer-1:
                    fp.write("}\n")


    def __set_ouput_file(self):
        """
        Execution process
        - Executes "temp.c" and **stores output** to display in **word file**
        - Deletes "temp.c" and "temp.exe" after its role is completed.
        """
        subprocess.run(["gcc", f"{self.process_path}\\temp.c", "-o", f"{self.process_path}\\temp"])

        with open(f"{self.process_path}\\output.txt", "w") as op:
            from os import remove
            subprocess.run([f"{self.process_path}\\temp.exe"], input=self.input_data, text=True, stdout=op)

            # Using this file will not remain in recycle bin
            remove(f"{self.process_path}\\temp.c")
            remove(f"{self.process_path}\\temp.exe")
            

    def get_output(self): 
        """
        Reads output from "output.txt" and **store it, to display in word file**
        """
        with open(f"{self.process_path}\\output.txt", "r") as op:
            outt = op.read()
        
        return outt
    
