from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.fields.html5 import EmailField
from wtforms.validators import DataRequired


class UsuarioForm(FlaskForm):
    nome = StringField('Nome Completo: ', validators=[DataRequired()])
    email = EmailField('Email: ', validators=[DataRequired()])
    senha = PasswordField('Senha: ', validators=[DataRequired()])
    enviar = SubmitField('submit')
