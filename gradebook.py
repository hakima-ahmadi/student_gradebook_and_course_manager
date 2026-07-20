class Gradebook:

    def __init__(self, students, courses, grades, passing_grade):
        self.assessments = None  # list
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
        if student_id not in self.students:
            print("Student not found.")
            return
        if course_code not in self.courses:
            print("Course not found.")
            return
        assessment = self.courses[course_code].find_assessment(assessment_title)
        if assessment is None:
            print("Assessment not found")
            return

        if student_id not in self.grades:
            self.grades[student_id] = {}
        if course_code not in self.grades[student_id]:
            self.grades[student_id][course_code] = {}
        self.grades[student_id][course_code][assessment_title] = score

        print(f"Student {student_id} gets {score} in {assessment_title} for course {course_code}.")

    def calculate_average(self, student_id, course_code):
        if student_id not in self.grades:
            print("No grade found")
            return
        if course_code not in self.grades[student_id]:
            print("No grades found for this course")
            return
        scores = self.grades[student_id][course_code].values()
        return sum(scores) / len(scores)

    def show_report(self, student_id):
        if student_id not in self.students:
            print("Student not found.")
            return
        student = self.students[student_id]
        for course_code in self.grades[student_id]:
            average = self.calculate_average(student_id, course_code)
            result = self.get_result(average)
            course = self.courses[course_code]
            print(f"{student.name}'s report shows that his {course.course_name} "
                  f"average is {average} and his result is {result}.")

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
        if student_id in self.grades:
            del self.grades[student_id]
        for course in self.courses.values():
            if student_id in course.students:
                course.students.remove(student_id)
                print(f"{student_id} student deleted successfully.")

    def get_result(self, average):
        if average is None:
            return "No grade found"
        if average >= self.__passing_grade:
            return "Student passed!"
        else:
            return "Student failed!"

    def get_letter_grades(self, average):
        if average >= 90:
            return "A"
        elif average >= 80:
            return "B"
        elif average >= 70:
            return "C"
        elif average >= 60:
            return "D"
        else:
            return "F"

    def teacher_comment(self, comment):
        print(f"Teacher comment: {comment}")

    def dashboard(self):
        print(f"Total student: {len(self.students)}")
        print(f"Total courses: {len(self.courses)}")

