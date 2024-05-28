#!/usr/bin/env python3
import csv
import json


def convert_csv_to_json(csv_filename):
    """
    Converts CSV data to JSON.

    Args:
        csv_filename (str): The name of the CSV file to convert.

    Returns:
        True if the conversion was successful, False otherwise.
    """
    try:
        with open(csv_filename, 'r') as csv_file:
            reader = csv.DictReader(csv_file)
            data = list(reader)

        with open('data.json', 'w') as json_file:
            json.dump(data, json_file)

        return True
    except Exception as e:
        print(f"An error occurred while converting CSV to JSON: {e}")
        return False
