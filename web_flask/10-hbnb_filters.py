#!/usr/bin/python3
"""This script starts a Flask web application"""

from flask import Flask
from flask import render_template
from models import storage
from models.state import State
from models.amenity import Amenity
import subprocess


app = Flask(__name__)


@app.route('/hbnb_filters', strict_slashes=False)
def hbnb_filters():
    """This function executes when 0.0.0.0:/5000/states_list
    is requested
    """
    state_list = storage.all(State)
    amenity_list = storage.all(Amenity)
    states = []
    amenities = []
    for value in state_list.values():
        states.append(value)
    for value in amenity_list.values():
        amenities.append(value)
    return render_template('10-hbnb_filters.html',
                           states=states, amenities=amenities)


@app.teardown_appcontext
def tear_down_context(exception):
    """This function removes the current SQLAlchemy Session"""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0')
    subprocess.run("export", "FLASK_APP=10-hbnb_filters.py")
    subprocess.run("flask run")
