# Анонимные функции (однострочные, безымянные)
# lambda  <Аргументы>: <выражение>
# проверка коллекций: any(), all()

# any - любой элемент коллекции вернул True
# all - все элементы коллекции вернули True

print(all([1, 2, 3]))  # все элементы ненулевые
print(all([1, 2, 0]))  # один элемент нулевой

# проверка всех слов из списка по длине слов
words = 'Odin dva tri'.split()
list_for_ana = list(map(lambda x: len(x) > 3, words))
print(list_for_ana, all(list_for_ana), any(list_for_ana))