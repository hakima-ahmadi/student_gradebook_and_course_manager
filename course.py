class Course:

    def __init__(self, course_code, course_name, students, assessments):
        self.__course_code = course_code
        self.__course_name = course_name
        self.students = students  # list
        self.assessments = assessments  # list

    @property
    def course_code(self):
        return self.__course_code

    @course_code.setter
    def course_code(self, value):
        self.__course_code = value

    @property
    def course_name(self):
        return self.__course_name

    @course_name.setter
    def course_name(self, value):
        self.__course_name = value

    def add_student(self, student_id):
        self.students.append(student_id)

    def add_assessments(self, assessment):
        self.assessments.append(assessment)

    def find_assessment(self, title):
        for assessment in self.assessments:
            if assessment.title == title:
                return assessment
            else:
                return f"No assessment found with {title}"

    def display_info(self):
        print(f"Course code: {self.__course_code}")
        print(f"Course name: {self.__course_name}")
        print(f"Enrolled students: {self.students}")  # must print the number of students
