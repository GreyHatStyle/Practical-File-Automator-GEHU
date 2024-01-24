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