# break, continue

num = 3  #Угадать это число

var =''
print('Ugaday number')
while True:
    var = int(input('Your num:'))
    if var == num:
        print('Yahoo')
        break  # принудительный вылет из цикла
    elif var > num:
        print('Big num')
    else:
        print('Small num')
print('welcome')