import os
import csv
import json

if __name__ == "__main__":
    folder_path = "gw_test/Question1/Dataset"
    convert_csv_to_json_in_folder(folder_path)

def convert_csv_to_json_in_folder(folder_path):
    abs_folder_path = os.path.abspath(folder_path)
    for root, _, files in os.walk(abs_folder_path):
        for filename in files:
            if filename.endswith('.csv'):
                csv_file_path = os.path.join(root, filename)
                csv_to_json(csv_file_path)

def csv_to_json(csv_file_path):
    json_file_path = csv_file_path.replace('.csv', '.json')
    
    with open(csv_file_path, 'r') as csv_file:
        reader = csv.reader(csv_file)
        # next(reader)  # Skip header line if present
        data = [
            {
                'x': float(row[0]),
                'y': float(row[1]),
                'width': float(row[2]),
                'height': float(row[3]),
                'tag': row[4],
            }
            for row in reader
        ]
    
    with open(json_file_path, 'w') as json_file:
        json.dump(data, json_file, indent=4)
