from view.menu import Menu
from mark.MarkBST import MarkBST
class Controller:
    def study_management(roll, student_list, subject_list, mark_list):
        status = False
        while True:
            Menu.display_update_study()
            choice = input("Enter your choice: ")
            if choice == '1':
                # add new mark
                subject_list.printList()
                subject_id = input("Enter subject id: ")
                if subject_list.searchBySubjectId(subject_id) != None:
                    mark = mark_list.input_mark(roll, subject_id, None)
                    status = mark_list.add_mark(mark)
                    if status == True: 
                        print("Registered successfully!")
                else:
                    print("Invalid subject!")            
            elif choice == '2':
                # update mark
                mark_list.print_student_marks(roll)
                subject_id = input("Enter subject id: ")
                if (roll, subject_id) in mark_list.marks: # check if student registered subject
                    score = input("Input new score: ")
                    mark = mark_list.input_mark(roll, subject_id, score)
                    mark_list.update_mark(mark)
                    print("Updated successfully!")
                    status = True
                else:
                    print("This student hasn't joined in this subject!")
            elif choice == '3':
                print("Student's transcript: \n")
                mark_list.print_student_marks(roll)
            elif choice == '4':
                return status

    def student_management(student_list, subject_list, mark_list):
        status = False
        while True:
            Menu.display_student_menu()
            choice = input("Enter your choice: ")
            if choice == '1':
                student_list.printList()
            elif choice == '2':
                roll = input("Enter roll number: ")
                student_list.displayByRoll(roll)
            elif choice == '3':
                status = student_list.add_student()
            elif choice == '4':
                print("Update student profile: ")
                roll = input("Enter the roll number: ")
                
                status = student_list.update_student(roll)
            elif choice == '5':
                roll = input("Enter roll number: ")
                if student_list.searchByRoll(roll) != None:
                    status = Controller.study_management(roll, student_list, subject_list, mark_list)
                else:
                    print("Student not found.")
                
            elif choice == '6':
                roll = input("Enter roll number: ")
                status = student_list.delete_student(roll, mark_list)
                
            elif choice == '7':
                return status  # Return to the main menu
            else:
                print("Invalid choice. Please try again.")
            
    
    def subject_management(subject_list, mark_list):
        status = False
        while True:
            Menu.display_subject_menu()
            choice = input("Enter your choice: ")
            if choice == '1':
                subject_list.printList()
            elif choice == '2':
                id = input("Enter subject id: ")
                subject_list.displayById(id)
            elif choice == '3':
                status = subject_list.add_subject()
            elif choice == '4':
                id = input("Enter subject id: ")
                name = input("Enter new subject name: ")
                if (name.strip() != ""):
                    status = subject_list.update_subject(id, name)
            elif choice == '5':
                id = input("Enter subject id: ")
                status = subject_list.delete_subject(id, mark_list)
            elif choice == '6':
                id = input("Enter subject id: ")
                mark_list.print_subject_marks(id)
            elif choice == '7':
                return status  # Return to the main menu
            else:
                print("Invalid choice. Please try again.")
            
    def grade_management(mark_list, subject_list, student_list):
        status = False
        while True:
            Menu.display_grade_menu()
            choice = input( "Enter your choice: ")
            if choice == '1':
                print("-----------------------------------------")
                print("| Roll       | Subject    | Score       |")
                print("-----------------------------------------")
                mark_list.print_all_marks()
                print("-----------------------------------------")
                markBST = MarkBST()
                root = markBST.create_tree(mark_list.marks)
                Controller.sort_management(markBST, root)
                
            elif choice == '2':
                roll = input("Enter student id: ")
                mark_list.print_student_marks(roll)
                markBST = MarkBST()
                root = markBST.create_tree_student(roll,mark_list.get_student_marks(roll))
                Controller.sort_management(markBST, root)
                
            elif choice == '3':
                subject = input("Enter subject id: ")
                mark_list.print_subject_marks(subject)
                markBST = MarkBST()
                root = markBST.create_tree_student(subject, mark_list.get_subject_marks(subject))
                Controller.sort_management(markBST, root)
                
            
                    
            elif choice == '4':
                roll = input("Enter student id: ")
                subject_id = input("Enter subject id: ")
                if (roll, subject_id) in mark_list.marks: # check if student registered subject
                    score = input("Input new score: ")
                    mark = mark_list.input_mark(roll, subject_id, score)
                    mark_list.update_mark(mark)
                    print("Updated grade successfully!")
                    status = True
                else:
                    print("The student is not enrolled for the given subject.")
                    status = False
                    
            elif choice == '5':
                roll = input("Enter student id: ")
                subject_id = input("Enter subject id: ")
                if (roll, subject_id) in mark_list.marks: # check if student registered subject
                    mark = mark_list.input_mark(roll, subject_id, None)
                    mark_list.update_mark(mark)
                    print("Deleted grade successfully!")
                    status = True
                else:
                    print("The student is not enrolled for the given subject.")
            elif choice == '6':
                return status
            else:
                print("Invalid choice. Please try again.")
               
    def sort_management(markBST, root):
        status = False
        while True:
            Menu.display_sort_menu()
            choice = input( "Enter your choice: ")
            if choice == '1':
                print("-----------------------------------------")
                print("| Roll       | Subject    | Score       |")
                print("-----------------------------------------")
                markBST.inorder_traversal(root, False)
                print("-----------------------------------------")
            elif choice == '2':
                print("-----------------------------------------")
                print("| Roll       | Subject    | Score       |")
                print("-----------------------------------------")
                markBST.inorder_traversal(root, True)
                print("-----------------------------------------")
            elif choice == '3':
                return status
            else:
                print("Invalid choice. Please try again.")
 
    def save_all_file(student_list, subject_list, mark_list):
        student_list.save_to_file()
        subject_list.save_to_file()
        mark_list.save_to_file()
        return False
    
    def exit_app(student_list, subject_list, mark_list, status):
        if status:
            confirm = input("You made some changes to the data in this system.\nDo you want to save before exit? (y/n): ")
            if confirm == 'y':
                status = Controller.save_all_file(student_list, subject_list, mark_list)
                print("Saved! Exiting...")
            else:
                print("Exiting without saving...")
        else:
            print("Exiting...")       