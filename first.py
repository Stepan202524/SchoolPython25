# Файл ОС-модуль

import os
# os.mkdir('libs')            # Создание директории в корне проекта
os.makedirs('libs', exist_ok=True)   # Мягкое создание директории
if os.path.exists('libs'):       # Проверка существования пути
    os.rmdir('libs')            # Удаление директории
path = os.getcwd()              # get current working directory
print(path)
os.chdir(path + '/fonts')       # Переход в директорию fonts
print(path)
# os.chdir('..')                  # Выход на уровень выше (из папки fonts)
# print(path)

all_files = [f for f in os.listdir('.')]  #if f.endswith('.ttf')  # Вывод в список всех файлов директории
os.chdir('..')
print(all_files)