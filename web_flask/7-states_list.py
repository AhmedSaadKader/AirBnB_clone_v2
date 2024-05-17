#!/usr/bin/python3
"""Starts a Flask web application, listening on 0.0.0.0 port 5000.
It uses storage for fetching data from the storage engine
"""


from models import storage
from models.state import State
from flask import Flask, render_template


app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/states_list')
def states_list():
    """Returns the states list on route('/states_list')
    """
    all_states = storage.all(State)
    print(all_states)
    return render_template('7-states_list.html', all_states=all_states)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
