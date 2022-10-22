class Course:

    def __init__(self, course_code, course_title, course_credit, prerequisites):
        self.course_code = course_code
        self.course_title = course_title
        self.course_credit = course_credit
        self.prerequisites = prerequisites[:]
    
    def show_details(self):
        print("Course Details:")
        print("---------------")
        print(f"Code: {self.course_code} \nTitle: {self.course_title} \nCredit: {self.course_credit} \nPrerequisites:")
        for prerequisite in self.prerequisites:
            print(prerequisite) 
        if len(self.prerequisites) == 0:
            print('None')
        print('')