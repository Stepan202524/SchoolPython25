# Строки (immutable, iterable)
# Методы строк
phrase = 'Язык Python'
print(phrase.lower())  # все маленькие
print(phrase.upper())  # все большие
print(phrase.capitalize())  # только первая заглавная
print(phrase.title())  # все слова заглавные
print('Телевизор'.count('е')) # сколько букв в слове
print('Телевизор'.index('з')) # возвращает индекс буквы в слове

# Повтор каждой буквы слова столько раз, какой её номер в строке начиная с первой
word = 'статор'
for i in range(len(word)):
    print(word[i] * (i + 1), end='')

print(word.strip())  # убираем лишние пробелы до и после слова