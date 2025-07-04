# import math as m              # Импорт библиотеки math (динамически)
from math import pi, sqrt, sin, radians       # Импорт конкретной функции из библиотеки
print('Chislo PI: ',round(pi, 6) , '\nKoren 9 = ', sqrt(9),
      '\nSin 30gr = ', round(sin(radians(30)), 2))

import random

for _ in range(6):
    num = random.randint(0, 10)
    print(num)

print('\n', random.randrange(0, 10, 2))   # Вывод чётных (с шагом 2)

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for _ in range(5):
    res = random.choice(lst)
    print('\t', res, '\t', random.choice(['Orel', 'Reska']))

d = {'a': 1.5, 'b': 2, 'c': 3.8, 'd': 4.1}
keys = list(d.keys())
for _ in range(5):          # Вывод случайных элементов из словаря по ключу
    key = random.choice(keys)
    print(d[key])

zara = ['\u2680', '\u2681', '\u2682', '\u2683', '\u2684', '\u2685', '\u2686']  # кубики (кости)
for _ in range(6):
    print('\t', random.choice(zara), random.choice(zara))

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for _ in range(5):
    res = random.sample(lst, k=5)       # Случайная выборка уникальных элементов(без повторов), к - кол-во элементов
    print(res)

abc = 'sfnwohngjaignrbgirlanaliugiurahafo'
lst = list(abc) + ['4', '7'] + ['^', '$']
random.shuffle(lst)                      # Случайное перемешивание (перетасовка)
lst1 = ''.join(lst[:8])                  # Создание случайного пароля длиной 8 символов
print('\t\t',lst1)

