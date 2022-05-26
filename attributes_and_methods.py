### Class attributes and instance attributes

## Class attributes - For every object created from the class the value of the presets will be the same

class Employee:
    working_hours = 40


employee_one = Employee()
employee_two = Employee()
print(employee_one.working_hours == employee_two.working_hours) # => True

## Changing the Class attributes
Employee.working_hours = 45

## Changing the instance attribute
employee_one.working_hours = 45

## The "self" parameter

# def EmployeeDetails():
#     pass
# employee = Employee()
# employee.EmployeeDetails()
# Employee.employeeDetails(employee) #=> self => def EmployeeDetails(self):

## Static methods


class Employee:

    @staticmethod
    def welcome_message():
        print("Welcome to our organization!")