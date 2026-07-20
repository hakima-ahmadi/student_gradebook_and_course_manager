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
    print("3. Search student")
    print("4. Delete student")
    print("5. Add course")
    print("6. Enroll student in course")
    print("7. Add assignment")
    print("8. Record grade")
    print("9. Calculate average and result")
    print("10. View student report")
    print("0. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        student_id = input("Student ID: ")
        name = input("Student name: ")
        email = input("Email: ")

        student = Student(student_id, name, email, [])
        gradebook.add_student(student)

    elif choice == "2":
        if len(gradebook.students) == 0:
            print("No students found.")
        else:
            for student in gradebook.students.values():
                student.display_info()

    elif choice == "3":
        keyword = input("Enter student name or ID: ")
        gradebook.search_student(keyword)

    elif choice == "4":
        student_id = input("Student ID: ")
        gradebook.delete_student(student_id)

    elif choice == "5":
        course_code = input("Course Code: ")
        course_name = input("Course Name: ")
        course = Course(course_code, course_name, [], [])
        gradebook.add_course(course)

    elif choice == "6":
        student_id = input("Student ID: ")
        course_code = input("Course Code: ")
        gradebook.enroll_student(student_id, course_code)

    elif choice == "7":
        course_code = input("Course Code: ")
        assessment = input("Assessment Title: ")
        gradebook.add_assessment(course_code, assessment)

    elif choice == "8":
        student_id = input("Student ID: ")
        course_code = input("Course Code: ")
        assessment = input("Assessment Title: ")
        score = int(input("Score: "))
        gradebook.record_grade(student_id, course_code, assessment, score)

    elif choice == "9":
        student_id = input("Student ID: ")
        course_code = input("Course Code: ")

        average = gradebook.calculate_average(student_id, course_code)
        print("Average:", average)
        print(gradebook.get_result(average))

