from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
   email = StringField('Email: ', validators=[DataRequired()])
   senha = PasswordField('Senha: ')
   enviar = SubmitField('Login')