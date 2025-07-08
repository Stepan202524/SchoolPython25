# Регулярные выражения (поиск по паттерну)
# Regular Expressions (re)
# r-строка - raw-string (сырая строка)

# Квантификаторы
# {m} - ровно m раз
# {m,} - m раз и более
# {,n} - не более n раз
# {m,n} - от m до n (без пробела)
# ?  -  от нуля до одного (аналог {0,1})
# *  -  от нуля до бесконечности (32767)  (аналог {0,32767})
# +  от 1 до бесконечности

import re
pattern = '20'
test_string = '10 plus 20, budet 30'
result = re.search(pattern, test_string)
print(result)

pattern = r'\b\w{4}\b'      # все слова из 4х символов
test_string = 'doma bylo holodno'
result = re.findall(pattern, test_string)
print(result)

pattern = r'\d'      # все цифры от 0 до 9
# pattern= r'\d{3}   # три цифры подряд
# pattern1 = r'nachalo\Z'     # на что заканчивалось
# pattern2 = '[0-5][0-9]'    # две идущие подряд
# pattern3 = '[а-яА-Я]'      # все буквы от а доя и от А до Я
# pattern4 = '[^ерм]'        # вывести всё, исключая символы
# pattern = r'\((.+?)\)'          # Вытащить текст из скобок
test_string = '4 tel89fon 653-45'
result = re.findall(pattern, test_string)       # Ternary If  Тернарный условный оператор
print('Cifry est') if result else print('Netu')
print(result)

pattern = 'Go{3,}gle'
test_string = 'Google, Gooogle, Gooooooogle'
result = re.findall(pattern,test_string)
print(result)