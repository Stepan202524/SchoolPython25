import re
import requests

pattern = r'<img[^>]+src="([^">]+)"'        # вытащить путь к картинке
# Сначала проверили
# test_string = '<img height="50" width="150" src="images/bg.jpg">'
html = requests.get('https://skillbox.ru').text
result = re.findall(pattern, html)
print(result)