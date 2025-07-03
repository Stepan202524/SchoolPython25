# Анонимные функции (однострочные, безымянные)
# lambda  <Аргументы>: <выражение>
# Потоковый ввод sys.stdin
import sys

# for line in sys.stdin:
#     print(line)
data = sys.stdin.readlines()
print(data, [d.strip('\n') for d in data])
# data1 = [d.strip('\n') for d in data]  # Убираем символы \n

temp =[]                # индекс строки в date и числа слов в виде кортежей
for i,s in enumerate(data):
    temp.append((i, len(s.split())))
temp.sort(key=lambda x:x[1])
index = temp[0][0]
res = sorted(data[index].split())
print(*res, sep='-')