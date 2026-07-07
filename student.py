class Student:

    def __init__(self, student_id, student_name, email, courses):
        self.__student_id = student_id
        self.__student_name = student_name
        self.email = email
        self.courses = courses

    @property
    def student_id(self):
        return self.__student_id

    @student_id.setter
    def student_id(self, value):
        self.__student_id = value

    @property
    def name(self):
        return self.__student_name

    @name.setter
    def name(self, value):
        self.__student_name = value

    def set_email(self, email):
        pass

    def enroll_courses(self, course_code):
        self.courses.append(course_code)

    def display_info(self):
        print(f"Student name: {self.__student_name}")
        print(f"Student id: {self.__student_id}")
        print(f"Student email address: {self.email}")
        print(f"Student courses: {self.courses}")
