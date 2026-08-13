#!/usr/bin/python3
"""
Flask application rendering dynamic list from JSON using Jinja templates.
"""
import json
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    """Render Home page."""
    return render_template('index.html')


@app.route('/about')
def about():
    """Render About Us page."""
    return render_template('about.html')


@app.route('/contact')
def contact():
    """Render Contact page."""
    return render_template('contact.html')


@app.route('/items')
def items():
    """Render Items page with data loaded from items.json."""
    items_list = []
    try:
        with open('items.json', 'r') as file:
            data = json.load(file)
            items_list = data.get('items', [])
    except (FileNotFoundError, json.JSONDecodeError):
        items_list = []

    return render_template('items.html', items=items_list)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
