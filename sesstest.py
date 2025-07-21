import datetime
from flask import Flask, request, make_response, redirect, session

app = Flask(__name__)
app.config['SECRET_KEY'] = 'just_secret_key'
app.config['PERMANENT_SESSION_LIFETIME'] = datetime.timedelta(hours=5)

@app.route('/')
def index():
    return redirect('/cookie_test')

@app.route('/cookie_test')
def cookie_test():
    visit_count = int(request.cookies.get('visit_count', 0))
    if visit_count:
        res = make_response(f'ВЫ посетили эту страницу {visit_count} раз')
        res.set_cookie('visit_count', str(visit_count + 1), max_age=60*60*24*30)
    else:
        res = make_response(f'ВЫ впервые здесь за этот месяц')
        res.set_cookie('visit_count', '1', max_age=60*60*24*30)
    return res

@app.route('/session_test')
def session_test():
    visit_count = session.get('visit_count', 0)
    session['visit_count'] = visit_count + 1
    # session.pop('visit_count', None)  # принудительно удалить сессию с этим ключом
    return make_response(f'Вы на этой странице {visit_count} раз')

if __name__ == '__main__':
    app.run(host='localhost', port=8000)