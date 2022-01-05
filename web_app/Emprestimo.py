from database import db
import datetime


class Emprestimo(db.Model):
    email_usuario = db.Column(db.String(50), db.ForeignKey('usuario.email'), primary_key=True)
    codigo_chave = db.Column(db.Integer, db.ForeignKey('chave.codigo'))
