from student import Student
from course import Course
from assessment import Assessment
from quiz import Quiz
from exam import Exam
from project import Project
from gradebook import Gradebook

students = {}
courses = {}
grades = {}

gradebook = Gradebook(students, courses, grades, 55)

while True:
    print("==========Student Gradebook Manager==========")
    print("1. Add student")
    print("2. View students")
    print("3. Add course")
    print("4. Search student")
    print("5. Delete student")
    print("6. Add course")
    print("7. Enroll student in course")
    print("8. Add assignment")
    print("9. Record grade")
    print("10. Calculate average and result")
    print("11. View student report")
    print("0. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        student_id = input("Student ID: ")
        name = input("Student name: ")
        email = input("Email: ")

        student = Student(student_id, name, email, [])
        gradebook.add_student(student)








