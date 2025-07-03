# Рекурсия функция вызывает сама себя
def factorial(count):  # 5! = 1 * 2 * 3 * 4 * 5
    res = 1
    for i in range(2, count + 1):
        res *= i
    return res

for x in range(6):
    print(x, factorial(x))


def factor(x):
    if x == 1 or x == 0:              #  Базовый вариант (Окончание функции)
        return 1
    return x * factor(x - 1)

print(f'Factorial ot 5! = ', factor(5))