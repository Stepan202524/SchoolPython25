# OOP (inheritance) - Наследование
# класс, от которого наследуем: Базовый, Родительский, Суперкласс
# класс, который наследуется: Производный, Дочерний

# Абстрактный класс, информирующий какой подкласс используется
class Shape:
    def info(self):
        print(f'Klass: {self.__class__.__name__}')

    def area(self):
        pass

    def perimetr(self):
        pass

# Фигуры
from math import pi
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
        self.name = 'Krug'

    def perimetr(self):
        return round(2 * pi * self.radius, 3)

    def area(self):
        return round(pi * self.radius ** 2, 3)

    def get_name(self):
        return self.name


class Rectangle(Shape):
    def __init__(self, side1, side2):
        self.side1 = side1
        self.side2 = side2
        self.name = 'Pryamougolnik'

    def perimetr(self):
        return  self.side1 + self.side2

    def area(self):
        return self.side1 * self.side2

    def get_name(self):
        return self.name

class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)
    #   self.side = side
        self.name = 'квадрат'

    # def perimetr(self):
    #     return 4 * self.side
    #
    # def area(self):
    #     return self.side ** 2
    #
    # def get_name(self):
    #     return self.name

class Triangle(Square):
    def __init__(self, side):
        super().__init__(side)
        self.side = side
        self.name = 'Треугольник'

    def area(self):
        return (self.side ** 2 * 3 ** 0.5) / 4

    def perimetr(self):
        return self.side * 3


s = Square(5)
print(s.get_name())
print(s.area(), '\t', s.perimetr())
s.info()
c = Circle(4)
print(c.get_name())
print(c.area(), '\t', c.perimetr())
c.info()
tr = Triangle(6)
print(tr.get_name())
print(tr.area(), '\t', tr.perimetr())
tr.info()