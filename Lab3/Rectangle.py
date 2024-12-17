from lab_python_oop.Geometry import shape
from lab_python_oop.Color import Color

class Rectangle(shape):
    SHAPE_TYPE = "Прямоугольник"

    @classmethod
    def get_shape_type(cls):
        return cls.SHAPE_TYPE

    def __init__(self, color: str, width: int, height: int):
        self.color = Color()
        self.color.colorName = color
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def __repr__(self):
        return f"{Rectangle.get_shape_type()}, цвет: {self.color.colorName}, ширина: {self.width}, высота: {self.height}, площадь: {self.area()}"
        
