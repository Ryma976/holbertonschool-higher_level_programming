#!/usr/bin/python3
"""
Flask application displaying products from JSON or CSV based on URL params.
"""
import csv
import json
from flask import Flask, render_template, request

app = Flask(__name__)


def read_json_file(filename):
    """Read and parse data from a JSON file."""
    try:
        with open(filename, 'r') as file:
            return json.load(file)
    except Exception:
        return []


def read_csv_file(filename):
    """Read and parse data from a CSV file."""
    products = []
    try:
        with open(filename, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                products.append({
                    'id': int(row['id']),
                    'name': row['name'],
                    'category': row['category'],
                    'price': float(row['price'])
                })
    except Exception:
        pass
    return products


@app.route('/products')
def products():
    """Render product details based on source and optional id."""
    source = request.args.get('source')
    product_id = request.args.get('id')

    if source not in ['json', 'csv']:
        return render_template('product_display.html', error="Wrong source")

    if source == 'json':
        products_list = read_json_file('products.json')
    else:
        products_list = read_csv_file('products.csv')

    if product_id:
        try:
            target_id = int(product_id)
            products_list = [
                p for p in products_list if p.get('id') == target_id
            ]
            if not products_list:
                return render_template(
                    'product_display.html', error="Product not found"
                )
        except ValueError:
            return render_template(
                'product_display.html', error="Product not found"
            )

    return render_template('product_display.html', products=products_list)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
