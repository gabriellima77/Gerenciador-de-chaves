from database import db


class Usuario(db.Model):
    email = db.Column(db.String(120), primary_key=True)
    nome = db.Column(db.String(150), unique=False, nullable=False)
    senha = db.Column(db.String(80), unique=False, nullable=False)
    emprestimos = db.relationship('Emprestimo', backref='usuario', lazy=True)
