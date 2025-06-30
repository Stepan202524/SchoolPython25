# Списки
# Создание аббревиатур

lst = []
while (word := input('please: ').strip().capitalize()) != '':
    lst.append(word[0])  # Добавляем в список первую букву слова
print(f'Poluchilos', end=': ')
print(*lst)

