#!/usr/bin/python3
from flask import Flask

# Instantiate a Flask web server
app = Flask(__name__)

# Define a route for the root URL


@app.route("/")
def hello_world():
    return "Hello, World!"


# Run the web server
if __name__ == "_main_":
    app.run(debug=True)
