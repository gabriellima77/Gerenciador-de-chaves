from database import db
import datetime


class Emprestimo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email_usuario = db.Column(db.Integer, db.ForeignKey('usuario.email'))
    codigo_chave = db.Column(db.Integer, db.ForeignKey('chave.codigo'))
    data_emprestimo = db.Column(
        db.DateTime, unique=False, nullable=True, default=datetime.datetime.now())
    data_devolucao = db.Column(db.DateTime, unique=False, nullable=True)
