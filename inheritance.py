# Inheritance - >  Three types

# Single level inheritance

class Apple: #Base class
    manufacturer = "Apple Inc."
    website = "www.apple.com/contact"


class MacBook(Apple): #Derived class

    def __init__(self):
        self.year_of_manufacture = 2017

    def manufacture_details(self):
        print(f"This MacBook was manufactured in the year {self.year_of_manufacture} by {self.manufacturer}")


macbook = MacBook()
macbook.manufacture_details()

# Multiple inheritance - More than one base class


class OperatingSystem:
    multitasking = True
    name = "Mac OS"


class Apple:
    website = "www.apple.com"
    name = "Apple"


class MacBook(OperatingSystem, Apple):
    def __init__(self):
        if self.multitasking:
            print(f"This is a multitasking system. Visit {self.website}")


macbook = MacBook()
        ## If both base classes have same attribute, the attribute is inherited with priority as first defined
        ## self.name => Mac OS


# Multilevel Inheritance


class MusicalInstruments:
    major_keys = 12


class StringInstruments(MusicalInstruments):
    type_wood = "Tonewood"


class Guitar(StringInstruments):
    def __init__(self):
        self.number_of_strings = 6
        print(f"This guitar consists of {self.number_of_strings},\
         it is made of {self.type_wood} and can play {self.major_keys}")

