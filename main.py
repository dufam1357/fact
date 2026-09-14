from flask import Flask 
from random import choice

app = Flask(__name__)

facts = open('fact.txt' , 'r' , encoding='utf-8').readlines()

@app.route("/")
def hello_world():
    return '''<p>Hello, World!</p>
    <a href="/fact">случайный факт</a>'''

@app.route('/fact')
def fact():
    return f'''<p>{choice(facts)}</p>
    <a href="/">главная страница</a>'''

app.run(debug=True)