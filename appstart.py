from flask import Flask, render_template
from flask_bootstrap import Bootstrap

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/user/<name>/<comments>')
def user(name,comments):
    return render_template('user.html', name=name,comments=comments)


