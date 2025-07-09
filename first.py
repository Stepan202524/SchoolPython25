# Регулярные выражения (поиск по паттерну)   regex101.com — отладка RegEx
# Regular Expressions (re)                      regexr.com — визуализация шаблонов
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

# pattern = 'Go{3,}gle'      # Google где 3 и более о
# test_string = 'Google, Gooogle, Gooooooogle'

# pattern = r'стеклянн?ый'        # 2-я "н" может присутствовать  но не обязана
# test_string = 'стекляный, стеклянный, оловянный'

# pattern = r'<img.*>'        # "жадный" квантификатор
# pattern = r'<img.*?>'       # "ленивый" квантификатор
# pattern = r'<img[^>]+srс="([^">]+)"'        # вытащит bg.jpg только путь к картинке
# test_string = 'Картинка <img srс="bg.jpg"> в тексте</p>'
# pattern = r'<p>(.*?)</p>'       # Содержимое абзаца html
# test_string = '<b>Вот начало: </b><p>Содержимое</p><i>и так далее</i>'
# pattern = r'<p[^>]*>(.*)</p>'       # Содержимое абзаца html с атрибутами
# test_string = '<b>Центрируем</b><p align="center">Содержимое</p>'
# result = re.findall(pattern,test_string)
# print(result)

# Убираем все знаки препинания
def remove_punctuation(input_str: str) -> str:
# Методом sub() заменяем все найденные совпадения пустой строки и возвращаем "очищенную"
# :param input_str: строка со знаками препинания
# :return: строку, очищенную от знаков препинания
    return re.sub(r'[^\w\s]', '', input_str)
test_string = 'Язык Python, явля?ясь инту,итивно понят.ным'
result = remove_punctuation(test_string)
print(result)

# Split
pattern = r'[,.:;!]'
test_string = 'яблоко,   груша.   банан  ;  слива  ! абрикос  '
# test_string = ''.join(test_string.split())      # убрали все пробелы
result = re.split(pattern, test_string)
# через map
# result= list(map(lambda x: x.strip(), result))
# через list с сортировкой
result = sorted(x.strip() for x in result)
print(result)

