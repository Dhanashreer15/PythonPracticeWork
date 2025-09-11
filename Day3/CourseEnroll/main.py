from course import Course
from enrollment import Enrollment
from student import Student
from premStudent import PremiumStudent

if __name__ == "__main__":
    # Courses
    python_course=Course("Python Programming", "CS101", 3, 400)
    data_science=Course("Data Science 101", "DS201", 6, 800)
    ml_course=Course("Machine Learning", "ML301", 3, 600)

    # Students
    alice=Student("Alice")
    bob=PremiumStudent("Bob")

    # Alice enrolls
    alice.enrollment.enroll_course(python_course)
    alice.enrollment.enroll_course(data_science)
    alice.enrollment.enroll_course(ml_course)
    alice.enrollment.drop_course("DS201")
    alice.display_totals()

    # Bob enrolls
    bob.enrollment.enroll_course(data_science)
    bob.enrollment.enroll_course(ml_course)
    bob.display_totals()

    # Dynamic attribute check
    print(f"Last course Alice enrolled: {alice.last_enrolled_course}")
    print(f"Last course Bob enrolled: {bob.last_enrolled_course}")
