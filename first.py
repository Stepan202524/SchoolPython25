# break, continue

# Loop's: (циклы)
# while
# for
counter = 0  # обнуляем счётчик
# цикл из 5ти итераций, но 3 пропускаем
while counter < 5:
    counter += 1  # краткая запись бинарным оператором
    if counter == 3:
        continue  # прервать текущую итерацию и начать следующую
    print(f'Iteration number {counter}')
    # counter = counter + 1  # инкремент


