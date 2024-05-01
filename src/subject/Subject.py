class Subject:
    __subject_id: None
    __subject_name: None
    
    def __init__(self, subject_id, subject_name):
        self.__subject_id = subject_id
        self.__subject_name = subject_name
        
    @property
    def subject_id(self):
        return self.__subject_id
    
    @subject_id.setter
    def subject_id(self, value):
        self.__subject_id = value
        
    @property
    def subject_name(self):
        return self.__subject_name

    @subject_name.setter
    def subject_name(self,value):
        self.__subject_name = value
        
    def print_subject(self):
        subject_id_str = str(self.subject_id).ljust(15)  
        subject_name_str = str(self.subject_name).ljust(28)
        print(f"| {subject_id_str} | {subject_name_str} |")
