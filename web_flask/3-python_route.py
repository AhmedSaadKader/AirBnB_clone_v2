#!/usr/bin/python3
""" Starts a flask web application
"""


from flask import Flask

app = Flask(__name__)

app.url_map.strict_slashes = False


@app.route('/')
def hello():
    """Return Hello HBNB on route(/)
    """
    return 'Hello HBNB!'


@app.route('/hbnb/')
def hbnb():
    """Return HBNB on route(/hbnb)
    """
    return 'HBNB'


@app.route('/c/<text>')
def describe_c(text):
    """Return C followed by text on route(/c/<text>)
    """
    return 'C ' + text.replace('_', ' ')


@app.route('/python/')
@app.route('/python/<text>')
def describe_python(text="is cool"):
    """Return Python followed by text on route(/python/<text>)
    """
    return 'Python ' + text.replace('_', ' ')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
