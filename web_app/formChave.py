from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField
from wtforms.validators import DataRequired


class ChaveForm(FlaskForm):
    codigo = IntegerField('Codigo', validators=[DataRequired()])
    nome = StringField('Nome da chave', validators=[DataRequired()])
    enviar = SubmitField('CADASTRAR')
