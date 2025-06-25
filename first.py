hour = int(input('Time please: '))
if hour > 23:
    hour = 23
if hour < 0:
    hour = 0

if 7 <= hour < 12:
    print('Morning')
elif 12 <= hour < 18:
    print('Day')
elif 18 <= hour < 23:
    print('Evening')
else:
    print('Good night')
