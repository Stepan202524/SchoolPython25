# Flask
# MVC - (Model View Controller)
# GET - запрашивает данные (read)
# POSt - отправляет данные на сервер (submit)
# PUT - принудительно заменяет всё на сервере из контекста запроса (заменить)
# DELETE - удаляет указанные данные
# PATCH - частичное изменение данных

#JINJA - переменные, условия, циклы и т.д.

from fileinput import filename
import sqlite3, os.path
from flask import Flask, url_for, request, render_template
from openpyxl.styles.builtins import title
from werkzeug.utils import secure_filename
from forms.loginform import LoginForm

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads/'
app.config['SECRET_KEY'] = 'just_secret_key'
ALLOWED_EXTENSIONS = ['txt', 'pdf', 'zip', 'jpg', 'png']

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
@app.route('/index')
def index():
#    username = 'Slushatel'
    params = {}
    params['user'] = 'Slushatel'
    params['title'] = 'Privetstvuyu'
    params['weath'] = 'Good day'
#    return render_template('index.html', title='Privetstvie', user=username)
    return render_template('index1.html', **params)

@app.route('/glavnaya')
def glavnaya():
    print('Funkciya glavnaya')
    return f'My est` - Korovnik!'

@app.route('/about')
def about():
    print('Funkciya about')
   # return 'Luchshe o Vas!'
    return render_template('about1.html', title='Pro nas')

@app.route('/contacts')
def contacts():
    print('Funkciya contact')
    return 'Pishite na derevnyu Dedushke!'

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        return 'Forma send'
    return render_template('login.html', title='Autorization', form=form)


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
        return f'Net zaprosa nomera'    # '<a href="https://localhost:5000/get-user/{id_num}">FIO</a>
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

@app.route('/upload', methods=['POST', 'GET'])
def file_upload():
    if request.method == 'GET':
        with open('upload.html', 'r', encoding='utf-8') as html:
            return html.read()
    elif request.method == 'POST':
        if 'file' not in request.files:
            return 'File not choose!'

        file = request.files['file']

        if file.filename == '':
            return 'File bez imeny'

        if file and allowed_file(file.filename):
            new_name = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], new_name))
            return f'YES!! File {new_name} success upload'
    return 'Error upload'

@app.route('/numbers/')
@app.route('/numbers/<int:number>')
def odd_even(number=None):
    if number is None:
        return render_template('numbers.html', title='Enter Chislo!', number=None)
    return render_template('numbers.html', title='Чёт-нечет', number=number)

@app.route('/deals')
def printlist():
    deal = ['Posuda', 'Schetckiki', 'Magaz', 'Sobaka']
    return  render_template('printlist.html', deals=deal)

@app.route('/queue')
def queue():
    # loop.index - номер итерации, начиная с 1
    # loop.index0 - номер итерации, начиная с 0
    # loop.first - True, если первая итерация (.last) - последняя итерация
    return render_template('vars.html', title='Stoim v ogheredi')

if __name__ == '__main__':
    app.run(host='localhost', port=5000)