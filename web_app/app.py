from flask import Flask
from waitress import serve
from flask import render_template
from flask import request,url_for,redirect,flash,session

app = Flask(__name__)

@app.route('/')
def root():
    return ("Ola mundo!")

if __name__ == "__main__":
    serve(app, host='0.0.0.0', port=80, url_prefix='/app')
