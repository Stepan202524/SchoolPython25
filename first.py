# Вложенные циклы
p = 0
for i in range (1, 10):
    for j in range (1, 10):
        p = i * j
        print(f'{i} * {j} = {p}', end='\n\t')
    print()
