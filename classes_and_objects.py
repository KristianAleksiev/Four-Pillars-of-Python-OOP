# Classes - Logical collection of attributes and methods

# Noun = > Class
# Adjective => Attributes
# Verb => Method

# check if an employee has achieved his weekly target or not

class Employee:
    def __init__(self, name, sales):
        self.name = name
        self.designation = "Sales Executive"
        self.weekly_sales = sales
        self.target = 5000

    def achieved_target(self):
        if self.weekly_sales < self.target:
            return False
        else:
            return True


employee = Employee(name="Maria", sales=4000)  # Object instantiation
print(employee.achieved_target())
