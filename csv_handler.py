import os
import csv

def find_csv_files():
    files = []
    for file in os.listdir():
        if file.endswith('.csv'):
            files.append(file)
    return files

def read(filename):
    with open(filename, 'r') as f:
        reader = csv.reader(f)
        # Check if the file has headers and skip it if necessary
        first_row = next(reader)
        if first_row[0].lower() in ["term", "definition"]:  # Assuming headers are "term" and "definition"
            table = list(reader)
        else:
            table = [first_row] + list(reader)  # No header, so include first row as data
        return table

def write(filename, data):
    with open(filename, 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(data)

