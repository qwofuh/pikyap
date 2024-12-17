import unittest
from lab_python_oop.circle import Circle
from math import pi


class TestArea(unittest.TestCase):

    def test_area(self):
        self.assertEqual(Circle("Зеленый", 2).area(), pi*2**2)
        self.assertEqual(Circle("Зеленый", 0).area(), 0)
        self.assertEqual(Circle("Зеленый", 1).area(), pi)
        self.assertEqual(Circle("Зеленый", 1.1).area(), pi*1.1**2)

    def test_negative(self):
        with self.assertRaises(ValueError):
            Circle("Зеленый", -1).area()
        with self.assertRaises(ValueError):
            Circle("Зеленый", -2).area()

    def test_type(self):
        with self.assertRaises(TypeError):
            Circle("Зеленый", 'alo').area()
        with self.assertRaises(TypeError):
            Circle("Зеленый", 3+5j).area()
        with self.assertRaises(TypeError):
            Circle("Зеленый", [10]).area()