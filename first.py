# Словари
# Пустой словарь  1. d = {}  2. d = dict()
# Предзаполненный словарь
d = {
    'table': 'таблица',
    'well': ['хорошо', 'колодец', 'скважина'],
    'chair': 'стул',
    'apple': 'яблоко',
    1: 'один',
}
print(d['well'][2], d[1])
d['plum'] = 'слива'# добавление в оперативную память в словарь, после окончания проги предзаполненный словарь останется изначальным
d['well'].append('яма') # добавление элемента в список ключа
del d['chair']
print(d)  # словарь целиком как есть

for key in d:               # Вывод словаря красиво
    print(key, ' =', d[key])

del_item = d.pop('apple')  # Удаление по ключу элемента из словаря
if 'table' in d:
    print('Yes')

for values in d.values():  # Перебор все значений
    print(values)
# d.key() # список ключей (list)
# d.values() # Список значений (list)
# d.items() # список Ключ - Значение (кортежем)

for k, v in d.items():  # Вывод словаря Ключ - Значение
    print(k, v)

pear = d.get('pear', 'Grushi net')  # мягкое обращение к ключу, если нет ключа - выдаст None или 'Grushi net'
print('Gde grusha: ', pear)


""" Методы словаря
'clear', 'copy', 'fromkeys', 'get', 'items', 'keys',
'pop', 'popitem', 'setdefault', 'update', 'values'
"""