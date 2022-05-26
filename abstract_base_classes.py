# Abstracting base class

# class Square:
#     side = 4
#
#     def area(self):
#         print(f"The area is {self.side * self.side}")
#
#
# class Rectangle:
#     width = 5
#     length = 10
#
#     def area(self):
#         print(f"The area is {self.width * self.length}")
#
#
# square = Square()
# rectangle = Rectangle()
# square.area()
# rectangle.area()
####

from abc import ABCMeta, abstractmethod


class Shape(metaclass=ABCMeta):
    @abstractmethod
    def area(self):
        return 0


class Square(Shape):
    side = 4

    def area(self):
        print(f"The area is {self.side * self.side}")


class Rectangle(Shape):
    width = 5
    length = 10

    def area(self):
        print(f"The area is {self.width * self.length}")


square = Square()
rectangle = Rectangle()
square.area()
rectangle.area()
shape = Shape()
