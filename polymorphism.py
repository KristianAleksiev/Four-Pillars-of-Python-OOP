# Polymorphism - Looks the same, behaves differently - (int +) (str +)

class Employee:
    def number_working_hours(self):
        self.number_of_hours = 40

    def display_working_hours(self):
        print(self.number_of_hours)


class Trainee(Employee):
    def number_working_hours(self):
        self.number_of_hours = 45

    def reset_working_hours(self):
        super().number_working_hours() #-> Accessing the number_working_hours method in base class, redefining


employee = Employee()
employee.number_working_hours()
employee.display_working_hours()

trainee = Trainee()
trainee.number_working_hours()
trainee.display_working_hours()

trainee.reset_working_hours()
