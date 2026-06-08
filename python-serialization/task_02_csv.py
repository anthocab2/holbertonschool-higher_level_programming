#!/usr/bin/python3
"""CSV to JSON conversion module."""

import csv
import json


def convert_csv_to_json(filename):
    """Convert CSV data into JSON format and save it to data.json."""
    try:
        with open(filename, "r", encoding="utf-8") as csv_file:
            reader = csv.DictReader(csv_file)
            data = list(reader)

        with open("data.json", "w", encoding="utf-8") as json_file:
            json.dump(data, json_file)

        return True
    except Exception:
        return False
