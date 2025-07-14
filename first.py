# JSON - (Java Script Object Notation)
# Для чтения load() - читает из файла
#           loads() - читает строковое представление
import json

with open('dogs.json', 'rt') as d:
#    data = json.load(d)        # Напрямую из файла
    temp = d.read()             # Читаем файл как строку
    data = json.loads(temp)     # строковое представление JSON
for i in range(len(data)):
    print(f'Pitomec #{i + 1}')
    for a, b in data[i].items():
        if type(b) == list:
            print(f'\t{a}: {','.join(b)}')
        else:
            print(f'{a}: {b}')
# Для одного питомца вывод
# for a, b in data.items():
#     if type(b)  == list:
#         print(f'{a}: {','.join(b)}')
#     else:
#         print(f'{a}: {b}')
print(data)
# Записываем словарь в файл JSON
d = {
    'ананас': 300,
    'банан': 400,
    'яблоко': 150,
    'груша': 250,
}
# Напрямую в файл
# with open('fruits.json', 'w', encoding='utf-8') as f:
#     json.dump(d, f, indent=4)

# Вывод в виде строки
print(json.dumps(d, indent=4))