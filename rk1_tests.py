import RK1
from operator import itemgetter
import unittest

class tests(unittest.TestCase):
    def test_first(self):
        test_spisok = [(3,3,3),(1,1,1),(2,2,2)]
        sp1 = RK1.first(test_spisok)
        sp2 = sorted(test_spisok, key = itemgetter(2))
        self.assertEqual(sp1,sp2)

    def test_second(self):
        test_spisok = [('Имя1', 1, 'Аудитория1'), ('Имя2', 2, 'Аудитория2'), ('Имя3', 3, 'Аудитория3'), ('Имя4', 4, 'Аудитория3')]
        sp1 = RK1.second(test_spisok)
        sp2 = [('Аудитория1', 1), ('Аудитория2', 2), ('Аудитория3', 7)]
        self.assertEqual(sp1,sp2)

    def test_third(self):
        test_spisok = [('Имя1', 1, 'Аудитория1 да'), ('Имя2', 2, 'Аудитория2'), ('Имя3', 3, 'Аудитория3 да'), ('Имя4', 4, 'Аудитория3 да')]
        sp1 = RK1.third(test_spisok, 'да')
        sp2 = {'Аудитория1 да': ['Имя1'], 'Аудитория3 да': ['Имя3', 'Имя4']}
        self.assertEqual(sp1,sp2)