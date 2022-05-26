# Public attributes and methods of the class - Everywhere
# Protected => _variable_name - Within this class and the derived classes
# Private => __variable_name - Within the class

class Car:
    number_of_wheels = 4
    _color = "Black"
    __year = 2017


print("Public attribute 'number_of_wheels'.")
car = Car()


class Bmw(Car):
    def __init__(self):
        print("Protected attribute 'color'")


bmw = Bmw()
print("Private attribute 'year'") #= > car._Car__year


