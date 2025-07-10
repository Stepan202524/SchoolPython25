# OOP  (Полиморфизм) - свойства кода работать с разными типами данных
# method override;  operator overloading
# isinstance (объект, тип) -> True
# isinstance (объект, (тип 1, тип 2, тип N)) -> True

from lib import Book
book = Book('Язык С++', 'Бьярн')
print(f'{book.get_title(), book.get_author()}')
############
from lib import Circle, Rectangle


def shape_info(shape: object):
    print(f'Plowad {shape.get_name()} : {shape.area()}, Perimetr {shape.get_name()}: {shape.perimetr()}')


rect, c = ['Прямоугольника', 'Круга']
fir = ''
def shape_info1(shape: object):
    if isinstance(shape, Circle):
        fig = c
    elif isinstance(shape, Rectangle):
        fig = rect
    print(f'Plowad` {fig} : {shape.area()}, Perimetr {fig}: {shape.perimetr()}')


r = Rectangle(10, 5)
shape_info(r)
cr = Circle(10)
shape_info(cr)
shape_info1(r)
shape_info1(cr)
###########
from lib import Person, Student, Employ
people = [
    Person('Alexander', 22),
    Student('Dima', 'GUAP'),
    Employ('Petya', 'BMW')
]
for person in people:
    if isinstance(person, Student):
        print(person.get_univer())
    elif isinstance(person, Employ):
        print(person.get_company())
    else:
        print(person.get_name(), person.get_age())
############
lst = list(range(1, 15))
# Разбиваем список на чётные и нечётные
class Selector:
    def __init__(self, vals):
        self._values = vals[:]      # получаем копию, чтобы не изменять начальный список
    def get_odd(self):
        return [x for x in self._values if x % 2] # остаток от деления
    def get_even(self):
        return [x for x in self._values if x % 2 == 0]

s = Selector(lst)
print(f'Nechet: ', s.get_odd())
print(f' Chet: ', s.get_even())
print(f'Ves spisok: ', lst)
#############
# lst += ['a']
class Stat:
    def __init__(self, vals):
        self._values = vals[:]
    def is_int(self) -> bool:
        return all(isinstance(item, int) for item in self._values)
    def get_min(self):
        if self.is_int():
            return min(self._values)
        return None
    def get_max(self):
        if self.is_int():
            return max(self._values)
        return None
    def get_aver(self):
        if self.is_int():
            return sum(self._values) / len(self._values)
        return None

st = Stat(lst)
print(st.get_min())
print(st.get_max())
print(st.get_aver())