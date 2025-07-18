from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.fields.simple import EmailField, TextAreaField
from wtforms.validators import DataRequired

class Register(FlaskForm):
    email = EmailField('Pochta', validators=[DataRequired('Enter corrective email')])
    password = PasswordField('Parol', validators=[DataRequired('Parol obyazatel`no')])
    password_again = PasswordField('Povtorite parol', validators=[DataRequired('Podtverdite parol')])
    name = StringField('Your Name', validators=[DataRequired('Enter Imya')])
    about = TextAreaField('Nemnogo pro sebya')
    submit = SubmitField('Registration')