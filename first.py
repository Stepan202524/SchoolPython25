# Функция как объект
# Если функция передаётся в другие функции, получается: Функция высшего порядка

# Функция критерия отбора элементов списка по длине слова
def is_longer(word):
    return len(word) > 4

words = ['v','etom', 'spiske', 'slova', 'kotoryx']
for word in filter(is_longer, words):
    print(word)


def if_est_o(word):
    return word[0] == 's'
res = list(filter(if_est_o, words))
print(res)


def square(num):
    return num ** 2

nums = [1, 2, 3, 4, 5, 6]
squares = map(square, nums)
print(list(squares))