# Строки (immutable, iterable)
#
alphab = 'абвгдеёжзийклмнопрстуфхцшщъэюя'
# alphab_u += alphab.upper()   добавляем Заглавные буквы и тогда надо убрать .lower()
mess = input('Stroka: ').strip().lower()  # убираем пробелы и делаем все буквы малыми
key = int(input('key: '))
crypt = ''
for lett in mess:    # перебираем каждый символ
    if lett in alphab:  # проверка символа как буква из алфавита
        t = alphab.index(lett)   # находим позицию буквы в алфавите
        newkey = (t + key) % len(alphab) # шифровка Вычисляем новую позицию с учётом сдвига (с остатком от деления)
        # newkey = (t - key) % len(alphab)  - расшифровка
        crypt += alphab[newkey]
    else:
        crypt += lett
print('Шифр: ',crypt)