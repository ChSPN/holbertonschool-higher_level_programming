#!/usr/bin/python3
from flask import Flask, jsonify, request, abort

# Step 1
app = Flask(__name__)

users = {}
# Example dictionary: username(key) whole object(value)
# users = {"jane": {"username": "jane", "name":
# "Jane", "age": 28, "city": "Los Angeles"}}


# Step 2: Creating Your First Endpoint:
@app.route("/")
def home():
    """ Prints welcome string """
    return "Welcome to the Flask API!"


# Step 3: Serving JSON Data
@app.route("/data")
def data():
    """ Returns JSON data """
    return jsonify(list(users.keys()))


# Step 4: Expanding Your API
@app.route("/status")
def status():
    """ Prints OK """
    return "OK"


@app.route("/users/<username>")
def users_specific(username):
    """ Get specified """
    if username not in users:
        abort(404)
    return jsonify(users[username])
