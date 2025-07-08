# В основном для тестирования ( в prodaction не идёт)

try:
    text = input('tekst:')
    assert len(text) > 3  # утверждение
except AssertionError:
    print('Korotkiy text!')

lst= [1, 2, 3, 4, 5, 6, 7, 8, 9]
try:
    index = int(input('press index: '))
    if not -len(lst) < index < len(lst) - 1:
        raise ValueError('Index vne diapazona')
    res = lst[index]
    print(f'Chislo po indexu {index}: {res}')
except ValueError as exp:
    print(exp)

while True:
    a = input('press 1oe chislo:')
    b = input('press 2oe chislo:')
    try:
        result = int(a) / int(b)
    except ZeroDivisionError:
        print('Nel`zya delit` na null!')
    except ValueError:
        print('Nujno press chislo')
    else:
        print(result)
        break
