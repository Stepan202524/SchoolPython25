# Функции
# Области видимости
PI = 3.14       # Глобальная переменная


def circle_len(radius: float):
    """
    :param radius:
    :return:
    """
    perimetr = 2 * PI * radius
    print(f'Dlina kruga s radiusom {radius} = {perimetr:.3f}')


def print_array(array: list) -> None:
    for item in array:           # Использование внешней(глобальной) переменной Недопустимо (вместо array -- words)
        print(item)


def greet(name: str):
    print('Privet', name)
    name = 'drug'
    print('Zdarova', name)


def main():
    circle_len(3)
    words = ['privet', 'mir']   # Все переменные в функции - локальные
    print_array(words)
    print_array(['a', 'b', 'c'])
    greet('Fedya')


main()      # Вызываем главную функцию и она уже выводит на экран