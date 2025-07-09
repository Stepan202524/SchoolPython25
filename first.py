# OOP  (encapsulation)
# Свойства классов
class Fruit:
    pass


a = Fruit()
b = Fruit()

a.name = 'Яблоко'
a.weigth = 120
b.name = 'Груша'
b.weight = 150
print(a.name, '\t', a.weigth, '\t\t', b.name, b.weight)

# self - это контекстный объект, через который передаётся вызванный метод класса,
# через него интерпретатор понимает, какой объект вызвал метод
# self - ссылка ведёт на определённый адрес оперативный памяти,ячейка памяти переменной с именем g

# Методы классов

class Greater:
    def hello(self, name = 'Noname'):
        print('Privet!!', name)

    def Bay(self):
        print('Bay Bay!!', '\n')


g = Greater()
g.hello()
g.Bay()

# Методы классов и анализ предыдущих вызовов
class Car:
    counter = 0     # статичное свойство (счётчик)

    def __init__(self, brand='NoName', model='NoName', color='NoName'):
        self.engine_on = False
        self.brand = brand    # 'Skoda'
        self.model = model    #'Oktavia'
        self.color = color      #'red'
        Car.counter += 1

    def start_engine(self):
        self.engine_on = True

    def drive_to(self, place):
        if self.engine_on:
            print(f'Edem v {place} na {self.brand} {self.model} {self.color}')
        else:
            print('Ne edem')

    @staticmethod
    def get_counter():
        return Car.counter


car = Car('BMW', '535i', 'black')
car.start_engine()
car.drive_to('gorod')
car1 = Car()
car2 = Car()
print('В парке машин:', Car.get_counter(), '\n')

# Геттеры и сеттеры
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


p = Person()
p.set_age(111)
p.person_info()
print(p.get_name(), 'emu stol`ko let', p.get_age())