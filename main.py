from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello_world():
    return """Hello World!

        <a href="/quiz">Take the quiz</a>
    """


@app.route('/quiz')
def quiz():
    return '<h1>QUIZ GOES HERE</h1>'
