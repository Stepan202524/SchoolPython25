a = int(input('A='))
b = int(input('B='))
c = int(input('C='))
if a != 0:
    d = b ** 2 - 4 * a * c
    if d < 0:
        print('No korni')
    elif d == 0:
        x = -b / (2 * a)
        print(f'Koren: {x:.2f}')
    else:
        x1 = (-b + d ** 0.5) / 2 * a
        x2 = (-b - d ** 0.5) / 2 * a
        print(f'Korni:\n\tx1 = {x1:.2f}\n\tx2 = {x2:.2f}\n\tx2')
else:
    print('A>0')

