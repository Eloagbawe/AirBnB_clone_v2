#!/usr/bin/python3
"""This script starts a Flask web application"""

from flask import Flask
from flask import render_template
from models import storage
from models.state import State
# import subprocess


app = Flask(__name__)


@app.route('/states', strict_slashes=False)
def states():
    """This function executes when 0.0.0.0:/5000/states
    is requested
    """
    state_list = storage.all(State)
    states = []
    for value in state_list.values():
        states.append(value)
    return render_template('9-states.html', states=states, id=None)


@app.route('/states/<id>', strict_slashes=False)
def single_state(id):
    """This function executes when 0.0.0.0:/5000/states
    is requested
    """
    state_list = storage.all(State)
    state = {}
    for key, value in state_list.items():
        if value.id == id:
            state = state_list[key]
    return render_template('9-states.html', id=id, state=state)


@app.teardown_appcontext
def tear_down_context(exception):
    """This function removes the current SQLAlchemy Session"""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0')
    # subprocess.run("export", "FLASK_APP=8-cities_by_state.py")
    # subprocess.run("flask run")
