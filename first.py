# Оператор is: a is b -> когда a и b -один и тот же объект
my_refr = ['Kolbas', 'Sblr', 'Maslo']
his_refr = ['Kolbas', 'Sblr', 'Maslo']
print(my_refr == his_refr)  # Сравнение содержимого объектов
print(my_refr is his_refr)  # Сравнение объектов
print(id(my_refr) == id(his_refr))  # Сравнение id-адресов


def print_array(array: list, start: int = None):
    if start is None:
        for i in array:
            print(i)
    else:
        for i in range(start, len(array)):
            print(array[i])


a = [1, 2, 3]
print_array(a, 1)


# Возврат нескольких значений из функции
def coord() -> tuple:
    return 5.4, 3.2, 3.8, 7.2, 9.9


x, y, *rest = coord()  # Распаковка (При распаковке * может быть ТОЛЬКО ОДНА)
print(f'x = {x}, y = {y}, rest = {rest}')  # Остаток rest (в список)
