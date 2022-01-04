from flask_wtf import FlaskForm
from wtforms import SubmitField, PasswordField
from wtforms.validators import DataRequired
from wtforms.fields.html5 import EmailField


class LoginForm(FlaskForm):
    email = EmailField('Email: ', validators=[DataRequired()])
    senha = PasswordField('Senha: ', validators=[DataRequired()])
    enviar = SubmitField('submit')
