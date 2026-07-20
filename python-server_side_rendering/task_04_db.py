#!/usr/bin/python3
"""Display product data from JSON, CSV, or SQLite sources."""

import csv
import json
import sqlite3
from flask import Flask, render_template, request

app = Flask(__name__)


def read_json(filename):
    """Read product data from a JSON file."""
    with open(filename, encoding='utf-8') as file:
        return json.load(file)


def read_csv(filename):
    """Read product data from a CSV file."""
    products = []

    with open(filename, encoding='utf-8', newline='') as file:
        reader = csv.DictReader(file)

        for row in reader:
            row['id'] = int(row['id'])
            row['price'] = float(row['price'])
            products.append(row)

    return products


def read_sql(filename):
    """Read product data from a SQLite database."""
    connection = sqlite3.connect(filename)
    connection.row_factory = sqlite3.Row
    cursor = connection.cursor()

    cursor.execute(
        'SELECT id, name, category, price FROM Products'
    )

    products = [dict(row) for row in cursor.fetchall()]
    connection.close()

    return products


@app.route('/products')
def products():
    """Display products from the selected data source."""
    source = request.args.get('source')
    product_id = request.args.get('id')
    product_list = []
    error = None

    try:
        if source == 'json':
            product_list = read_json('products.json')
        elif source == 'csv':
            product_list = read_csv('products.csv')
        elif source == 'sql':
            product_list = read_sql('products.db')
        else:
            error = 'Wrong source'
    except (OSError, json.JSONDecodeError, csv.Error, sqlite3.Error):
        error = 'Database error'

    if error is None and product_id is not None:
        try:
            product_id = int(product_id)
            product_list = [
                product for product in product_list
                if product['id'] == product_id
            ]
        except ValueError:
            product_list = []

        if not product_list:
            error = 'Product not found'

    return render_template(
        'product_display.html',
        products=product_list,
        error=error
    )


if __name__ == '__main__':
    app.run(debug=True, port=5000)
