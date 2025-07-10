# OOP (специальные методы)  magic methods
# method override, operator overloading

class MyTime:
    def __init__(self, minutes, seconds):
        if 0 <= minutes < 60:
            self.minutes = minutes
        if 0 <+ seconds < 60:
            self.seconds = seconds

    def __str__(self):
        return f'Minute {self.minutes:02}: Seconds {self.seconds:02}'

    def __add__(self, other):
        return f'Minut {self.minutes + other.minutes} : Secund {self.seconds + other.seconds}'

t1 = MyTime(18, 55)
t2 = MyTime(22,4)
print(t1, '\t', t2)
print(f'Summa vremeny = ', t1 + t2)
#############

# __call__ - экземпляр класса вызываем как функцию
# y = ax^2 + bx + c
class SquareFunc:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def __call__(self, x):
        return self.a * x ** 2 + self.b * x + self.c

s = SquareFunc(1, 2, 3)
print(f'Uravnenue: y = ax^2 + bx + c = ', s(2))