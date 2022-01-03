from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, IntegerField
from wtforms.fields.html5 import EmailField
from wtforms.validators import DataRequired


class UsuarioForm(FlaskForm):
    email = EmailField('E-mail: ', validators=[DataRequired()])
    nome = StringField(u'Nome de usuário: ', validators=[DataRequired()])
    senha = PasswordField('Senha: ', validators=[DataRequired()])
    enviar = SubmitField('CADASTRAR')
