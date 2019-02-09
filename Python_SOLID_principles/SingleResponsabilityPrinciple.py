import abc
import math
import pprint
from collections import OrderedDict as ordDict

"""
DRY = Don`t repeat yourself
KISS = Keep It Stupid Simple
SOLID = SRP - Single Responsibility Principle: Every object should have a single resp and
                                               that resp should be entirely encapsulated by the class
      = OCP - Open Closed Principle
      = LSP - Liskov Substitution Principle
      = ISP - Interface Segregation Principle
      = DIP - Dependency Inversion Principle
"""


class GeometricRectangle(metaclass=abc.ABCMeta):
    """Interfaces define the same behavior for different object but with different business logic inside"""
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @abc.abstractmethod
    def calculate_area(self):
        pass

    @abc.abstractmethod
    def calculate_perimeter(self):
        pass


class DrawRectangle(GeometricRectangle):
    """Implements methods to the interface class in order to have different logic for different object"""
    def __init__(self, width, height):
        super(DrawRectangle, self).__init__()
        self.height = height
        self.width = width

    def calculate_area(self):
        if isinstance(self.width, int) and isinstance(self.height, int):
            return {"area": str(self.width * self.height)}
        return ValueError("Input values are not integers!")

    def calculate_perimeter(self):
        if isinstance(self.width, int) and isinstance(self.height, int):
            return {"perimeter": str(2 * (self.width + self.height))}
        return ValueError("ERROR: Input values are not integers!")

    def calculate_diagonal(self):
        if isinstance(self.height, int) and isinstance(self.width, int):
            return {"diagonal": str(math.sqrt(math.pow(self.width, 2) + math.pow(self.height, 2)))}
        return ValueError("ERROR: Input values are not integers!")

    def get_shape_values(self):
        return {"width": self.width, "height": self.height}

    def get_shape_calculated_values(self):
        shapeDict = ordDict()
        shapeDict.setdefault(str(self.get_shape_values()))
        shapeDict.setdefault(str(self.calculate_area()))
        shapeDict.setdefault(str(self.calculate_perimeter()))
        shapeDict.setdefault(str(self.calculate_diagonal()))
        return shapeDict


class DrawSquare(GeometricRectangle):
    def __init__(self, width):
        super().__init__()
        self.width = width

    def calculate_area(self):
        if isinstance(self.width, int):
            return {"area": str(math.pow(self.width, 2))}
        return ValueError("ERROR: Input values are not integers!")

    def calculate_perimeter(self):
        if isinstance(self.width, int):
            return {"perimeter": str(self.width * 4)}
        return ValueError("ERROR: Input values are not integers!")

    def calculate_diagonal(self):
        if isinstance(self.width, int):
            return {"diagonal": str(math.sqrt(2) * self.width)}
        return ValueError("ERROR: Input values are not integers!")


if __name__ == '__main__':
    rectangle = DrawRectangle(3, 5)
    pprint.pprint(rectangle.get_shape_calculated_values())

    square = DrawSquare(4)
    print(square.calculate_area())
    print(square.calculate_perimeter())
    print(square.calculate_diagonal())


