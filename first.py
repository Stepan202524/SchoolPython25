# Анонимные функции (однострочные, безымянные)
# lambda  <Аргументы>: <выражение>
words = ['v','etom', 'spiske', 'slova', 'kotoryx']

is_long_six = lambda word: len(word) > 6

if_first_let_a = lambda word: word[0] == 'a'

#def string_contains = lambda s: 'e' in s
res = list(filter(lambda x: x[0] == 's', words))
print(res)

res1 = list(filter(lambda s: 'e' in s, words))
print(res1)

res2 = list(map(lambda y: y ** 2,range(3, 16)))
num = [3, 4, 5, 6, 7, 8, 9, 10]
res3 = [y ** 2 for y in num]
print(res2, '\n',  res3)

long_word = [word for word in words if len(word) > 4]
print(long_word)

# Создание алфавитов и их объединение
ENGLISH_ABC = [chr(ch) for ch in range(ord('a'), ord('z') + 1)]
RUSS_ABC = [chr(ch) for ch in range(ord('а'), ord('я') + 1)] + ['ё']
ABC = (set(ENGLISH_ABC) ^set(RUSS_ABC) ^ set([x.upper() for x in ENGLISH_ABC]) ^ set([x.upper() for x in RUSS_ABC]))

# удаление пунктуации из строки
text = 'ну и зачем, чтобы, если они.!'       # .lower()   если хотим сделать все маленькие буквы
text = ''.join(filter(lambda x: x in ABC ^ {' '}, text))
print(text)

def remov_punct(text):
    return ''.join(filter(lambda x: x in ABC ^ {' '}, text))

print(remov_punct(text))

def get_words(text: str)  -> list:
    return remov_punct(text).split()

def long_words(text, length=4) -> filter:      # вернёт слова длина которых большеравно 4м
    return filter(lambda word: len(word) >= length, get_words(text))

print(list(long_words(text)))