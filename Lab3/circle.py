import math

from lab_python_oop.Geometry import shape
from lab_python_oop.Color import Color

class Circle(shape):
    SHAPE_TYPE = "Круг"

    @classmethod
    def get_shape_type(cls):
        return cls.SHAPE_TYPE

    def __init__(self, color: str, radius):
        self.color = Color()
        self.color.colorName = color
        self.radius = radius

    def area(self):
        if type(self.radius) not in [int,float]:
            raise TypeError
        if self.radius < 0:
            raise ValueError
        return math.pi * self.radius**2

    def __repr__(self):
        return f"{Circle.get_shape_type()}, цвет: {self.color.colorName}, радиус: {self.radius}, площадь: {self.area()}"
        
