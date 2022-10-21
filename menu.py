print("")

print("________________Welcome to Course Management Application________________")

print("")

user_menu_choice = ''

while user_menu_choice != 'quit':

    print("\t\t-----------------------------")
    print("\t\t|            Menu            |")
    print("\t\t-----------------------------")
    print("\t\t|Add Course         : add    |")
    print("\t\t|Update Course      : update |")
    print("\t\t|Delete Course      : delete |")
    print("\t\t|Show All Courses   : courses|")
    print("\t\t|Show One Course    : course |")
    print("\t\t|Search Course      : search |")
    print("\t\t|Quit               : quit   |")
    print("\t\t-----------------------------")

    user_menu_choice = input("Chose from the menu above: ")

    if user_menu_choice == 'add':
        print("Demo add")
        print("")
    elif user_menu_choice == 'update':
        print("Demo update")
        print("")
    elif user_menu_choice == 'delete':
        print("Demo delete")
        print("")
    elif user_menu_choice == 'courses':
        print("Demo courses")
        print("")
    elif user_menu_choice == 'course':
        print("Demo course")
        print("")
    elif user_menu_choice == 'search':
        print("Demo search")
        print("")
    elif user_menu_choice == 'quit':
        print("Bye..")
        print("")
    else:
        print('Invalid choice!')
        print("")
