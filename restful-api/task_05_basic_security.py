#!/usr/bin/python3
from flask import Flask, jsonify, request, abort
from werkzeug.security import generate_password_hash, check_password_hash
from flask_httpauth import HTTPBasicAuth
from flask_jwt_extended import JWTManager

# Create Flask app
app = Flask(__name__)

# Initialize HTTP Basic Auth
auth = HTTPBasicAuth()

# Initialize JWT Manager
jwt = JWTManager(app)

# In-memory storage for users
users = {
    "user1": {
        "username": "user1",
        "password": generate_password_hash("password"),
        "role": "user"
    },
    "admin1": {
        "username": "admin1",
        "password": generate_password_hash("adminpass"),
        "role": "admin"
    }
}


@auth.verify_password
def verify_password(username, password):
    user = users.get(username)
    if user and check_password_hash(user['password'], password):
        return user


@app.route('/')
def home():
    return "Welcome to the Secure Flask API!"
