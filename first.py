# Исключения
# try:
#    что пытаемся сделать
# except:
#    обрабатываем исключения
# else:
#    если исключения не было
# finally:
#    выполняется в любом случае
flag = False    # открывался ли на запись

try:
    fo = open('inform.txt', encoding='utf-8')
    print(fo.read())
    fo.close()
except FileNotFoundError:
    print('Net takogo fayla')
    with open('inform.txt', 'wt', encoding='utf-8') as fo:
        fo.write('По умолчанию')
else:
    print('Fayl otkryt uspeshno. Read & close')
    print(fo.read())
    fo.close()
finally:
    print('Rabotaem dal`she')