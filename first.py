# вывод чисел, заканчивается на 3
cout = 1
while cout <= 100:
    if cout % 10  == 3:
        print(cout, end=', ')
    cout += 1