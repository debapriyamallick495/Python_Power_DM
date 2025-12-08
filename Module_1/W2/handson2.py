#csv data processor

import csv
import json

path = "Module_1/W2/assets/"

def csv_to_json(csv_file, json_file):
    """Convert CSV file to JSON format"""
    try:
        with open(csv_file, 'r') as csvfile:
            csv_reader = csv.DictReader(csvfile)
            data = list(csv_reader)
        
        with open(json_file, 'w') as jsonfile:
            json.dump(data, jsonfile, indent=2)
        
        print(f"Converted {csv_file} to {json_file}")
        print(f"Records processed: {len(data)}")
        
    except FileNotFoundError:
        print("CSV file not found!")
    except Exception as e:
        print(f"Error: {e}")

# Test the function
csv_to_json(path+'employee.csv', path+'employee.json')