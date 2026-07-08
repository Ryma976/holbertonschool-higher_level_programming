#!/usr/bin/python3
"""
A simple RESTful API using the Flask web framework.
"""
from flask import Flask, jsonify, request

app = Flask(__name__)

# Dictionary to store users in memory (keep empty for checker)
users = {}


@app.route('/')
def home():
    """Root endpoint returning a welcome message."""
    return "Welcome to the Flask API!"


@app.route('/data')
def get_data():
    """Returns a list of all usernames stored in the API."""
    return jsonify(list(users.keys()))


@app.route('/status')
def get_status():
    """Returns the API status."""
    return "OK"


@app.route('/users/<username>')
def get_user(username):
    """Returns the full object corresponding to the provided username."""
    user = users.get(username)
    if user:
        return jsonify(user)
    return jsonify({"error": "User not found"}), 404


@app.route('/add_user', methods=['POST'])
def add_user():
    """Handles POST requests to add a new user to the directory."""
    data = request.get_json(silent=True)
    
    if data is None:
        return jsonify({"error": "Invalid JSON"}), 400

    username = data.get("username")
    if not username:
        return jsonify({"error": "Username is required"}), 400

    if username in users:
        return jsonify({"error": "Username already exists"}), 409

    users[username] = {
        "username": username,
        "name": data.get("name"),
        "age": data.get("age"),
        "city": data.get("city")
    }

    response = {
        "message": "User added",
        "user": users[username]
    }
    return jsonify(response), 201


if __name__ == "__main__":
    app.run()
