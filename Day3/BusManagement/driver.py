# Driver class
class Driver:
    def __init__(self,name,employee_id,license):
        self.name = name
        self.employee_id = employee_id
        self.license = license

    def display_details(self):
        print(f"Driver: {self.name}, ID: {self.employee_id}, License: {self.license}")
