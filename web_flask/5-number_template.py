#!/usr/bin/python3
"""This script starts a Flask web application"""


from flask import Flask
from flask import render_template

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


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """This function executes when 0.0.0.0:/5000/number/<int:n>
    is requested
    """
    return render_template('5-number.html', n=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0')
    subprocess.run("export", "FLASK_APP=5-number_template.py")
    subprocess.run("flask run")
