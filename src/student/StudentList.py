import csv
from student.Student import Student
from linked_list.LinkedList import LinkedList

student_file_name = "data/student.csv" 


class StudentList(LinkedList):
    @staticmethod
    def create_student(line):
        tokens = line.strip().split(",")
        roll = tokens[0].strip()
        name = tokens[1].strip()
        birth = int(tokens[2].strip())
        hometown = tokens[3].strip()
        return Student(roll, name, birth, hometown)
    
    def read_from_file(self):
        with open(student_file_name, "r") as file:
            csv_reader = csv.reader(file)
            next(csv_reader)  # Skip the header row
            for line in csv_reader:
                student = self.create_student(",".join(line))
                self.addLast(student)  # Add student to the linked list
                
    def save_to_file(self):
        with open(student_file_name, "w") as file:
            file.write("roll,name,birth,hometown\n")
            for student in self:
                file.write(f"{student.roll},{student.name},{student.birth},{student.hometown}\n")
        print("Student data saved to file successfully.")



    def printList(self):
        print("-------------------------------------------------------------------------\n")
        print("| Roll       | Name                 | Age        | Hometown             |\n")
        print("-------------------------------------------------------------------------\n")
        for student in self:
            student.print_student()
        print("-------------------------------------------------------------------------\n")
        
    def searchByRoll(self, roll):
        found_student = None
        for student in self:
            if (student.roll == roll):
                found_student = student
                break
        return found_student

    # find by roll
    def displayByRoll(self, roll):
        find = self.searchByRoll(roll)
        if (find != None):
            print("Student Found!\n")
            find.print_student() 
        else:
            print("Not found!")
            
    def add_student(self):
        roll = input("Enter Roll: ")
        for s in self:
            if (s.roll == roll):
                print("\nThis Roll is already taken.\nPlease enter a different Roll.")
                return False
        name = input("Enter Name: ")
        birth = int(input("Enter birth year: "))
        hometown = input("Enter hometown: ")
        student = Student(roll, name, birth, hometown)
        self.addLast(student)
        print("Student added successfully. New student: ")
        student.print_student()
        return True

    def delete_student(self, roll, mark_list):
        status = False
        # find student by roll
        stud = self.searchByRoll(roll)
        if (stud == None):
            print("No such student exists.")
            return status
        # check student learnt a subject, if yes => cannot delete
        if mark_list.check_student_existence(roll) != False:
            print("This student has learnt a subject.\n Therefore, he/ she cannot be deleted")
            return status
        # remove from linked list and set status to true
        self.remove_node(stud)
        print("Student deleted successfully!")
        status = True
        return status
    
    def update_student(self, roll):
        student = self.searchByRoll(roll)
        if student != None :
            print("The student profile:")
            student.print_student()
            
            # edit profile
            print("Update the student profile:")
            print("\n")
            new_hometown = input("Enter new hometown: \n (Blank space will be treated as no change): ").strip()
            print("\n")
            new_name = input("Enter new name: \n (Blank space will be treated as no change): ").strip()
            print("\n")
            new_birth = input("Enter new birth year: \n (Blank space will be treated as no change): ").strip()
            print("\n")
            
            if new_name != "":
                student.name = new_name
                
            if new_birth != "":
                student.birth = int(new_birth)
            
            if new_hometown != "":
                student.hometown = new_hometown
           
            print("Student information after updating:")
            student.print_student()
        else:
            print("Invalid student information!")

            
