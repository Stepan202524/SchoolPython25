# Методы строки split() и join()

text = 'один два три пять'
# split() - расщипляет строку на элементы и возвращает списком и только списком
lst = text.split() # все символы пустого пространства
ip = '192.168.0.3'
lst1 = ip.split('.')
print(lst, lst1)

text2 = '-'.join(lst1) # соединяет список из строковых значений Join работает только для списков из строк
print(text2)

text3 = '  P y  t h    o   n   '
res = ''.join(text3.split())  # убрать все пробелы
print(res)
# Фраза: ну я типа вообще короче не понимаю этот язык
stop_words = ['ну', 'типо', 'короче']
text = ''
lst2 = ''
while (message := input('Сообщение: ')) != '':
    lst2 = message.split()
for item in lst2:
    if item in stop_words:
        item = ''
    else:
        text += item + ' '
        res = ''.join(text.split())
print(res)
for a, b in enumerate(res, 1):
    print(f'{a}. {b}')