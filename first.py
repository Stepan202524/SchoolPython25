# pip freeze > requirements.txt     - Создание файла зависимости
# pip install -r requirements.txt    - установка списка библиотек
from PIL import Image, ImageDraw       # Подгружаем базовые навыки для картинок, для рисования


image = Image.open('Kartinka/Spanch.jpg')

x, y = image.size       # Распаковка размера картинки в координаты (кортеж)
mode =image.mode        # Режим файла картинки
pixels = image.load()   # Создать таблицу адресов пикселей  (кортеж - RGB)(двумерный массив)
for i in range(x):
    for j in range(y):
        r, g, b = pixels[i, j]      # Обращение в кортеже
# image.save('Kartinka/spanch2.jpg')
print(f'Shyrina = {x}, Vysota = {y}, Color shema = {mode}')

# image_rotate = image.rotate(90) # Потом надо сохранять в новый файл, чтоб не испортить оригинал
# import_flip = image.transpose(Image.Transpose.FLIP_TOP_BOTTOM)    # Отражение

# cropped = image.crop((245, 0, 500, 430))   # Вырезание части картинки (адрес начала - адрес конца)
# resize = image.resize((x, y)) # Изменение размера
RED = (255, 0, 0)
image1 = Image.new('RGB', (600, 400), (0, 0, 255))  # Создание новой картинки с синим фоном
#image1.save('Kartinka/blue.jpg')
draw = ImageDraw.Draw(image1)
draw.line((0, 0, 600, 400), fill=(255, 0 ,0), width=5) # Рисуем линию
draw.rectangle((10, 10, 590, 390), outline=RED, width=11) # Прямоугольник
draw.text((150, 150), 'Ura Privet', fill=RED)

POLY = [(100, 50), (150, 50), (180, 120)]
draw.polygon(POLY, outline='GREEN', width=15) #  Треугольник