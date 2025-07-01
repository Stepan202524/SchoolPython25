# Списочные выражения (list comprehension)
# Список квадратов чисел от 0 до 9
squar = [i**2 for i in range(10)]
print(*squar, sep=', ')

# Список чётных чисел
squar = [i**2 for i in range(10) if i % 2 == 0]
        # что|   закон          |  условие
print(*squar, sep=', ')

# произведение i и j
print([i * j for i in range(3) for j in range(3)])

# перевод строки в список чисел (можно присвоить переменной)
n = '500 600 700 800 900'
app = ['500', '800'] # исключения| условие  |
print([int(i) for i in n.split() if i not in app])

# занести в список каждое третье слово из предложения
text = 'Каждое третье слово из этого бреда что зачем куда'
print(*[a for a in text.split()[2::3]])
                            # срез с третьего слова с шагом 3 слова