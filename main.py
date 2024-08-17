from UI import GUI_Front
from subprocess import run

if __name__ == "__main__":
    process_path = "Language_Selection\\Process"

    GUI_Front()
    run(["rm",f"{process_path}\\input.txt",f"{process_path}\\output.txt"])
    

    