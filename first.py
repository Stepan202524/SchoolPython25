# Исключения
# try:
#    что пытаемся сделать
# except:
#    обрабатываем исключения
# else:
#    если исключения не было
# finally:
#    выполняется в любом случае

# Бросаемся исключениями - raise
max_val = 10
min_val = 1

try:
    val = int(input(f'VVedite celoe chislo ot {min_val} do {max_val}: '))
    if not min_val < val < max_val:
        raise ValueError('Vne diapozona')
    print(f'Chislo {val} lejit v nujnom diapozone')
except ValueError as exp:
    print('Vnimatelno: ', exp)
# print('Ostatok ot deleniya.')
# loop = True
# while loop:
#     try:
#         value = int(input('Na chto delim 10:'))
#         res = 10 % value
#         print(f'Ostatok ot deleniya 10 na {value} = {res}')
#     except ZeroDivisionError:
#         print('Nelzya delit na 0!')
#     except ValueError:
#         print('Nodo vvodit tolko celye chisla')
#     except Exception as exp:
#         print('Proizoshlo iskluchenie -', exp.__class__.__name__, exp)
#     else:
#         loop = False


# flag = False    # открывался ли на запись
#
# try:
#     fo = open('inform.txt', encoding='utf-8')
#     print(fo.read())
#     fo.close()
# except FileNotFoundError:
#     print('Net takogo fayla')
#     with open('inform.txt', 'wt', encoding='utf-8') as fo:
#         fo.write('По умолчанию')
# else:
#     print('Fayl otkryt uspeshno. Read & close')
#     print(fo.read())
#     fo.close()
# finally:
#     print('Rabotaem dal`she')