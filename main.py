from flask import Flask
from flask import render_template
app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template("main.html")


@app.route('/quiz')
def quiz():
    return render_template("quiz.html")
