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

# Методы классов                self - ссылка ведёт на определённый адрес оперативный памяти
class Greater:
    def hello(self, name = 'Noname'):
        print('Privet!!', name)

    def Bay(self):
        print('Bay Bay!!')


g = Greater()
g.hello()
g.Bay()

# Методы классов и анализ предыдущих вызовов
class Car:
    def __init__(self):
        print('Konstructor est`')
    def start_engine(self):
        self.engine_on = True

    def drive_to(self, place):
        if self.engine_on:
            print(f'Edem v {place}')
        else:
            print('Ne edem')

car = Car()
car.start_engine()
car.drive_to('gorod')