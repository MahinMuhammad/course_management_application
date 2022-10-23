import json

file_name = 'save.json'

def store_on_file(courses):
    with open(file_name, 'w') as file_object:
        for course in courses:
            json.dump(course.__dict__, file_object)
            file_object.write('\n')
    print("saved!")

def retrive_from_file():
    courses = []
    try:
        with open (file_name, 'r') as file_object:
            for line in file_object:
                courses.append(json.loads(line))
            return courses
    except FileNotFoundError:
        return courses
