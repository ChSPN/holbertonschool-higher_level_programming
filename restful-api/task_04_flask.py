#!/usr/bin/python3
"""Develop a Simple API using Python with Flask"""

import logging
from flask import Flask, jsonify, request

app = Flask(__name__)

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


"""Stockage des données en mémoire"""
users = {
    "jane": {
        "username": "jane",
        "name": "Jane",
        "age": 28,
        "city": "Los Angeles"
    },
    "john": {
        "username": "john",
        "name": "John",
        "age": 30,
        "city": "New York"
    }
}


@app.route('/')
def home():
    """Home route to welcome users to the Flask API."""
    return "Bienvenue sur l'API Flask !"


@app.route('/data', strict_slashes=False)
def get_usernames():
    """Route to get the list of all usernames."""
    return jsonify(list(users.keys()))


@app.route('/status', strict_slashes=False)
def status():
    """Route to check the status of the server."""
    return jsonify({"status": "OK"})


if __name__ == "__main__":
    host = '0.0.0.0'
    port = 5000

    """Enable debug mode for development"""
    debug = True

    """Set up logging"""
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)

    """Print a message to indicate the server is starting"""
    logger.info(f"Starting Flask server at http://{host}:{port}/")

    """Additional configuration options"""
    app.config['ENV'] = 'development'
    app.config['DEBUG'] = debug
    app.config['TESTING'] = False

    """Log configuration details"""
logger.info(f"Configuration - ENV: {app.config['ENV']},"
            f"DEBUG: {app.config['DEBUG']},"
            f"TESTING: {app.config['TESTING']}")

"""Run the Flask app"""
app.run(host=host, port=port, debug=debug)
