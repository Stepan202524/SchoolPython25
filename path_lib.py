from os import path

# __file__ - встроенная переменная содержащая путь к исполняемому скрипту
img_dir = path.join(path.dirname(__file__), 'Kartinka')  # Присвоение img-dir Полный путь к папке Kartinka
font_dir = path.join(path.dirname(__file__), 'fonts')     # Присвоение font_dir Полный путь к папке fonts