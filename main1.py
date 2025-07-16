# Flask
# MVC - (Model View Controller)
# GET - запрашивает данные (read)
# POSt - отправляет данные на сервер (submit)
# PUT - принудительно заменяет всё на сервере из контекста запроса (заменить)
# DELETE - удаляет указанные данные
# PATCH - частичное изменение данных

from fileinput import filename
import sqlite3
from flask import Flask, url_for, request

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

@app.route('/sample-page2')
def sample_page2():
    with open('temp.html', 'r', encoding='utf-8') as html:
        return html.read()

# Конвертор: <string> -по умолчанию строка  <int:number> -целое число  <float:number> -дес. дробь
#           <path:p> -может содержать слэши для указания пути
#           <uuid:id> - строка идентификатор (16-байт в HEX-формате)
@app.route('/greeting/<user>/<int:id_num>')
def greeting(user, id_num):
    return f'Privet, {user}, s takim vot id= {id_num}'

# Подгружаем БД и вытаскиваем строку по номеру
@app.route('/ger-user/')        # Пустой параметр
@app.route('/get-user/<int:id_num>')
def get_user(id_num=None):
    if id_num is None:
        return f'Net zaprosa nomera'
    con = sqlite3.connect('db/movies.sqlite')
    cur = con.cursor()
    query = f'SELECT name, city FROM users WHERE trip_id={id_num}'
    response = cur.execute(query)
    result = response.fetchone()
    print(result)
    name, city = result
    cur.close()
    con.close()
    # return str(result[0])
    return f'''
    <table border=1>
    <tr>
    <td>FIO</td>
    <td>Gorod</td>
    </tr>
    <tr>
    <td>{name}</td>
    <td>{city}</td>
    </tr>
    </table>
'''

@app.route('/form-test', methods=['POST', 'GET'])
def form_test():
    if request.method == 'GET':
        with open('form.html', 'r', encoding='utf-8') as html:
            return html.read()
    elif request.method == 'POST':
        print(request.form['gender'])
        print(request.form['email'])
        print(request.form['about'])
        print(request.form['level'])
        print(request.form['password'])
        print(request.form['accept'])
        return 'Forma otpravlena'

if __name__ == '__main__':
    app.run(host='localhost', port=5000)