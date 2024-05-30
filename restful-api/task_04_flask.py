#!/usr/bin/python3
from flask import Flask, jsonify, request

app = Flask(__name__)

# Stockage des utilisateurs en mémoire
users = {}


@app.route("/")
def home():
    return "Welcome to the Flask API!"


@app.route("/data", methods=["GET"])
def get_data():
    return jsonify(list(users.keys()))


@app.route("/status", methods=["GET"])
def get_status():
    return "OK"


@app.route("/users/<username>", methods=["GET"])
def get_user(username):
    user = users.get(username)
    if user:
        return jsonify(user)
    else:
        return "User not found", 404


@app.route("/add_user", methods=["POST"])
def add_user():
    user = request.get_json()
    username = user.get("username")
    if username in users:
        return "User already exists", 400
    else:
        users[username] = user
        return jsonify({"message": "User added", "user": user})


if __name__ == "__main__":
    app.run(debug=True)
