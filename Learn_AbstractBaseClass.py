# from abc import ABCMeta, abstractmethod
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def printarea(self):
        return 0

class Rectangle(Shape):
    type = "Rectangle"
    # length = int(input("Enter Length \n"))
    # breath = int(input("Enter breath \n"))
    def __init__(self):
        self.length = int(input("Enter Length"))
        self.breath = int(input("Enter Breath"))

    def printarea(self):
        return self.length * self.breath

rect = Rectangle()
print(rect.printarea())