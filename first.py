# Строки (immutable, iterable)
# Начало и окончание строки startswith endswith
s = 'Смотреть, вертеть, видеть'
if s.lower().startswith('смо'):
    print('Yes')
if s.endswith('еть'):
    print('Ye')
# find('подстрока')
# find('подстрока',start) поиск с начало строки s с позиции start
# find('подстрока', 10, 15) поиск с позиции 10 и до позиции 15
index = s.find('еть')  # возвращает первое появление 'еть' поиск с начала строки s
print(index)
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
