from student import Student
from course import Course
from assessment import Assessment
from quiz import Quiz
from exam import Exam
from project import Project

student = Student("001", "Zahra Ahmadi", "zahra@example.com", ["PY101", "MATH101"])
student.enroll_courses("HTML101")
student.display_info()

course = Course("PY101", "Python Programming", [
    "S001", "S002"], ["QuizObject", "ExamObject", "ProjectObject"])
course.add_student("S003")
course.add_assessments("Quiz")
course.find_assessment("Quiz")
course.display_info()

assessment = Assessment("Quiz 1", 20)
assessment.calculate_percentage(12)
assessment.display_info()

quiz = Quiz("Quiz 2", 20)
quiz.display_info()
quiz.grade_message(15)

exam = Exam("Exam 1", 100)
exam.display_info()
exam.grade_message(30)

project = Project("Project 1", 20)
project.display_info()
project.grade_message(20)
