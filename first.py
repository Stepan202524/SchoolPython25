# Строки (immutable, iterable)
s = 'Python'
print(s[0])  # вывод значения по индексу, индекс может быть отрицательным (отсчёт с конца строки)
print(f'Dlina stroki: {len(s)}')
v = 0
for ch in s:
    if ch in {'a', 'e', 'i', 'o', 'y'}:  # или if ch in 'aeioy'
        v += 1
print(f' Number glasnyx v stroke "{s}" = {v}')

# перебор строки по  числовому индексу
for index in range(len(s)):
    print(s[index])
# замена символа в строке по индексу
d = 'sabaka'
res = ''
for i in range(len(d)):
    if i == 1:
        res += 'o'
    else:
        res += d[i]
print(res)