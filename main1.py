# Flask
# MVC - (Model View Controller)
from flask import Flask

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

if __name__ == '__main__':
    app.run(host='localhost', port=5000)