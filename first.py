# Функция с переменным числом аргументов (с числами)
def multy(*args):       # Функция выводит в кортеж
    print(len(args))    # подсчёт числа аргументов (длина)
    print(args)         # по индексу, либо перебором в цикле (кортеж)
    res = 1
    for arg in args:
        res *= arg      # произведение аргументов
    return res

# multy(1, 2)
print(multy(1, 2, 4))


def fio(name, surname):     # именованные аргументы
    return f'{name} {surname}'

print(fio('Ostap', 'Bender'))


def calc(*args, oper):
    # match oper:
    #     case '+':
    #         res = 0
    #         for i in args:
    #             res += i
    #     case '*':
    #         res = 1
    #         for i in args:
    #             res *= i
    # return res
    if oper == '+':
        res = 0
        for arg in args:
            res += arg          # Сложение аргументов
        return res
    else:
        res = 1
        for arg in args:
            res *= arg          # Умножение аргументов
        return res

print(calc(1, 2, 4, oper = '+'))

            # Позиционные | Именованные
def print_any(*args, **kwargs):
    for i in args:
        print(i)
    for k, v in kwargs.items():
        print(k, '=', v)

print_any(18, 9, name = 'Dima', age =27)


def profile(name, surname, city, *child, **dopol):
    print(f'Imya: {name}')
    print(f'FIO: {surname}')
    print(f'Gorod: {city}')
    if len(child) > 0:
        print('Dety:', ', '.join(child))
    # print('Hobby: ', end=': ')
    print('Hobby:', dopol['hobby'])

profile('Dima', 'Kolesov', 'SPB', 'Petya', 'Oleg', hobby=['Chess', 'Fizra'] )