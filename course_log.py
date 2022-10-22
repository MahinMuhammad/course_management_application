import course as course_module

class CourseLog():

    courses = []
    def __init__(self):
        pass
    
    def search_course(self, course_code):
        for course in self.courses:
            if course_code == getattr(course, 'course_code'):
                return course
        else:
            return None 

    def add_course(self, course_code):
        if self.search_course(course_code) != None:
            print(f"Course with course code {course_code} already exist!")
            return None
        else:
            course_title = input("Input Course title: ")
            course_credit = input("Input Course credit: ")
            prerequisites = []
            while True:
                user_input = input(f"Input code of prerequisites for {course_title}(input 0 to end): ")
                if user_input == '0':
                    break
                elif self.search_course(user_input) == None:
                    adding_choice = input("Prerequisite does not exist. Do you want to add as new course?('y' to add): ")
                    if adding_choice == 'y':
                        self.add_course(user_input)
                    else:
                        continue
                prerequisites.append(user_input)
        new_course = course_module.Course(course_code, course_title, course_credit, prerequisites[:])
        self.courses.append(new_course)
        print("Course added!")

    def update_course(self, course_code, course_title, course_credit, prerequisites):
        course = self.search_course(course_code)
        setattr(course, 'course_title', course_title)
        setattr(course, 'course_credit', course_credit)
        setattr(course, 'prerequisites', prerequisites)

    def delete_course(self, course_code):
        for course in self.courses:
            if course_code == getattr(course, 'course_code'):
                self.courses.remove(course)
                print("Course deleted!")
                break
        else:
            print('Course not found!')
    
    def show_all_courses(self):
        if len(self.courses) == 0:
            print("No courses added yet!")
            return None
        for course in self.courses:
            course.show_details()

    def show_one_course(self, course_code):
        if self.search_course(course_code) == None:
            print("Course not found!")
            return None
        course = self.search_course(course_code)
        course.show_details()
