from mark.Mark import Mark

file_name = "data/mark.csv"

class MarkList:
    def __init__(self):
        self.marks = {}

    def input_mark (self, roll, subject, score):
        return Mark(roll, subject, score)

    def add_mark(self, mark):
        key = (mark.roll, mark.subject)
        if key in self.marks:
            print("This student already joined this subject.")
            return False
        else:
            self.marks[key] = mark.score
            return True
        
    def update_mark(self, mark):
        key = (mark.roll, mark.subject)
        self.marks[key] = mark.score

    def get_mark(self, roll, subject):
        key = (roll, subject)
        return self.marks.get(key, None)

    def remove_mark(self, roll, subject):
        key = (roll, subject)
        if key in self.marks:
            del self.marks[key]

    def get_student_marks(self, roll):
        student_marks = {}
        for (student_roll, subject), score in self.marks.items():
            if student_roll == roll:
                student_marks[subject] = score
        return student_marks

    def get_subject_marks(self, subject):
        subject_marks = {}
        for (roll, subject_id), score in self.marks.items():
            if subject_id == subject:
                subject_marks[roll] = score
        return subject_marks
    
    def print_student_marks(self, roll):
        student_marks = self.get_student_marks(roll)
        if student_marks:
            print(f"Student Marks for Roll Number {roll}:")
            for subject, score in student_marks.items():
                print(f"\tSubject: {subject}, Score: {score}")
        else:
            print(f"No marks found for student with roll number {roll}")

    def print_subject_marks(self, subject):
        subject_marks = self.get_subject_marks(subject)
        if subject_marks:
            print(f"Students who learnt the Subject {subject}:")
            for roll, score in subject_marks.items():
                print(f"\tRoll Number: {roll}, Score: {score}")
        else:
            print(f"No students found for subject {subject}")
    
    def print_all_marks(self):
        for (roll, subject), mark in self.marks.items():
            print(f"Roll Number: {roll}, Subject: {subject}, Mark: {mark}")

    def check_subject_existence(self, subject_id):
        return any(subject_id == subject for (_, subject), _ in self.marks.items())
    
    def check_student_existence(self, student_roll):
        return any(student_roll == roll for (roll, _), _ in self.marks.items())

    def read_from_file(self):
        with open(file_name, 'r') as file:
            next(file)
            for line in file:
                roll, subject, score = line.strip().split(',')
                if score != "None":
                    self.add_mark(Mark(roll, subject, int(score)))
                else:
                    self.add_mark(Mark(roll, subject, None))

    def save_to_file(self):
        with open(file_name, 'w') as file:
            file.write("roll,subject,score\n")
            for (roll, subject), score in self.marks.items():
                file.write(f"{roll},{subject},{score}\n")
        print("Grade data saved successfully!")
