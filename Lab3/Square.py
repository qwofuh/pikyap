from lab_python_oop.Geometry import shape
from lab_python_oop.Rectangle import Rectangle
from lab_python_oop.Color import Color

class Square(Rectangle):
    SHAPE_TYPE = "Квадрат"

    @classmethod
    def get_shape_type(cls):
        return cls.SHAPE_TYPE

    def __init__(self, color: str, side: int):
        self.color = Color()
        self.color.colorName = color
        self.width = side
        self.height = side

    def __repr__(self):
        return f"{Square.get_shape_type()}, цвет: {self.color.colorName}, сторона: {self.width}, площадь: {self.area()}"
        
