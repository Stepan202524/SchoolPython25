# Строки (immutable, iterable)
# Начало и окончание строки startswith endswith
s = 'Смотреть, вертеть, видеть'
if s.lower().startswith('смо'):
    print('Yes')
if s.endswith('еть'):
    print('Ye')
index = s.find('еть')  # возвращает первое появление 'еть' поиск с начала строки s
print(index)

# find('подстрока')
# find('подстрока',start) поиск с начало строки s с позиции start
# find('подстрока', 10, 15) поиск с позиции 10 и до позиции 15
s1 = 'синхрофазотрон'
ch = 'о'
if ch in s1:
    count = s1.count(ch)
    print(f'Буква {ch} столько раз {count} в слове {s1}')
    print(f'position: ', end='')
    start = 0
    for i in range(count):
        pos = s1.find(ch, start)
        start = pos + 1
        print(pos)
else:
    print(f'Буквы {ch} нет в слове {s1}')

# replace('что', 'на что') - полная замена
# replace('что', 'на что', сколько раз)  - число замен
s = '+7-012-345-67-89'
res = ''
res = s.replace('-',' (', 1)
res = res.replace('-',') ', 1)
print(res)
