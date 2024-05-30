#!/usr/bin/python3
from flask import Flask, jsonify, request
from werkzeug.security import generate_password_hash, check_password_hash
from flask_httpauth import HTTPBasicAuth
from flask_jwt_extended import JWTManager, jwt_required, create_access_token

app = Flask(____)
app.config['SECRET_KEY'] = 'super-secret-key'  # Change this!

auth = HTTPBasicAuth()
jwt = JWTManager(app)

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
    if username in users and \
            check_password_hash(users[username]['password'], password):
        return username


@app.route('/basic-protected')
@auth.login_required
def basic_protected():
    return jsonify({"message": "Basic Auth: Access Granted"})


@app.route('/login', methods=['POST'])
def login():
    username = request.json.get('username', None)
    password = request.json.get('password', None)
    if username not in users or \
            not check_password_hash(users[username]['password'], password):
        return jsonify({"error": "Bad username or password"}), 401

    token = create_access_token(identity=username)
    return jsonify(access_token=token), 200


@app.route('/jwt-protected')
@jwt_required
def jwt_protected
