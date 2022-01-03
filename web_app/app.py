from Emprestimo import Emprestimo
from Chave import Chave
from Usuario import Usuario
from flask import Flask
from waitress import serve
from flask import render_template
from flask import request, url_for, redirect, flash, make_response
from flask_wtf.csrf import CSRFProtect
import logging
import os
import datetime
from formLogin import LoginForm
from flask_session import Session
from flask import session
from formLogin import LoginForm
import hashlib
import json
from flask_json import FlaskJSON, JsonError, json_response, as_json
from database import db


app = Flask(__name__)
CSRFProtect(app)
CSV_DIR = '/flask/'

# Configuração da sessão
app.config['SESSION_TYPE'] = 'filesystem'
app.config['SECRET_KEY'] = os.urandom(24)
app.config['WTF_CSRF_SSL_STRICT'] = False
Session(app)
FlaskJSON(app)
app.config['JSON_ADD_STATUS'] = False

logging.basicConfig(filename='/web_app/app.log', filemode='w',
                    format='%(asctime)s %(name)s - %(levelname)s - %(message)s', level=logging.DEBUG)

# Iniciando e configurando o BD
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + CSV_DIR + 'bd.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['TEMPLATES_AUTO_RELOAD'] = True


db.init_app(app)


@app.route('/', methods=['POST', 'GET'])
def root():
    form = LoginForm()
    if form.validate_on_submit():
        # PROCESSAMENTO DOS DADOS RECEBIDOS
        email = request.form['usuario']
        senha = request.form['senha']
        senhahash = hashlib.sha1(senha.encode('utf8')).hexdigest()
        # Verificar se existe alguma linha na tabela usuários com o login e senha recebidos
        linha = Usuario.query.filter(
            Usuario.email == email, Usuario.senha == senhahash).all()
        if (len(linha) > 0):  # "Anota" na sessão que o usuário está autenticado
            session['autenticado'] = True
            session['usuario'] = linha[0].id
            flash(u'Usuário autenticado com sucesso!')
            resp = make_response(redirect(url_for('root')))
            if 'contador' in request.cookies:
                contador = int(request.cookies['contador'])
                contador = contador + 1
            else:
                contador = 1
            resp.set_cookie('contador', str(contador))
            return(resp)
        else:  # Usuário e senha não conferem
            flash(u'Usuário e/ou senha não conferem!')
            resposta = make_response(redirect(url_for('login')))
            if 'contador2' in request.cookies:
                contador2 = int(request.cookies['contador2'])
                contador2 = contador2 + 1
            else:
                contador2 = 1
            resposta.set_cookie('contador2', str(contador2))
            return(resposta)
    return (render_template('login.html', form=form, action=url_for('login')))


@app.route('/admin')
def admin():
    return (render_template('adm_screen.html'))


@app.route('/lista-chaves')
def lista_chaves():
    return (render_template('key_list.html'))


@app.route('/emprestimos')
def emprestimos():
    return (render_template('loan_screen.html'))


@app.route('/chaves')
def chaves():
    return (render_template('manager_keys.html'))


@app.route('/registro')
def registro():
    return (render_template('register_user.html'))


if __name__ == "__main__":
    serve(app, host='0.0.0.0', port=80, url_prefix='/app')
