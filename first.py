# Файл
# name.txt
# t - текстовый файл(txt, html, xml)
# b - бинарные файлы(jpg, avi, mp3)
# w - write (открывается на запись и удаляет все записи в нём, Если не было - создаётся файл
# a - append (запись в конец)
# r - read  (чтение, без записи)

# fo = open('info.txt', 'wt', encoding='utf-8')
# print(fo)
# print(fo.mode, fo.name, fo.encoding)
# count = fo.write('Этот текст будет в файле!')
# print('В файл записано', count, 'bytes!')
# fo.close()

# fo = open('info.txt', 'rt', encoding='utf-8')
# text = fo.read(11)                    # Сколько байт читать (3) -
# fo.read(6)                             # Курсор остаётся на месте, после прочтения
# text += fo.read(7)
# print('V fayle zapisano:', end=': ')
# print(text)
# fo.close()

fo = open('info.txt', 'rt', encoding='utf-8')   # Для добавки текста .write писать 'at'
# fo.write(' Хороший текст')            # Добавление в конец текста
# print('\nА вот это будет уже с новой строки.', file=fo)
# print('Ёще одна строка', file=fo)
# text = fo.readline()
# print(text)
# text = fo.readline()
# print(text)
# while text := fo.readline():            # Построчное чтение №1
#     print(text.rstrip('\n'))
# lst = fo.readlines()                    # Построчное чтение №2
# lst = list(map(lambda x: x.strip('\n'), lst))
# print(lst)
# text = fo.read()                        # Третий вариант №3
# lst = text.splitlines()
# print(lst)
fo.close

# Открытие с менеджером контекста
with open('info.txt', 'rt', encoding='utf-8') as fo:
    text = fo.read()
    lst = text.splitlines()
    print(lst)
# Проследит, чтобы файл закрылся