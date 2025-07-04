# Встроенные библиотеки
import sys

strings = [d.strip('\n') for d in sys.stdin.readlines()]
length = len(strings)  # сколько строк
rem = length % 3

if rem:
    strings = strings[:length - rem]

for x in range(0, length - rem, 3):
    summ = sum(len(a) for a in strings[x:x + 3])
    result = []
    for s in strings[x:x + 3]:
        temp = s.lower().split()
        result += filter(lambda a: len(a) % 2 == summ % 2, temp)
    result = sorted(set(map(lambda b: b.capitalize(), result)))[:5]
    print(*result, sep='. ')