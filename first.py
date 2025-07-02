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

num_to_str = {
    0 : 'null',
    1 : 'odin',
    2 : 'dva',
    11 : 'Odinadc`at`',
    20 : 'Dvadcat`',

}
#  Функция, принимающая число и возвращает его словами

def num_to_words(n: int) -> str:
    if len(str(n)) > 2:
        return 'Nujno  ne bol`she 2x znakov'
    if len(str(n)) == 1 or n in num_to_str:
        return num_to_str[int(n)]
    return num_to_str[int(str(n)[0] + '0')] + ' ' + num_to_str[int(str(n)[1])]


print(num_to_words(22))