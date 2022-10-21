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

    def add_course(self, course_code, course_title, course_credit, prerequisites):
            new_course = course_module.Course(course_code, course_title, course_credit, prerequisites)
            self.courses.append(new_course)

    def update_course(self, course_code, course_title, course_credit, prerequisites):
            course = self.search_course(course_code)
            setattr(course, 'course_title', course_title)
            setattr(course, 'course_credit', course_credit)
            setattr(course, 'prerequisites', prerequisites)

    def delete_course(self, course_code):
        for course in self.courses:
            if course_code == getattr(course, 'course_code'):
                del course
                break
    
    def show_all_courses(self):
        for course in self.courses:
            course.show_details()

    def show_one_course(self, course_code):
        course = self.search_course(course_code)
        course.show_details()
