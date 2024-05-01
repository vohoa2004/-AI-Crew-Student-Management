import datetime

class Student:
    def __init__(self, roll, name, birth, hometown):
        self.__roll = roll
        self.__name = name
        self.__birth = birth
        self.__hometown = hometown
        
    @property
    def roll(self):
        return self.__roll
    
    @roll.setter
    def roll(self, value): 
        self.__roll = value
    
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self,value):
        self.__name = value
    
    @property
    def birth(self):
        return self.__birth
    
    @birth.setter
    def birth(self, value):
        self.__birth = value
    
    def get_age(self):
        today = datetime.date.today()
        age = today.year - self.__birth
        return age
    
    @property
    def hometown(self):
        return self.__hometown
    
    @hometown.setter
    def hometown(self,value):
        self.__hometown = value

    def print_student(self):
        roll_str = str(self.roll).ljust(10)  # Adjust the width as needed
        name_str = str(self.name).ljust(20)  # Adjust the width as needed
        age_str = str(self.get_age()).ljust(10)  # Adjust the width as needed
        hometown_str = str(self.hometown).ljust(20)  # Adjust the width as needed
        print(f"| {roll_str} | {name_str} | {age_str} | {hometown_str} |")

 