from student import Student
from course import Course

student = Student("001", "Zahra Ahmadi", "zahra@example.com", ["PY101", "MATH101"])
student.enroll_courses("HTML101")
student.display_info()

course = Course("PY101", "Python Programming", [
    "S001", "S002"], ["QuizObject", "ExamObject", "ProjectObject"])
course.add_student("S003")
course.add_assessments("Quiz")
course.display_info()
