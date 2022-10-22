import course_log

print("")

print("________________Welcome to Course Management Application________________")

print("")

user_menu_choice = ''
course_log_reference = course_log.CourseLog()

while user_menu_choice != 'quit':

    print("\t\t ----------------------------")
    print("\t\t|            Menu            |")
    print("\t\t ----------------------------")
    print("\t\t|Add Course         : add    |")
    print("\t\t|Update Course      : update |")
    print("\t\t|Delete Course      : delete |")
    print("\t\t|Show All Courses   : courses|")
    print("\t\t|Show One Course    : course |")
    print("\t\t|Search Course      : search |")
    print("\t\t|Quit               : quit   |")
    print("\t\t ----------------------------")

    user_menu_choice = input("Chose from the menu above: ").replace(" ", "")
    print("=>")

    if user_menu_choice == 'add':
        course_code = input("Input Course code: ")
        course_log_reference.add_course( course_code)
        print("")

    elif user_menu_choice == 'update':
        print("Demo update")
        print("")

    elif user_menu_choice == 'delete':
        course_code = input("Input course code to delete course: ")
        course_log_reference.delete_course(course_code)
        print("")

    elif user_menu_choice == 'courses':
        course_log_reference.show_all_courses()
        print("")

    elif user_menu_choice == 'course':
        course_code = input("Input course code to see details: ")
        course_log_reference.show_one_course(course_code)
        print("")

    elif user_menu_choice == 'search':
        course_code = input("Input course code to search: ")
        if course_log_reference.search_course(course_code) != None:
            print("Course found!")
            course_log_reference.show_one_course(course_code)
        else:
            adding_choice = input("Course does not exist. Do you want to add as new course?('y' to add): ")
            if adding_choice == 'y':
                course_log_reference.add_course(course_code)
        print("")

    elif user_menu_choice == 'quit':
        print("Bye..")
        print("")

    else:
        print('Invalid choice!')
        print("")
