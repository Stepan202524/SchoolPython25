from PIL import Image, ImageDraw, ImageFont
orig = Image.open('Kartinka/sunny_day.jpg').convert('RGB')  # открыть файл и конвертация в RGB
up = orig.crop((0, 0, 600, 200))        # вырезаем половину картинки
down = orig.crop((0, 200, 600, 400))    # вырезаем вторую половину
new =Image.new('RGB', (600, 400))
new.paste(down, (0, 0))
new.paste(up, (0, 200))     # Поменяем местами
#new.show()

from PIL import ImageFilter, ImageEnhance

orig1 = Image.open('Kartinka/Spanch.jpg')
blur_image = orig1.filter(ImageFilter.GaussianBlur(radius=8))        # Размытие
blur_image.show()

enchancer = ImageEnhance.Sharpness(orig1)
sharpened_image = enchancer.enhance(4.0)        # Усиление резкости
blur_image.show()

edges = orig1.filter(ImageFilter.FIND_EDGES)    # Контуры
blur_image.show()