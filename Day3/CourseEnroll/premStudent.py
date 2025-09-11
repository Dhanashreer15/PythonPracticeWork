from student import Student

class PremiumStudent(Student):
    def calculate_fees(self):
        total_fees=self.enrollment.calculate_total_fees()
        return total_fees * 0.8  # 20% discount

    def display_totals(self):
        credits=self.enrollment.calculate_total_credits()
        fees=self.calculate_fees()
        print(f"{self.name}'s total credits: {credits}, Fees with discount: ${fees:.2f}")
        self.last_enrolled_course = (
            self.enrollment.courses[-1].name if self.enrollment.courses else None
        )
