# Flask
# MVC - (Model View Controller)
# GET - запрашивает данные (read)
# POSt - отправляет данные на сервер (submit)
# PUT - принудительно заменяет всё на сервере из контекста запроса (заменить)
# DELETE - удаляет указанные данные
# PATCH - частичное изменение данных

#JINJA - переменные, условия, циклы и т.д.

#ORM - Object Relational Mapping (Объектно-реляционное отображение)
# SOA - Service Oriented Architecture
# MSA - Micro Service Architecture
# REST - Representation State Transfer
# GET - /book/page/50   - посмотреть страницу 50
# GET - /book           - увидеть список всех книг
# POST - /book
# DELETE - /book/7

from fileinput import filename
import sqlite3, os.path

import requests
from flask import Flask, url_for, request, render_template, redirect, abort,jsonify, make_response
from openpyxl.styles.builtins import title
from pyexpat.errors import messages
from werkzeug.utils import secure_filename
from forms.loginform import LoginForm
from forms.news import NewsForm
from forms.user import Register
from data import db_session, news_api, api_resources
from flask_restful import Api
from data.users import User
from data.news import News
from flask_login import LoginManager, login_user, logout_user, current_user, login_required

from send_mail import send_mail

app = Flask(__name__)
api = Api(app)

login_manager = LoginManager()
login_manager.init_app(app)

app.config['UPLOAD_FOLDER'] = 'uploads/'
app.config['SECRET_KEY'] = 'just_secret_key'
ALLOWED_EXTENSIONS = ['txt', 'pdf', 'zip', 'jpg', 'png']

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@login_manager.user_loader
def load_user(user_id):
    db_sess = db_session.create_session()
    return db_sess.get(User, user_id)

# @app.errorhandler(404)
# def not_found(e):
#     return render_template('404.html', title='Ne naydeno')

@app.errorhandler(400)
def bad_request(_):
    return make_response(jsonify({'error': 'Bad request'}), 400)

@app.errorhandler(404)
def not_notfound(e):
    return make_response(jsonify({'error': 'Not found'}), 404)

@app.errorhandler(401)
def not_authorized(_):
    return redirect('/login')

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
@login_required
def about():
    print('Funkciya about')
   # return 'Luchshe o Vas!'
    return render_template('about1.html', title='Pro nas')

@app.route('/contacts')
def contacts():
    print('Funkciya contact')
#    return 'Pishite na derevnyu Dedushke!'
    return render_template('contacts.html', title='Kontakty')

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        user = db_sess.query(User).filter(User.email == form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember_me.data)
            return redirect('/')
        return render_template('login.html', message='Nevernyi login ili parol`',
                               title='Error authorization', form=form)
    return render_template('login.html', title='Authorization', form=form)

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = Register()
    if form.validate_on_submit():       # тоже самое что и request.method == 'POST'
        # Если пароли не совпали
        if form.password.data != form.password_again.data:
            return render_template('register.html', title='Registration',
                                   message='Paroli ne sovpadayut', form=form)
        db_sess = db_session.create_session()
        # Если пользователь с таким email уже есть
        if db_sess.query(User).filter(User.email==form.email.data).first():
            return render_template('register.html', title='Registration',
                                       message='Takoy polzovatel` uje est`', form=form)

        user = User(name=form.name.data, email=form.email.data, about=form.about.data)
        user.set_password(form.password.data)
        db_sess.add(user)
        db_sess.commit()
        return redirect('/login')
    return render_template('register.html', title='Registration', form=form)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect('/')

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

@app.route('/news')
def news():
    db_sess = db_session.create_session()
    if current_user.is_authenticated:
        all_news = db_sess.query(News).filter((News.user == current_user) | (News.is_private != True)).all()
    else:
        all_news = db_sess.query(News).filter(News.is_private != True).all()
#   all_news = db_sess.query(News).filter(News.is_private != True).all()
    print(all_news)
    return render_template('news.html', title='Новости', news=all_news)

@app.route('/newsjob', methods=['GET', 'POST'])
@login_required
def add_news():
    form = NewsForm()
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        news = News()
        news.title = form.title.data
        news.content = form.content.data
        news.is_private = form.is_private.data
        current_user.news.append(news)
        db_sess.merge(current_user)
        db_sess.commit()
        return redirect('/news')
    return render_template('newsjob.html', title='Добавление новости', form=form)

@app.route('/newsjob/<int:id_num>', methods=['GET', 'POST'])
@login_required
def edit_news(id_num):
    form = NewsForm()
    if request.method == 'GET':
        db_sess = db_session.create_session()
        news = db_sess.query(News).filter(News.id == id_num, News.user == current_user).first()
        if news:
            form.title.data = news.title
            form.content.data = news.content
            form.is_private.data = news.is_private
        else:
            abort(404)
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        news = db_sess.query(News).filter(News.id == id_num, News.user == current_user).first()
        if news:
            news.title = form.title.data
            news.content = form.content.data
            news.is_private = form.is_private.data
            db_sess.commit()
            return redirect('/news')
        else:
            abort(404)
    return render_template('newsjob.html', title='Редактирование новости', form=form)

@app.route('/newsdel/<int:news_id>')
@login_required
def news_delete(news_id):
    db_sess = db_session.create_session()
    news = db_sess.query(News).filter(News.id == news_id, News.user == current_user).first()
    if news:
        db_sess.delete(news)
        db_sess.commit()
    else:
        abort(404)
    return redirect('/news')

@app.route('/adminpage', methods=['GET', 'POST'])
@login_required
def adminpanel():
    if current_user.is_authenticated and current_user.is_admin():
        db_sess = db_session.create_session()
        res = db_sess.query(News).all()
        return render_template('admin.html', title='Panel` administratora', news=res)
    else:
        abort(404)

@app.route('/testapi')
def testapi():
    res = requests.get('http://localhost:5000/api/news').json()
    return  render_template('testapi.html', title='Тест API')

@app.route('/sendmail', methods=['GET','POST'])
def mail_send():
    name=request.form.get('name')
    email = request.form.get('email')
    message = request.form.get('message')
    return f'Otpravleno na {email} ot {name} s message ({message}).'
# Отправка mail из обратной связи
#     temp = (f'Pismo s obratnoy ot {name} s tekstom {message}. Otpravitel` {email}')
#     mess = temp + message
#     send_mail('Vash email', 'Obratnaya svyaz`', mess)
#     send_mail(email, 'Polucheno', f'{name}', 'Thank you')
#    return render_template('contacts.html', tutle='Otpravleno!', mess='Otpravilos`')

if __name__ == '__main__':
    db_session.global_init('db/news.sqlite')
    app.register_blueprint(news_api.blueprint)
    # Доступ к отдельной новости
    api.add_resource(api_resources.NewsResource, '/api/v2/news/<int:news_id>')
    # Доступ ко всем новостям
    api.add_resource(api_resources.NewsResourceList, '/api/v2/news')
    app.run(host='localhost', port=5000)

    # news = News()
    # # db_sess = db_session.create_session()
    # # first = db_sess.query(User).filter(User.id > 1).all() # .first() - первая строка  .all() -все строки
    # # print(first)
    # news.name = 'User2'
    # news.title = 'Dannye321 ob User1'
    # news.content = 'Abra4314Cadabra'
    # db_sess = db_session.create_session()
    # db_sess.add(news)
    # db_sess.commit()