#!/usr/bin/python3
"""This script starts a Flask web application"""


from flask import Flask
import subprocess


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_world():
    """This function executes when the 0.0.0.0:5000/ is requested"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """This function executes when 0.0.0.0:5000/hbnb is requested"""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c_route(text):
    """This function executes when 0.0.0.0:/5000/c/<text>
    is requested
    """
    new_text = text.replace("_", " ")
    return 'C ' + new_text


@app.route('/python', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python(text):
    """This function executes when 0.0.0.0:/5000/python/<text>
    is requested
    """
    return 'Python ' + text.replace("_", " ")


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """This function executes when 0.0.0.0:/5000/number/<int:n>
    is requested
    """
    return str(n) + ' is a number'


if __name__ == '__main__':
    app.run(host='0.0.0.0')
    subprocess.run("export", "FLASK_APP=4-number_route.py")
    subprocess.run("flask run")
