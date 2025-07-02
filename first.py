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