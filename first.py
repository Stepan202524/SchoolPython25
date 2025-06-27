# Строки (immutable, iterable)
# Таблица символов
s ='\xB0'
u = '\u2603' # в 16тиричной системе

print(u)
print('25' + s + 'C')
print(f'Kod symbola ☃ UNICODE: {ord('☃')}')
# ord(символ) - возвращает код символа в unicod в 10тиричной
# chr(kod)    - возвращает символ по unicode в 10тиричной
print(chr(9731))