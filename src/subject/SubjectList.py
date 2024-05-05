import csv
from subject.Subject import Subject
from linked_list.LinkedList import LinkedList

subject_file_name = "data/subject.csv" 

class SubjectList(LinkedList): 
            
    @staticmethod
    def create_subject(line):
        tokens = line.strip().split(",")
        subject_id = tokens[0].strip()
        subject_name = tokens[1].strip()
        return Subject(subject_id, subject_name)
    
    def read_from_file(self):
        with open(subject_file_name, "r") as file:
            csv_reader = csv.reader(file)
            next(csv_reader)  # Skip the header row
            for line in csv_reader:
                subject = self.create_subject(",".join(line))
                self.addLast(subject)  # Add student to the linked list
                
    def save_to_file(self):
        with open(subject_file_name, "w") as file:
            file.write("subject_id,subject_name\n")
            for subject in self:
                file.write(f"{subject.subject_id},{subject.subject_name}\n")
        print("Subject data saved to file successfully.")


    def printList(self):
        print("--------------------------------------------------\n")
        print("| Subject ID      | Subject Name                 |\n")
        print("--------------------------------------------------\n")
        for subject in self:
            subject.print_subject()
        print("--------------------------------------------------\n")
        
    def searchBySubjectId(self, subject_id):
        found_subject = None
        for subject in self:
            if (subject.subject_id == subject_id):
                found_subject = subject
                break
        return found_subject

    # find by subject ID
    def displayById(self, subject_id):
        find = self.searchBySubjectId(subject_id)
        if (find != None):
            print("Subject Found!\n")
            find.print_subject() 
        else:
            print("Not found!")
            
    def add_subject(self):
        id = input("Enter Subject ID: ")
        for s in self:
            if (s.subject_id == id):
                print("\nThis subject ID is already taken.\nPlease enter a different subject ID.")
                return False
        name = input("Enter Subject Name: ")
        
        subject = Subject(id, name)
        self.addLast(subject)
        print("Subject added successfully.")
        return True
    
    def delete_subject(self, id, mark_list):
        status = False
        # find subject by ID
        sub = self.searchBySubjectId(id)
        if (sub == None):
            print("No such subject exists.")
            return status
        # check student learnt a subject, if yes => cannot delete
        if mark_list.check_subject_existence(id) != False:
            print("This subject has been learnt.\n Therefore, it cannot be deleted")
            return status
        # remove from linked list and set status to true
        self.remove_node(sub)
        print("Subject deleted successfully!")
        status = True
        return status

    def update_subject(self, id, new_name):
        status = False
        subject = self.searchBySubjectId(id)
        if subject != None:
            subject.subject_name = new_name
            print("Subject updated successfully.")
            subject.print_subject()
            status = True
        else:
            print("The subject does not exist.")
        return status
        