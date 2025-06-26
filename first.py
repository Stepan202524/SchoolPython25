# min, max, average, summ, production
total = 0
N = 3
prod = 1
min_val = float('inf')  # + бесконечность
max_val = float('-inf')  # - бесконечность
for _ in range(N):
    num = int(input('Please number: '))
    total += num
    average = total / N
    prod *= num
    if num < min_val:
        min_val = num
    if num > max_val:
        max_val = num
print(f'Summa: {total}')
print(f'Sr. arifmet: {average}')
print(f'Proizved: {prod}')
print(f'Min: {min_val}')
print(f'Max: {max_val}')
