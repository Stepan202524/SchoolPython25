from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    username = StringField('Login', validators=[DataRequired('Bez logina NIKAK!')])
    password = PasswordField('Password', validators=[DataRequired('i bez parolya NIKAK!')])
    remember_me = BooleanField('Zapomnit` menya')
    submit = SubmitField('Enter')