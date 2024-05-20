#!/usr/bin/python3
"""
A script that starts a Flask web application:
"""

from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_route():
    """
    Displays 'Hello HBNB!'
    Returns:
        str: "Hello HBNB"
    """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb_route():
    """
    Displays 'HBNB'
    Returns:
        str: "HBNB"
    """
    return "HBNB"

@app.route('/c/<text>', strict_slashes=False)
def c_route(text):
    """
    Displays 'HBNB'
    Returns:
        str: "HBNB"
    """
    return "C {}".format(text.replace("_"," "))


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_route(text = "is cool"):
    """
    Displays 'HBNB'
    Returns:
        str: "HBNB"
    """
    return "Python  {}".format(text.replace("_"," "))

@app.route('/number/<int:n>', strict_slashes=False)
def number_route(n):
    """
    Displays 'HBNB'
    Returns:
        str: "HBNB"
    """
    return "{}  is a number".format(n)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
