class Enrollment:
    def __init__(self):
        self.courses = []

    def enroll_course(self,course):
        if course in self.courses:
            print(f"Already enrolled in '{course.name}'.")
        else:
            self.courses.append(course)
            print(f"Enrolled '{course.name}'.")

    def drop_course(self, course_code):
        for course in self.courses:
            if course.code == course_code:
                self.courses.remove(course)
                print(f"Dropped '{course.name}' from courses.")
                return
        print(f"Course with code '{course_code}' not found in enrollment.")

    def calculate_total_credits(self):
        return sum(course.credits for course in self.courses)

    def calculate_total_fees(self):
        return sum(course.get_fee() for course in self.courses)

