def summ(a, b):
    return a + b
def diff(a, b):
    return a - b

if __name__ == '__first__':
    print('Это библиотека. а исполняемый файл - first')

class Separator:
    def __init__(self):
        self.odd = []
        self.even = []  # чётные

    def add_num(self, num):
        if num % 2:
            self.odd.append(num)
        else:
            self.even.append(num)

    def get_odd(self):
        return self.odd

    def get_even(self):
        return self.even

class Clicker:
    def __init__(self):
        self._counter = 0

    def click(self):
        self._counter += 1

    def get_counter(self):
        return self._counter

    def reset(self):
        self._counter = 0


class Book:
    def __init__(self, title, author):
        self._title = title
        self._author = author

    def get_title(self):
        return self._title
    def get_author(self):
        return self._author

from math import pi
class Circle:
    def __init__(self, radius):
        self.radius = radius
        self.name = 'Kruga'

    def perimetr(self):
        return round(2 * pi * self.radius, 3)

    def area(self):
        return round(pi * self.radius ** 2, 3)

    def get_name(self):
        return self.name


class Rectangle:
    def __init__(self, side1, side2):
        self.side1 = side1
        self.side2 = side2
        self.name = 'Pryamougolnika'

    def perimetr(self):
        return  self.side1 + self.side2

    def area(self):
        return self.side1 * self.side2

    def get_name(self):
        return self.name


class Person:

    def __init__(self, name='Bill', age=11):
        # свойства (поля) класса
        self._name = name
        self._age = age

    # setters
    def set_name(self, new_name):
        if new_name:
            self._name = new_name

    def set_age(self, new_age):
        if 0 < new_age < 100:
            self._age = new_age
        else:
            print('Net takogo vozrasta', new_age)
    #getters
    def get_name(self):
        return self._name

    def get_age(self):
        return self._age

    def person_info(self):
        print(f'Chel s imenem {self._name}. Vozrast: {self._age}')

class Student:
    def __init__(self, name='Bill', univ=''):
        self._name = name
        self._univer = univ

    def get_univer(self):
        return self._name, self._univer

class Employ:
    def __init__(self, name='BMW', comp=''):
        self._name = name
        self._company = comp

    def get_company(self):
        return self._name, self._company