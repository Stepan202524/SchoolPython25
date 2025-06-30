# Списки

# lst = []   # empty список
lst = [1, 2, 3] * 3
print(lst, list('Python'))

s1 = [1, 2, 3]
s2 = [4, 5, 6]
s1.extend(s2) # сложение двух списков
s1 += [7]     # добавление в список значение 7
s1[0] = 22    # изменить 1ый элемент на 22
print(s1)

lst1 = list(range(10))
slice = lst1[1:len(lst1):2]
for item in lst1:
    print(item, '-', item ** 2)
for item in range(0, len(lst1)):
   print(lst1[item], '=', lst1[item] * 2)

lst2 = [1, 2, 2, 3, 4, 5, 6]
lst2.remove(2)  # удаляет первый попавшийся элемент 2
print(lst2)
lst2.pop(4)     # удаляет элемент после элемента 4
print(lst2)
lst2.append(2)  # добавляет в конец списка элемент 2
print(lst2)

a = ['a', 'b', 'c']
b = a.copy()
b.append('d')
print(a, '=', b)

lst4 = []
while (item := input('please ingredients: ')) != '':
    lst4.append(item)
print(f'Stolko ingredients: {len(lst4)}')
temp = set(lst4) # перевод во множества
lst4 = list(temp)
lst4.sort()   # сортировка по алфавиту
for i in range(len(lst4)):
    print(f'\t{i + 1}. {lst4[i]}')

# имитация stack
lst5 = []
N = 5
for i in range(N):
    print(f'Kladem knigu {i + 1} .')
    lst5.append(i + 1)
print('---')
while lst5:
    item = lst5.pop()
    print(f'Zabiraem rnigu {item} .')
#while (item := input('please knigi: ')) != '':
#    lst5.append(item)
#print(f'Stolko knig: {len(lst5)}')
#for d in range(len(lst5)):
#    lst5 = lst5.pop(len(lst5 - 1))
#    print (f'остались: {lst5}')