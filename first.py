# OOP (специальные методы)  magic methods
# method override, operator overloading
import math
from math import hypot

class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    def __str__(self):
        return f'<Point: ({self.x}, {self.y})>'
    def __repr__(self):
        return f'<List Point: ({self.x}, {self.y})>'
    def __sub__(self, other):
        return (self.x - other.x, self.y - other.y)
      #  return Point(abs(self.x - other.x), abs(self.y - other.y))  Абсолютные значения
    def __add__(self, other):
        return math.hypot(abs(self.x - other.x), abs(self.y - other.y))


p = Point()
p1 = [Point(), Point()]
p2 = Point(5, 8)
p3 = Point(12, 15)
print(p, '\n', p1)
print(f'Raznica koordinat: ', p2 - p3)
print(f'Gipotinuza: ', p2 + p3)