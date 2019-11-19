import random
from flask import Flask
from flask import render_template
app = Flask(__name__)


def random_question():
    questions = [
        "Q 1",
        "Q 2",
        "Q 3",
        "Q 4",
        "Q 5",
    ]
    return random.sample(questions, 1)


@app.route('/')
def hello_world():
    return render_template("main.html")


@app.route('/quiz')
def quiz():
    return render_template("quiz.html", question=random_question())
