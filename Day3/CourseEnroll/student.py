from enrollment import Enrollment
class Student:
    def __init__(self,name):
        self.name=name
        self.enrollment=Enrollment()

    def calculate_fees(self):
        return self.enrollment.calculate_total_fees()

    def display_totals(self):
        credits=self.enrollment.calculate_total_credits()
        fees=self.calculate_fees()
        print(f"{self.name}'s total credits: {credits}, Fees: ${fees}")
        self.last_enrolled_course = (
            self.enrollment.courses[-1].name if self.enrollment.courses else None
        )
