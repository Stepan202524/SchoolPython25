# Flask
# MVC - (Model View Controller)
from fileinput import filename

from flask import Flask, url_for

app = Flask(__name__)
@app.route('/')
@app.route('/index')
def index():
    return 'Privet, Flask'

@app.route('/about')
def about():
    print('Funkciya about')
    return 'O nas'

@app.route('/countdown')
def cd():
    lst = [str(x) for x in reversed(range(10))]
    lst.append('Poleteli!!')
    return '<br>'.join(lst)

@app.route('/image')
def show_image():
    return f'<img src="{url_for('static', filename='images/spanch.jpg')}">'
                     # static/images/spanch.jpg">')

@app.route('/sample-page')
def sample_page():
    return f"""
            <!DOCTYPE html>
        <html lang="ru">
        <head>
            <meta charset="UTF-8">
            <title>Kartinka</title>
        </head>
        <body>
            <img src="{url_for('static', filename='images/spanch.jpg')}" alt="Spanch"> 
        </body>
        </html>
    """

if __name__ == '__main__':
    app.run(host='localhost', port=5000)