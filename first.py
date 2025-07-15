# Погода через API
import requests
from PIL import Image
import io

API_KEY = '087a95ccd5be51143083f162cdf078d3'
URL = 'http://api.openweathermap.org/data/2.5/weather'
CITY = 'Выборг'
params = {
    'q': CITY,
    'appid': API_KEY,
    'units': 'metric',
    'lang': 'ru'
}
response = requests.get(URL, params=params)
result = response.json()

weather = result['weather'][0]['description']
temper = result['main']['temp']
humid = result['main']['humidity']
wind = result['wind']['speed']
data = result['coord']
ll = f'{data['lon']}, {data['lat']}'

print(f'Koordinates: {ll}')
print(f'Segodnya v gorode {CITY}: {weather}', '\t', f'Temper: {temper:1f}', '\n', f'Vlajnost: {humid}%', '\t',
      f'Speed: {wind} M/C')
link = f'https://static-maps.yandex.ru/1.x/?ll={ll}&spn=0.0025,0.0025&l=map&pt={ll},pm2dgl'
image = requests.get(link).content
if image:
    Image.open(io.BytesIO(image)).show()
