#!/usr/bin/python3
"""
A secure Flask API demonstrating Basic Auth, JWT, and Role-based access.
"""
from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from flask_jwt_extended import (
    JWTManager, create_access_token, jwt_required, get_jwt_identity, get_jwt
)
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)

# Security configurations
app.config["JWT_SECRET_KEY"] = "super-secret-key-change-in-production"
jwt = JWTManager(app)
basic_auth = HTTPBasicAuth()

# In-memory users database with role management
users = {
    "user1": {
        "username": "user1",
        "password": generate_password_hash("password"),
        "role": "user"
    },
    "admin1": {
        "username": "admin1",
        "password": generate_password_hash("password"),
        "role": "admin"
    }
}


# --- Basic Authentication Setup ---
@basic_auth.verify_password
def verify_password(username, password):
    """Verifies user credentials for Basic Auth."""
    user = users.get(username)
    if user and check_password_hash(user["password"], password):
        return username
    return None


# --- JWT Error Handlers (Ensuring strict 401 response status) ---
@jwt.unauthorized_loader
def handle_unauthorized_error(err):
    return jsonify({"error": "Missing or invalid token"}), 401


@jwt.invalid_token_loader
def handle_invalid_token_error(err):
    return jsonify({"error": "Invalid token"}), 401


@jwt.expired_token_loader
def handle_expired_token_error(err):
    return jsonify({"error": "Token has expired"}), 401


@jwt.revoked_token_loader
def handle_revoked_token_error(err):
    return jsonify({"error": "Token has been revoked"}), 401


@jwt.needs_fresh_token_loader
def handle_needs_fresh_token_error(err):
    return jsonify({"error": "Fresh token required"}), 401


# --- Routes ---
@app.route('/basic-protected')
@basic_auth.login_required
def basic_protected():
    """Route protected by HTTP Basic Authentication."""
    return "Basic Auth: Access Granted"


@app.route('/login', methods=['POST'])
def login():
    """Authenticates a user and generates a JWT access token."""
    data = request.get_json(silent=True)
    if not data:
        return jsonify({"error": "Invalid JSON"}), 400

    username = data.get("username")
    password = data.get("password")

    if not username or not password:
        return jsonify({"error": "Username and password are required"}), 400

    user = users.get(username)
    if user and check_password_hash(user["password"], password):
        # Embed the role into custom claims within the JWT
        additional_claims = {"role": user["role"]}
        token = create_access_token(
            identity=username,
            additional_claims=additional_claims
        )
        return jsonify({"access_token": token}), 200

    return jsonify({"error": "Invalid credentials"}), 401


@app.route('/jwt-protected')
@jwt_required()
def jwt_protected():
    """Route protected by standard JWT Authentication."""
    return "JWT Auth: Access Granted"


@app.route('/admin-only')
@jwt_required()
def admin_only():
    """Route protected by JWT and strict admin role validation."""
    claims = get_jwt()
    if claims.get("role") != "admin":
        return jsonify({"error": "Admin access required"}), 403
    return "Admin Access: Granted"


if __name__ == "__main__":
    app.run()
