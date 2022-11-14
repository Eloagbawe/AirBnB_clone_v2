#!/usr/bin/python3
"""This script starts a Flask web application"""

from flask import Flask
from flask import render_template
from models import storage
from models.state import State
from models.amenity import Amenity
from models.place import Place
import subprocess


app = Flask(__name__)


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """This function executes when 0.0.0.0:/5000/states_list
    is requested
    """
    state_list = storage.all(State)
    amenity_list = storage.all(Amenity)
    place_list = storage.all(Place)
    states = []
    amenities = []
    places = []
    for value in state_list.values():
        states.append(value)
    for value in amenity_list.values():
        amenities.append(value)
    for value in place_list.values():
        places.append(value)
    return render_template('100-hbnb.html',
                           states=states, amenities=amenities,
                           places=places)


@app.teardown_appcontext
def tear_down_context(exception):
    """This function removes the current SQLAlchemy Session"""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0')
    subprocess.run("export", "FLASK_APP=100-hbnb.py")
    subprocess.run("flask run")
