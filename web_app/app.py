from flask import Flask
from waitress import serve
from flask import render_template
from flask import request, url_for, redirect, flash, session
from formLogin import LoginForm
import logging

app = Flask(__name__)

logging.basicConfig(filename='/web_app/app.log', filemode='w',
                    format='%(asctime)s %(name)s - %(levelname)s - %(message)s', level=logging.DEBUG)


@app.route('/')
def root():
    return (render_template('login.html'))


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
