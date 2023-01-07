# about object-oriented programming

from enum import Enum


class Person:
    def __init__(self, name, age):  # __init__ is a constructor
        self.name = name
        self.age = age

    def say_hi(self):  # say_hi is a method
        print('Hello, my name is', self.name,
              'and I am', self.age, 'years old.')

    def say_hi_to(self, name):
        print('Hello ' + name + ' my name is', self.name)

# inheritance


class Student(Person):
    def __init__(self, name, age, grade):
        Person.__init__(self, name, age)
        self.grade = grade

    def say_hi(self):
        print('Hello, my name is', self.name,
              'and I am', self.age, 'years old.',
              'I am in grade', self.grade)

# enumeration
# enumeration is a set of symbolic names (members) bound to unique, constant values
# enumeration is a data type that consists of a set of named values called elements or members of the enumeration
# enumeration is a set of symbolic names (members) bound to unique, constant values


class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3


print(Color.RED)
print(Color.RED.name)
print(Color.RED.value)
