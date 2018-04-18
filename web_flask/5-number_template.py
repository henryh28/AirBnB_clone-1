#!/usr/bin/python3
""" Starts a Flask web application """

from flask import Flask, render_template
app = Flask(__name__)


@app.route("/", strict_slashes=False)
def index():
    """ Display 'Hello HBNB!' """
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """ Display 'HBNB' """
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c(text):
    """ Display 'C' followed by parameter value """
    return "C " + text.replace("_", " ")


@app.route("/python/", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python(text="is cool"):
    """ Display 'Python' followed by parameter value """
    return "Python " + text.replace("_", " ")


@app.route("/number/<int:n>", strict_slashes=False)
def number(n):
    """ Display 'n' only if 'n' is an integer """
    return "{} is a number".format(n)


@app.route("/number_template/<int:n>", strict_slashes=False)
def number_template(n):
    """ Display a HTML page only if 'n' is an integer """
    return render_template("5-number.html", number=n)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
