class Gradebook:

    def __init__(self, students, courses, grades, passing_grade):
        self.students = students  # dictionary
        self.courses = courses  # dictionary
        self.grades = grades  # dictionary
        self.__passing_grade = passing_grade

    @property
    def passing_grade(self):
        return self.__passing_grade

    @passing_grade.setter
    def passing_grade(self, value):
        if value < 0:
            print("Passing grade cannot be negative!")
        self.__passing_grade = value

    def add_student(self, student):
        if student.student_id in self.students:
            print("Student already exists!")
            return
        self.students[student.student_id] = student
        print("Student added!")

    def add_course(self, course):
        if course.course_code in self.courses:
            print("Course already exists!")
            return
        self.courses[course.course_code] = course
        print("Course added!")

    def enroll_student(self, student_id, course_code):
        if student_id not in self.students:
            print("Student not found!")
            return
        if course_code not in self.courses:
            print("Course not found")
            return
        student = self.students[student_id]
        course = self.courses[course_code]
        student.enroll_courses(course_code)
        course.add_student(student_id)
        print(f"Student {student_id} is enrolled in course {course_code} successfully.")

    def add_assessment(self, course_code, assessment):
        if course_code not in self.courses:
            print("Course not found.")
            return

        course = self.courses[course_code]
        course.add_assessments(assessment)
        print(f"{assessment} added to the course {course_code}")

    def record_grade(self, student_id, course_code, assessment_title, score):
        pass

    def calculate_average(self, student_id, course_code):
        pass

    def show_report(self, student_id):
        pass

    def search_student(self, keyword):
        for student in self.students.values():
            if keyword.lower() in student.name.lower() or keyword.lower() in student.student_id.lower():
                student.display_info()
                return
        else:
            print("Student not found.")

    def delete_student(self, student_id):
        if student_id not in self.students:
            print("Student not found.")
            return
        del self.students[student_id]
        print("Student deleted.")
        if student_id in self.grades:
            del self.grades[student_id]
            print("Yes student deleted.")
        for course in self.courses.values():
            if student_id in course.students:
                course.students.remove(student_id)
                print(f"{student_id} student deleted successfully.")

    def get_result(self, average):
        if average >= self.__passing_grade:
            print("Student passed!")
        else:
            print("Student failed!")
