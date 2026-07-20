from student import Student
from course import Course
from assessment import Assessment
from quiz import Quiz
from exam import Exam
from project import Project
from gradebook import Gradebook

student = Student("001", "Zahra Ahmadi", "zahra@example.com", ["PY101", "MATH101"])
student.enroll_courses("HTML101")
student.display_info()
result = student.set_email("example@gmail..com")
print(result)

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


gradebook = Gradebook(
    {
        "S001": Student("S001", "Ali", "ali@gmail.com", [])
    },
    {
        "PY101": Course("PY101", "Python Programming", [], [])
    },
    {
        "S001": {
            "PY101": {
                "Quiz 1": 85,
                "Midterm Exam": 78,
                "Final Project": 92,
            }
        }
    },
    60
)
gradebook.add_student(Student("S004", "Elham", "elham@gmail.com", []))
gradebook.add_course(Course("PY101", "Python Programming", [], []))
gradebook.enroll_student("S004", "PY101")
gradebook.add_assessment("PY101", "Project 2")
gradebook.record_grade("S001", "PY101", "Project 2", "70")
gradebook.calculate_average("S001", "PY101")
gradebook.show_report("S001")
gradebook.search_student("Elham")
gradebook.delete_student("S004")
gradebook.get_result(55)





