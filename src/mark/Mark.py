class Mark:
    __roll: None
    __subject: None
    __score: None
    
    def __init__(self, roll, subject, score):
        self.__roll = roll
        self.__subject = subject
        self.__score = score
        
    @property
    def roll(self): return self.__roll
    
    @roll.setter
    def roll(self, value): 
        self.__roll = value
            
    @property
    def subject(self): return self.__subject
    
    @subject.setter
    def subject(self, value):  
        if isinstance(value, str):
            self.__subject = value
        else:
            raise TypeError('Subject name should be a string')
    
    @property
    def score(self): return self.__score
    
    @score.setter
    def score(self, value):
        if isinstance(value, (int, float)) or value == None:
            self.__score = value
        else:
            raise TypeError("Marks should be a number")
        
    def print_score(self):
        roll_str = str(self.roll).ljust(10)  # Adjust the width as needed
        subject_str = str(self.subject).ljust(10)  # Adjust the width as needed
        score_str = str(self.score).ljust(10)  # Adjust the width as needed
        print(f"| {roll_str} | {subject_str} | {score_str} |")
