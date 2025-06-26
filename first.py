#  Диапазон роста
rost = int(input('Please your rost: '))
while rost <= 150 or rost >= 180: # 150 >= rost <= 180:
    print('Sorry')
    rost = int(input('Again:'))

print(f'Yes, Your rost: {rost}')
