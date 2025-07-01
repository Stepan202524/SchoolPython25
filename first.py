# Функции
# Return Value
def square(num):
    return num ** 2

                                    # После return функция останавливается (подобно break в цикле)
def even_odd(num):
    if num % 2 == 0:
        return 'Chetnoe'
    return 'NotCHetnoe'


t = square(5)
print(t)

print(even_odd(10))