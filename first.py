# города игра
s = set()
while (city := input('Please city :')) != '':
    if city in s:
        print('Uje est`')
    else:
        s.add(city)
print(f'Vsego city: {len(s)} ukazano:')
for item in s:
    print('\t', item)