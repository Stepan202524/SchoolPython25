num = 3  #Угадать это число
flag = True
var =''
print('Ugaday number')
while flag:
    var = int(input('Your num:'))
    if var == num:
        print('Yahoo')
        flag = not flag  # flag  инвертирован
    elif var > num:
        print('Big num')
    else:
        print('Small num')
print('welcome')