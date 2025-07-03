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