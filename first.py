# Iterable object
# len() - сколько элементов в объекте
a = 123456  # int - не является iterable
lenght = len(str(a))  # поэтому конвертируем в str
print(lenght)

word = input(' please word for analys:')
if not word or len(word) < 3:
    print('Net slova or small')
