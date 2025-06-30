# Кортеж (tuple, immutable)
channels = ('red', 'green', 'blue')
r, g, b = channels    # распаковка
print(r, b)
a, b, c = 1, 2, 3 # input(), input(), input()
d, e = [4, 5], 6 # упаковка в d [4, 5]

# студент и средний балл
N=3
studs = []
for _ in range(N):
    stud, aver = input('Name'), float(input('Ball'))
    studs.append((stud, aver)) # append идёт кортежом (скобки в скобках) через ,
print(studs)

for st in studs:
    stud, aver = st  # распаковка
    print('Sudent: ', stud)
    print('Sredniy ball: ', aver)
