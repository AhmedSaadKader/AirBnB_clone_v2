#!/usr/bin/python3
"""Starts a Flask web application.
Routes:
    /states_id: HTML page with a list of all State objects in DBStorage.
"""
from models import storage
from flask import Flask, render_template


app = Flask(__name__)


@app.route("/states", strict_slashes=False)
def states():
    """Displays  a list of all States.
    States are sorted by name.
    """
    states = storage.all("State")
    return render_template("9-states.html", state=states)


@app.route("/states/<id>", strict_slashes=False)
def states_id(id):
    """Displays an HTML page with info about <id>, if it exists."""
    for state in storage.all("State").values():
        if state.id == id:
            return render_template("9-states.html", state=state)
    return render_template("9-states.html")


@app.teardown_appcontext
def teardown(exception):
    """Closes storage session"""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0")