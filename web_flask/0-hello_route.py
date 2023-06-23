#!/usr/bin/python3
""" Script that runs an app with Flask framework """
from flask import Flask


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """ Function called with / route """
    return 'Hello HBNB!'

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True, port=5000)