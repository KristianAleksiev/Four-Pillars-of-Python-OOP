class Employee:
    def employee_detais(self):
        self.name = "Mark"

    def display_employee_details(self):
        print(self.name)


employee = Employee()
employee.display_employee_details()
# AttributeError: 'Employee' object has no attribute 'name'

# Initialize the data attributes

def __init__(self): # Object initialized
    self.name = "Mark"

