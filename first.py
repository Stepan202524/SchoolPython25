import datetime as dt

print(dt.datetime.now())
print(dt.datetime.now().date())    # .time

time = dt.datetime.now()
ftime = time.strftime('%d-%m-%Y')       # Перевод в другой формат (российский) указания даты (получаем в строке)
ftime1 = time.strftime('%H :%M :%S')
print(ftime, ftime1)

my_time = dt.time(15, 27, 55)   # Задаём своё время (объект)
my_date = dt.date(2023, 11, 30)     # дату
print(dt.datetime.combine(my_date, my_time))        # Объединяем
