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


if __name__ == '__main__':
    app.run(host='0.0.0.0')
    subprocess.run("export", "FLASK_APP=1-hbnb_route.py")
    subprocess.run("flask run")
