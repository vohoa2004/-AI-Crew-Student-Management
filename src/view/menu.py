class Menu:
    @staticmethod
    def display_main_menu():
        print("-----------------------------")
        print("| Student Management System |")
        print("-----------------------------")
        print("| 1. Manage Students        |")
        print("| 2. Manage Subjects        |")
        print("| 3. Manage Grades          |")
        print("| 4. Save data              |")
        print("| 5. Exit                   |")
        print("-----------------------------")

    @staticmethod
    def display_student_menu():
        print("-----------------------------")
        print("| Manage Students           |")
        print("-----------------------------")
        print("| 1. View Student List      |")
        print("| 2. Search Student         |")
        print("| 3. Add New Student        |")
        print("| 4. Update Student Profile |")
        print("| 5. Update Student Study   |")
        print("| 6. Delete Student         |")
        print("| 7. Save student data      |")
        print("| 8. Back to Main Menu      |")
        print("-----------------------------")

    @staticmethod
    def display_update_study():
        print("----------------------------------")
        print("| Update Student Study           |")
        print("----------------------------------")
        print("| 1. Register student to subject |")
        print("| 2. Update student grade        |")
        print("| 3. View student transcript     |")
        print("| 4. Save edit                   |")
        print("| 5. Back to Student Menu        |")
        print("----------------------------------")

    @staticmethod
    def display_subject_menu():
        print("------------------------------")
        print("| Manage Subjects            |")
        print("------------------------------")
        print("| 1. View Subject List       |")
        print("| 2. Search Subject          |")
        print("| 3. Add New Subject         |")
        print("| 4. Update Subject          |")
        print("| 5. Delete Subject          |")
        print("| 6. View Students in Subject|")
        print("| 7. Save subject data       |")
        print("| 8. Back to Main Menu       |")
        print("------------------------------")

    @staticmethod        
    def display_grade_menu():
        print("-----------------------------")
        print("| Manage Grades             |")
        print("-----------------------------")
        print("| 1. View Grade List        |")
        print("| 2. Search Grade By Student|")
        print("| 3. Search Grade By Subject|")
        print("| 4. Update grade           |")
        print("| 5. Delete grade           |")
        print("| 6. Save grade data        |")
        print("| 7. Back to Main Menu      |")
        print("-----------------------------")
        
    @staticmethod
    def display_sort_menu():
        print("----------------------------------")
        print("| Sorting Menu                   |")
        print("----------------------------------")
        print("| 1. Sort mark list ascending    |")
        print("| 2. Sort mark list descending   |")
        print("| 3. Back to Previous Menu       |")
        print("----------------------------------")