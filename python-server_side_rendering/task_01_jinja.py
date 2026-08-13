#!/usr/bin/python3
"""
Flask application rendering HTML pages using Jinja templates.
"""
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    """Render the Home page."""
    return render_template('index.html')


@app.route('/about')
def about():
    """Render the About Us page."""
    return render_template('about.html')


@app.route('/contact')
def contact():
    """Render the Contact Us page."""
    return render_template('contact.html')


if __name__ == '__main__':
    app.run(debug=True, port=5000)
